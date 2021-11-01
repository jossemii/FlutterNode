RANDOM = '0a8f63bfc040dee78ce75f566cebd79ba6a95105653e4a83f44293b1c54a25e3'
FRONTIER = '921e3910a78f345fa0a7924e5f44fd65fe87b6431df4b0b6dce9fb9c6df3155a'
WALL = '52e760af042a8014a8b07bf6a4586991a09e58bf8f7117462fc25e73f546f30d'
WALK = '22a0bd5d09cc5ee6ceed3cca5b8515b9f0bcb22d297603b6177c75bd5b473cee'
LISIADO_UNDER = ''
LISIADO_OVER = ''

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.1.54'
MOJITO = '192.168.1.143'
TEQUILA = '192.168.1.63'
GATEWAY = MOJITO

def generator(hash: str):
    yield gateway_pb2.ServiceTransport(
        hash = gateway_pb2.celaut__pb2.Any.Metadata.HashTag.Hash(
            type = bytes.fromhex(SHA3_256),
            value = bytes.fromhex(hash)
        ),
        config = gateway_pb2.celaut__pb2.Configuration()
    )

# GrpcBigBuffer.
CHUNK_SIZE = 1024 * 1024  # 1MB
import os, shutil, gc
import gateway_pb2
from random import randint
from typing import Generator
from threading import Condition

class Signal():
    # The parser use change() when reads a signal on the buffer.
    # The serializer use wait() for stop to send the buffer if it've to do it.
    # It's thread safe because the open var is only used by one thread (the parser) with the change method.
    def __init__(self, exist: bool = True) -> None:
        self.exist = exist
        if exist: self.open = True
        if exist: self.condition = Condition()
    
    def change(self):
        if self.exist:
            if self.open:
                self.open = False  # Stop the input buffer.
            else:
                with self.condition:
                    self.condition.notify_all()
                self.open = True  # Continue the input buffer.
    
    def wait(self):
        if self.exist and not self.open:
            with self.condition:
                self.condition.wait()

def get_file_chunks(filename, signal = Signal(exist=False)) -> Generator[gateway_pb2.Buffer, None, None]:
    signal.wait()
    try:
        with open(filename, 'rb', buffering = CHUNK_SIZE) as f:
            while True:
                f.flush()
                signal.wait()
                piece = f.read(CHUNK_SIZE)
                if len(piece) == 0: return
                yield gateway_pb2.Buffer(chunk=piece)
    finally: 
        gc.collect()


def save_chunks_to_file(buffer_iterator, filename):
    with open(filename, 'wb') as f:
        f.write(''.join([buffer.chunk for buffer in buffer_iterator]))

def parse_from_buffer(request_iterator, message_field = None, signal = Signal(exist=False), indices: dict = None): # indice: method
    if indices and len(indices) == 1: message_field = list(indices.values())[0]
    while True:
        all_buffer = bytes()
        while True:
            buffer = next(request_iterator)
            # The order of conditions is important.
            if buffer.HasField('head'):
                try:
                    message_field = indices[buffer.head]
                except: pass
            if buffer.HasField('chunk'):
                all_buffer += buffer.chunk
            if buffer.HasField('signal') and buffer.signal:
                signal.change()
                continue
            if buffer.HasField('separator') and buffer.separator: 
                break
        if message_field:
            message = message_field()
            message.ParseFromString(
                all_buffer
            )
            yield message
        else:
            yield all_buffer

def serialize_to_buffer(message_iterator, signal = Signal(exist=False), cache_dir = None, indices: dict = None): # method: indice
    if not hasattr(message_iterator, '__iter__'): message_iterator=[message_iterator]
    for message in message_iterator:
        if type(message) is tuple:
            try:
                yield gateway_pb2.Buffer(
                    head = indices[message[1]]
                )
            except:
                yield gateway_pb2.Buffer(head = 1)
            
            for b in get_file_chunks(filename = message[0], signal = signal):
                yield b
            
            yield gateway_pb2.Buffer(separator = True)

        else: # if message is a protobuf object.
            try:
                    head = indices[type(message)]
            except:  # if not indices or the method not appear on it.
                    head = 1

            message_bytes = message.SerializeToString()
            if len(message_bytes) < CHUNK_SIZE:
                signal.wait()
                try:
                    yield gateway_pb2.Buffer(
                        chunk = bytes(message_bytes),
                        head = head,
                        separator = True
                    )
                finally: signal.wait()

            else:
                try:
                    yield gateway_pb2.Buffer(
                        head = head
                    )
                finally: signal.wait()
    
                try:
                    signal.wait()
                    file = cache_dir + str(len(message_bytes))
                    with open(file, 'wb') as f:
                        f.write(message_bytes)
                    for b in get_file_chunks(file, signal=signal):
                        signal.wait()
                        try:
                            yield b
                        finally: signal.wait()
                finally:
                    try:
                        os.remove(file)
                        gc.collect()
                    except: pass

                try:
                    yield gateway_pb2.Buffer(
                        separator = True
                    )
                finally: signal.wait()

def client_grpc(method, output_field = None, input=None, timeout=None, indices_parser: dict = None, indices_serializer: dict = None): # indice: method
    signal = Signal()
    cache_dir = os.path.abspath(os.curdir) + '/__hycache__/grpcbigbuffer' + str(randint(1,999)) + '/'
    os.mkdir(cache_dir)
    try:
        for b in parse_from_buffer(
            request_iterator = method(
                                serialize_to_buffer(
                                    input if input else '',
                                    signal = signal,
                                    cache_dir = cache_dir,
                                    indices = {e[1]:e[0] for e in indices_serializer.items()} if indices_serializer else None
                                ),
                                timeout = timeout
                            ),
            message_field = output_field,
            signal = signal,
            indices = indices_parser
        ): yield b
    finally:
        try:
            shutil.rmtree(cache_dir)
            gc.collect()
        except: pass


"""
    Serialize Object to plain bytes serialization.
"""
def serialize_to_plain(object: object) -> bytes:
    pass