SORTER = '36c55f054f7eee3702b47dcacae9a9d5259d66d6e7ee88d1cf7401b37c38287e'
RANDOM = 'f4fcda807f35eb2671c731a831e38af4697befbda626d3e7ac900497598b7e4d'
REGRESION = '1877819543342e43684b328c4754142f1de333d73fa438da4a5cd0d0894d3f61'
WALL = ''
WALK = ''
FRONTIER = ''

LISIADO_UNDER = ''
LISIADO_OVER = ''

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.1.16'
MOJITO = '192.168.1.20'
TEQUILA = '192.168.1.17'
GATEWAY = TEQUILA

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