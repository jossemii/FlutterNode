
SORTER = '041e0bf1e5de0b96b3c2eca17933698819e1021da3e4fa39a2a8eb47493ce432'
RANDOM = '05f6562f4a0a0e1ae92fa9b238fce2a978fbdc204a0d6a58989871b4f0fe95c3'
FRONTIER = '5029ca335ac7e434dac7317d910de20fd0943906019cdf424405e284252f9401'
REGRESION = '8e86f9461f83790bfc1be49543646447ab4704437957bb6c442b8d6a9308f2ac'
WALL = 'f0d6aa3003a74c84ff9242017ecb5ca2e09a6a78c1d2fd932c60fa422a33ffbb'
WALK = 'a449787ebe7a818dd49ff795b135d977c390ff29489108d853989b5d9eb0a6bd'

LISIADO_UNDER = ''
LISIADO_OVER = ''

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.43.180'
MOJITO = '192.168.1.20'
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