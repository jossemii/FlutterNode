import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2, api_pb2_grpc
from time import sleep

SORTER = "e472e695f0f353fb366730f49136b62f783cf7a7e7ce9c7ac534c76a68248114"
RANDOM = '59711af0372a8b1785bc7af60037e4e97aa2992bb47600c9a9b1cd2a1e424008'
FRONTIER = 'e740d93e8e9cbedb917c00ccd9887d934f881ab3812867a596019116ebbb31db'
WALK = '9142c5317ea881d20c5553fbf0403950db5bebfea1e0ea3cd7306febe5b78f98'
WALL = '436b35c87727d8856cdf77fe176a5dbc715bbd8a78dffccbd057ba4f3c15e060'

GATEWAY = '192.168.1.143'

def generator(hash):
    transport = gateway_pb2.ServiceTransport()
    transport.hash = 'sha3-256:'+hash
    transport.config.CopyFrom(gateway_pb2.ipss__pb2.Configuration())
    yield transport

g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel(GATEWAY+':8080')
    )




# Get a classifier.
classifier = g_stub.StartService(generator(
    hash=SORTER
))

uri=classifier.instance.uri_slot[0].uri[0]

c_stub = api_pb2_grpc.SolverStub(
    grpc.insecure_channel(
        uri.ip +':'+ str(uri.port)
        )
    )

# Inicia el entrenamiento.
c_stub.StartTrain(api_pb2.Empty())

# Añade solvers.
for s in [FRONTIER, WALL, WALK]:
    solver = api_pb2.ipss__pb2.Service()
    solver.ParseFromString(open('__registry__/'+s+'.service', 'rb').read())
    c_stub.UploadSolver(solver)

print('Wait to train the model ...')
sleep(200)



# While classifier is training get random cnf
random_cnf_service = g_stub.StartService(generator(
    hash=RANDOM
))

uri=random_cnf_service.instance.uri_slot[0].uri[0]
r_stub = api_pb2_grpc.RandomStub(
    grpc.insecure_channel(
        uri.ip +':'+ str(uri.port)
        )
    )

cnf = r_stub.RandomCnf(api_pb2.Empty())

# Stop Random cnf service.
g_stub.StopService(random_cnf_service.token)
print('Our cnf for the test is ', cnf)




# Termina el entrenamiento.
c_stub.StopTrain(api_pb2.Empty())

# Comprueba si sabe generar una interpretacion (sin tener ni idea de que tal
# ha hecho la seleccion del solver.)

print('SOLVING CNF ...')

interpretation = c_stub.Solve(cnf)

print('OKAY THE INTERPRETATION WAS ', interpretation)

input("Press Enter to continue...")



# Stop the classifier.
g_stub.StopService(classifier.token)
