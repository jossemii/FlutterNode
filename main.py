RANDOM = 'ba2a1ae598c805782adc94fea8d620e5c7ea1cfabc2eeca0e2d7d6adb4e82d0c'
FRONTIER = 'd99d13e4216d51cee12ec1042a7f3562dbd49952f207e0dbe8d509bfbb081d57'
WALL = '0a36361f4244357c82f76243d419595b6dbd50da5a2c49ce3108a0797b192d8b'
WALK = 'ff9180ceb61fc82f4bccb89a51017dadc352be8f9491c098898db81d933d1b55'
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