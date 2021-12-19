RANDOM = 'ce280312d1440957ef39ed9695e01b7ae0eed1690834d18170446b976fd32204'
FRONTIER = ''
WALL = ''
WALK = ''
LISIADO_UNDER = ''
LISIADO_OVER = ''

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.1.54'
MOJITO = '192.168.1.143'
TEQUILA = '192.168.1.63'
GATEWAY = 'localhost'

import gateway_pb2

def generator(hash: str):
    yield gateway_pb2.HashWithConfig(
        hash = gateway_pb2.celaut__pb2.Any.Metadata.HashTag.Hash(
            type = bytes.fromhex(SHA3_256),
            value = bytes.fromhex(hash)
        ),
        config = gateway_pb2.celaut__pb2.Configuration()
    )
    
    # Get the two partitions of the Service with metadata.
    yield (
        gateway_pb2.ServiceWithMeta, 
        '__registry__/' + hash,
    )