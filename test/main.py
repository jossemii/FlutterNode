SORTER = '08dca216b359cb0495601e6fd8bca0ed57e18ddbba14fe5469ccc4e49c3fb9ef'
RANDOM = 'b0fc076a49adb3d5e03b76996cfe82c81efba9f2115d343a39ee46883c5fdc35'
REGRESION = ''
WALL = ''
WALK = ''
FRONTIER = 'ef109dd8fc1ce1499dc82e1719431651b58d6c277b5981ded05b37246c1722d3'

LISIADO_UNDER = ''
LISIADO_OVER = ''

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.1.16'
MOJITO = '192.168.1.21'
TEQUILA = '192.168.1.17'
LOCALHOST = 'localhost'
CODESPACE = 'jossemii-hypernode-xqvwggjxhr5w-8090.githubpreview.dev'
GATEWAY = CODESPACE

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
