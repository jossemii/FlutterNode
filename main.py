RANDOM = 'b7b31b23f9c236b2bee3e27e48f8e592128e33e7c9519922db151c4d6c6d8ec3'
FRONTIER = '1b843c8c42ccc6f364f2e8382e01733c2653c27b425e702e3c9b1de9d93bddbd'
WALL = '8c24a0726ff2a82ff1e66a65cb287ac7ab36262d171e56faf8784ffb5aef9748'
WALK = 'b1376051fcb0218eb66b97f7efee150880edb7434f3afc04252641c43551897f'
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

def parse_from_buffer(request_iterator, message_field = None) -> Generator:
    while True:
        all_buffer = ''
        for buffer in request_iterator:
            if buffer.separator:
                break
            all_buffer.append(buffer.chunk)
        
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
        for chunk in message.SerializeToString().read(CHUNK_SIZE):
            yield gateway_pb2.Buffer(
                chunk = chunk
            )
        yield gateway_pb2.Buffer(
            separator = ''
        )


def client_grpc(method, output_field = None, input=None, timeout=None) -> Generator:
    return parse_from_buffer(
        request_iterator = method(
                            serialize_to_buffer(
                                input if input else ''
                            ),
                            timeout = timeout
                        ),
        message_field = output_field
    )

def generator(hash: str):
    yield gateway_pb2.ServiceTransport(
        hash = gateway_pb2.celaut__pb2.Any.Metadata.HashTag.Hash(
            type = bytes.fromhex(SHA3_256),
            value = bytes.fromhex(hash)
        ),
        config = gateway_pb2.celaut__pb2.Configuration()
    )