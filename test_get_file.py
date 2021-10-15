from celaut_pb2 import Service
import grpc, gateway_pb2, gateway_pb2_grpc

SORTER = "7bcb1809dbe4fc673c03204e694f65414e6e654ebc70b5495cf117917dfdaf66"
RANDOM = '4bae4b952f0b9fa4f658585965692caa1f530fb1dee2f01f94b451f4abae9c96'
FRONTIER = '038e4eb5ecf1166368ab1d4ee51168f689721ed4a39bbc90efa6eb4995b26953'
WALL = '7d05071d88751a6f378fe32bee204380cb3c95574c0cc47368efc00f81a81971'
WALK = '8012f59dd6ea6471ac9b8d18c6b7594237d1e03206e3e66693c2168793a5f6f2'
LISIADO_UNDER = '4c7b30d0960171cce80faa2752f2470c704bf72840a405c7f950be5b2e870903'
LISIADO_OVER = 'bb64cd53a47ebe6f84cd086254eb66ccfdfaa983d0435c32e48703dcfc819b67'

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.1.54'
MOJITO = '192.168.1.144'
TEQUILA = '192.168.1.63'
GATEWAY = MOJITO

def generator():
    yield gateway_pb2.celaut__pb2.Any.Metadata.HashTag.Hash(
        type = bytes.fromhex(SHA3_256),
        value = bytes.fromhex(FRONTIER)
    )

# Start the script.
g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel(GATEWAY+':8080')
)

any = g_stub.GetFile(
    generator()
)

print('Any -> ', any)

service = Service()
service.ParseFromString(any.value)
print('Service -> ', service)