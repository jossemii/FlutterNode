RANDOM = ''
FRONTIER = ''
WALL = ''
WALK = ''
LISIADO_UNDER = ''
LISIADO_OVER = ''

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.1.54'
MOJITO = '192.168.1.144'
TEQUILA = '192.168.1.63'
GATEWAY = MOJITO


CHUNK_SIZE = 1024 * 1024  # 1MB

from typing import Generator
import gateway_pb2

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

def parse_from_buffer(request_iterator, message_field = None):
    while True:
        all_buffer = bytes('', encoding='utf-8')
        for buffer in request_iterator:
            if buffer.separator:
                break
            all_buffer += buffer.chunk
        
        if message_field: 
            message = message_field()
            message.ParseFromString(
                all_buffer
            )            
            yield message
        else:
            yield all_buffer # Clean buffer index bytes.

def serialize_to_buffer(message_iterator):
    if not hasattr(message_iterator, '__iter__'): message_iterator=[message_iterator]
    for message in message_iterator:
        byte_list = list(message.SerializeToString())
        for chunk in [byte_list[i:i + CHUNK_SIZE] for i in range(0, len(byte_list), CHUNK_SIZE)]:
            buffer =  gateway_pb2.Buffer(
                chunk = bytes(chunk)
            )
            yield buffer
        yield gateway_pb2.Buffer(
            separator = bytes('', encoding='utf-8')
        )

def client_grpc(method, output_field = None, input=None, timeout=None):
    for b in parse_from_buffer(
        request_iterator = method(
                            serialize_to_buffer(
                                input if input else ''
                            ),
                            timeout = timeout
                        ),
        message_field = output_field
    ): yield b