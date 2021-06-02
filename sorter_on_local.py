import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2, api_pb2_grpc
from time import sleep

RANDOM = 'e92d52639d2f582d4c9f148ae776abd14ebad4c261d06672e27f317008641200'
FRONTIER = 'e740d93e8e9cbedb917c00ccd9887d934f881ab3812867a596019116ebbb31db'
WALK = '9142c5317ea881d20c5553fbf0403950db5bebfea1e0ea3cd7306febe5b78f98'
WALL = '436b35c87727d8856cdf77fe176a5dbc715bbd8a78dffccbd057ba4f3c15e060'

GATEWAY = '192.168.1.172'

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

# Añade solvers.
for s in [FRONTIER, WALL, WALK]:
    solver = api_pb2.ipss__pb2.Service()
    solver.ParseFromString(open('__registry__/'+s+'.service', 'rb').read())
    c_stub.UploadSolver(solver)

print('Wait to train the model ...')
for i in range(10): 
    # Realiza regresion 20 veces, el tiempo por defecto entre cada una son 900 segundos
    print('TEMPO ', i)
    sleep(900)

print('Vamos a generar un cnf.')

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

sleep(5) # Espera a que el servidor se levante.

cnf = r_stub.RandomCnf(api_pb2.Empty())

print('Our cnf for the test is ', cnf)

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
