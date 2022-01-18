RANDOM = 'b11074a440261eee100bb8751610be5c5cf6efdf9a9a1128de7d61dd93dc0fd9'
FRONTIER = '330c6b059f8d952634b798236d2668b5e636d7f02844e25a55f7c874866da982'
WALL = '3b89558260e54b37f88a4ed08c86fb07858d2841453370f7e7401707e0bb493f'
WALK = '35e98659aea3b6f1c8283dea38712c1389248357e8657a7b684fa39c8add0f97'
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