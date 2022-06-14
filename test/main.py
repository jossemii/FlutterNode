SORTER = 'a305fe12465d9ef8b9b42716f025bf29403cc3421ab9d11fcc601075c0f3dc8c'
RANDOM = 'b0fc076a49adb3d5e03b76996cfe82c81efba9f2115d343a39ee46883c5fdc35'
REGRESION = ''
WALL = ''
WALK = ''
FRONTIER = '0f737f69a2b015099d1d6999fe45f22d258c9ca43f51e912a18b3ed2c658b11f'

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