RANDOM = '16426da109eed68c89bf32bcbcab208649f01d608116f1dda15e12d55fc95456'
FRONTIER = '66a6b7547e29745cdf77cd365072cf08ed6e4edaf32a8fa0976dcd194f1c90a5'
WALL = '47744b30d73d12235f80be88e6e665d5f2d4784f9ca90a12bc9e002633fd9b3e'
WALK = '60610f898fc859ca133cb971e9fd757fbf40513e60eee0a0f937994781922cdd'
LISIADO_UNDER = ''
LISIADO_OVER = ''

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.1.54'
MOJITO = '192.168.1.143'
TEQUILA = '192.168.1.63'
GATEWAY = MOJITO

def generator(hash: str):
    yield gateway_pb2.HashWithConfig(
        hash = gateway_pb2.celaut__pb2.Any.Metadata.HashTag.Hash(
            type = bytes.fromhex(SHA3_256),
            value = bytes.fromhex(hash)
        ),
        config = gateway_pb2.celaut__pb2.Configuration()
    )
    yield ('__registry__/' + hash, gateway_pb2.celaut__pb2.Any)