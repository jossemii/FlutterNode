RANDOM = '05f6562f4a0a0e1ae92fa9b238fce2a978fbdc204a0d6a58989871b4f0fe95c3'
FRONTIER = 'e56f7e2503319d8d6b8b4bb11fb7fbd2c0a892628878fea1faed32e202adf85f'
REGRESION = '8e86f9461f83790bfc1be49543646447ab4704437957bb6c442b8d6a9308f2ac'
WALL = '81694e37a0a4d9dc98dcf649ce5e9db1f9108e0b24cc16524561472f3bbdb6a8'
WALK = 'ba54c6053ee21d7eb819331515aede8d5ce7e9c46c614e36abcc81a9cf73c6dc'

LISIADO_UNDER = ''
LISIADO_OVER = ''
FRONTIER_X86 = "a7633ebc4dcea1f82c8850d0c2262c8e2080969ba08d9f587065e737d36f7e79"

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.43.180'
MOJITO = ''
TEQUILA = '192.168.43.35'
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