import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2, api_pb2_grpc
from time import sleep

RANDOM = '09fb4947e59b569eb3dd5726a4e52d7244dc562852559b2efda2a5234f6ff446'
FRONTIER = 'e0613ac5773a46f22d119b0c4fc1f6047f3f90c4cd677edee89bcab76960b208'
WALK = 'ddd36870083b58df28db54391552143e231f1b5d93937efd3cb1dae179dacae6'
WALL = '9d79082de68b72b8c2fb7bcc3a229374cca11794f1b5d2cb5f47a22b9a1c820b'

GATEWAY = '192.168.1.143'

def generator(hash):
    transport = gateway_pb2.ServiceTransport()
    transport.hash = 'sha3-256:'+hash
    transport.config.CopyFrom(gateway_pb2.ipss__pb2.Configuration())
    yield transport

c_stub = api_pb2_grpc.SolverStub(
    grpc.insecure_channel(
        'localhost:8080'
        )
    )

# Inicia el entrenamiento.
c_stub.StartTrain(api_pb2.Empty())


# Obteniendo servicio de cnf's random.
g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel(GATEWAY+':8080')
    )

# While classifier is training get random cnf
random_cnf_service = g_stub.StartService(generator(
    hash=RANDOM
))

print('Servicio random obtenido.')

uri=random_cnf_service.instance.uri_slot[0].uri[0]
r_stub = api_pb2_grpc.RandomStub(
    grpc.insecure_channel(
        uri.ip +':'+ str(uri.port)
        )
    )

# Añade solvers.
for s in [FRONTIER, WALL, WALK]:
    solver = api_pb2.ipss__pb2.Service()
    solver.ParseFromString(open('__registry__/'+s+'.service', 'rb').read())
    c_stub.UploadSolver(solver)

print('Wait to train the model ...')
for i in range(10): 
    sleep(80)
    
    cnf = r_stub.RandomCnf(api_pb2.Empty())
    # Comprueba si sabe generar una interpretacion (sin tener ni idea de que tal
    # ha hecho la seleccion del solver.)
    print('\n ---- ', i)
    print('SOLVING CNF ...')
    interpretation = c_stub.Solve(cnf)
    print('OKAY THE INTERPRETATION WAS ', interpretation)

print('Vamos a generar un cnf.')


# Stop Random cnf service.
g_stub.StopService(random_cnf_service.token)

print('Parando entrenamiento.')



# Termina el entrenamiento.
c_stub.StopTrain(api_pb2.Empty())

print('Entrenamiento parado.')

# Comprueba si sabe generar una interpretacion (sin tener ni idea de que tal
# ha hecho la seleccion del solver.)

print('SOLVING CNF ...')

interpretation = c_stub.Solve(cnf)

print('OKAY THE INTERPRETATION WAS ', interpretation)

input("Press Enter to continue...")
