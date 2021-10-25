RANDOM = '0a8f63bfc040dee78ce75f566cebd79ba6a95105653e4a83f44293b1c54a25e3'
FRONTIER = '921e3910a78f345fa0a7924e5f44fd65fe87b6431df4b0b6dce9fb9c6df3155a'
WALL = '52e760af042a8014a8b07bf6a4586991a09e58bf8f7117462fc25e73f546f30d'
WALK = '22a0bd5d09cc5ee6ceed3cca5b8515b9f0bcb22d297603b6177c75bd5b473cee'
LISIADO_UNDER = ''
LISIADO_OVER = ''

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.1.54'
MOJITO = '192.168.1.144'
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

CHUNK_SIZE = 1024 * 1024  # 1MB
import os, shutil
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

def get_file_chunks(filename) -> Generator[gateway_pb2.Buffer, None, None]:
    with open(filename, 'rb') as f:
        while True:
            piece = f.read(CHUNK_SIZE);
            if len(piece) == 0:
                return
            yield gateway_pb2.Buffer(chunk=piece)


def save_chunks_to_file(chunks: gateway_pb2.Buffer, filename):
    with open(filename, 'wb') as f:
        for buffer in chunks:
            f.write(buffer.chunk)

def parse_from_buffer(request_iterator, message_field = None, signal = Signal(exist=False)):
    while True:
        all_buffer = bytes('', encoding='utf-8')
        while True:
            buffer = next(request_iterator)
            if buffer.HasField('separator'):
                break
            if buffer.HasField('signal'):
                signal.change()
                continue
            if buffer.HasField('chunk'):
                all_buffer += buffer.chunk
        if message_field: 
            message = message_field()
            message.ParseFromString(
                all_buffer
            )
            yield message
        else:
            yield all_buffer # Clean buffer index bytes.

def serialize_to_buffer(message_iterator, signal = Signal(exist=False), cache_dir = None):
    if not hasattr(message_iterator, '__iter__'): message_iterator=[message_iterator]
    for message in message_iterator:
        message_bytes = message.SerializeToString()
        if len(message_bytes) < CHUNK_SIZE:
            signal.wait()
            try:
                yield gateway_pb2.Buffer(
                    chunk = bytes(message_bytes)
                )
            finally: signal.wait()
        else:
            try:
                signal.wait()
                print('vamos a pasar todo a lista ', len(message_bytes))
                byte_list = list(message_bytes)
                for chunk in [byte_list[i:i + CHUNK_SIZE] for i in range(0, len(byte_list), CHUNK_SIZE)]:
                    signal.wait()
                    try:
                        yield gateway_pb2.Buffer(
                                        chunk = bytes(chunk)
                                    )
                    finally: signal.wait()
            except: # INEFICIENT.    
                try:
                    signal.wait()
                    print('vamos a escribir en cache ', len(message_bytes))
                    file = cache_dir + str(len(message_bytes))
                    open(file, 'wb').write(message_bytes)
                    for b in get_file_chunks(file): 
                        signal.wait()
                        try:
                            yield b
                        finally: signal.wait()
                finally:
                    try:
                        os.remove(file)
                    except: pass

        try:
            yield gateway_pb2.Buffer(
                separator = bytes('', encoding='utf-8')
            )
        finally: signal.wait()

def client_grpc(method, output_field = None, input=None, timeout=None):
    signal = Signal()
    cache_dir = os.path.abspath(os.curdir) + '/__hycache__/grpcbigbuffer' + str(randint(1,999)) + '/'
    os.mkdir(cache_dir)
    try:
        for b in parse_from_buffer(
            request_iterator = method(
                                serialize_to_buffer(
                                    input if input else '',
                                    signal = signal,
                                    cache_dir = cache_dir
                                ),
                                timeout = timeout
                            ),
            message_field = output_field,
            signal = signal
        ): yield b
    finally:
        try:
            shutil.rmtree(cache_dir)
        except: pass