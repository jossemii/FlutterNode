RANDOM = '05f6562f4a0a0e1ae92fa9b238fce2a978fbdc204a0d6a58989871b4f0fe95c3'
FRONTIER = 'e56f7e2503319d8d6b8b4bb11fb7fbd2c0a892628878fea1faed32e202adf85f'
REGRESION = '8e86f9461f83790bfc1be49543646447ab4704437957bb6c442b8d6a9308f2ac'
WALL = ''
WALK = ''
LISIADO_UNDER = ''
LISIADO_OVER = ''

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.1.54'
MOJITO = '192.168.1.143'
TEQUILA = '192.168.1.63'
GATEWAY = 'localhost'

import celaut_pb2, gateway_pb2
from grpcbigbuffer import Dir

def generator(hash: str):
    yield gateway_pb2.HashWithConfig(
        hash = celaut_pb2.Any.Metadata.HashTag.Hash(
            type = bytes.fromhex(SHA3_256),
            value = bytes.fromhex(hash)
        ),
        config = celaut_pb2.Configuration()
    )

    # Send partition model.
    yield (
        gateway_pb2.ServiceWithMeta,
        Dir('__registry__/'+hash)
    )