import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2_grpc, api_pb2, celaut_pb2

from main import GATEWAY, FRONTIER, client_grpc, generator

def get_grpc_uri(instance: celaut_pb2.Instance) -> celaut_pb2.Instance.Uri:
    for slot in instance.api.slot:
        #if 'grpc' in slot.transport_protocol.metadata.tag and 'http2' in slot.transport_protocol.metadata.tag:
            # If the protobuf lib. supported map for this message it could be O(n).
        for uri_slot in instance.uri_slot:
            if uri_slot.internal_port == slot.port:
                return uri_slot.uri[0]
    raise Exception('Grpc over Http/2 not supported on this service ' + str(instance))


g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel(GATEWAY + ':8080'),
)

print('Get new services....')

c_stub = api_pb2_grpc.SolverStub(
    grpc.insecure_channel('localhost:8080')
    )

print('Tenemos clasificador. ', c_stub)

# Get random cnf
service = next(client_grpc(
    method = g_stub.StartService,
    output_field=gateway_pb2.Instance,
    input=generator(hash=FRONTIER)
))

uri = get_grpc_uri(service.instance)
random_stub = api_pb2_grpc.RandomStub(
    grpc.insecure_channel(
        uri.ip + ':' + str(uri.port)
    )
)
random_token = service.token

print('RANDOM SERVICE -> ', uri, random_token)

"""
cnf = next(client_grpc(
            method = random_stub.RandomCnf,
            input = api_pb2.Empty(),
            output_field = api_pb2.Cnf
))

print('Cnf -> ', cnf)
"""
