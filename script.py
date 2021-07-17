import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2, api_pb2_grpc, threading, json
from six import with_metaclass
from time import sleep, time

SORTER = "e15dc1dc49db2c01564e20dbaab95f085f03c9259ecc05c0e5a3336f4ef5378c"
RANDOM = 'e92d52639d2f582d4c9f148ae776abd14ebad4c261d06672e27f317008641200'
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

if open('script_data.json', 'r').read() == '':
    uri=classifier.instance.uri_slot[0].uri[0]

    c_stub = api_pb2_grpc.SolverStub(
        grpc.insecure_channel(
            uri.ip +':'+ str(uri.port)
            )
        )

    print('Tenemos clasificador. ', c_stub)

    sleep(10) # Espera a que el servidor se levante.

    # Get random cnf
    random_cnf_service = g_stub.StartService(generator(
        hash=RANDOM
    ))

    uri=random_cnf_service.instance.uri_slot[0].uri[0]
    r_stub = api_pb2_grpc.RandomStub(
        grpc.insecure_channel(
            uri.ip +':'+ str(uri.port)
            )
        )

    print('Tenemos random. ', r_stub)

    # save stubs on json.
    with open('script_data.json', 'w') as data:
        data.write(json.dumps({
            'sorter': c_stub.__dict__,
            'random': r_stub.__dict__
        }))

else:
    print('Getting from json file.')
    with open('script_data.json', 'r') as file:
        c_stub = json.loads(json.dumps(file.read()['sorter']), object_hook=api_pb2_grpc.SolverStub)
        r_stub = json.loads(json.dumps(file.read()['random']), object_hook=api_pb2_grpc.RandomStub)


print('Iniciando entrenamiento...')
# Inicia el entrenamiento.
c_stub.StartTrain(api_pb2.Empty())



print('Subiendo solvers al clasificador.')
# Añade solvers.
for s in [FRONTIER, WALL, WALK]:
    print('     ', s)
    solver = api_pb2.ipss__pb2.Service()
    solver.ParseFromString(open('__registry__/'+s+'.service', 'rb').read())
    c_stub.UploadSolver(solver)


print('Wait to train the model ...')
for i in range(5): 
    for j in range(10):
        print(' time ', i, j)
        sleep(200)
    
    cnf = r_stub.RandomCnf(api_pb2.Empty())
    # Comprueba si sabe generar una interpretacion (sin tener ni idea de que tal
    # ha hecho la seleccion del solver.)
    print('\n ---- ', i)
    print(' SOLVING CNF ...')
    t = time()
    interpretation = c_stub.Solve(cnf)
    print(interpretation, str(time()-t)+' OKAY THE INTERPRETATION WAS ')

print('Termina el entrenamiento')
# Termina el entrenamiento.
c_stub.StopTrain(api_pb2.Empty())

sleep(100)

# Comprueba si sabe generar una interpretacion (sin tener ni idea de que tal
# ha hecho la seleccion del solver.)
def final_test(c_stub, r_stub, i, j):
    cnf = r_stub.RandomCnf(api_pb2.Empty())
    t = time()
    interpretation = c_stub.Solve(cnf)
    print(interpretation, str(time()-t)+'THE FINAL INTERPRETATION IN THREAD '+threading.get_ident(),' last time ', i, j)

def logs(c_stub):
    for file in c_stub.StreamLogs(api_pb2.Empty()):
        print('\n\nNEW FILE.', file.file)

for i in range(20):
    sleep(10)
    threads = []
    for j in range(10 if i%2==0 else 4):
        t = threading.Thread(target=final_test, args=(c_stub, r_stub, i, j, ))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

l = threading.Thread(target=logs, args=(c_stub, ))
l.start()

print('Obtiene el tensor.')
counter = 6
for tensor in c_stub.GetTensor(api_pb2.Empty()):
    print('\n\nTENSOR -> ', tensor)
    sleep(10)
    if counter==0: break
    else: counter-=1

l.join()
# Stop the classifier.
g_stub.StopService(classifier.token)

# Stop Random cnf service.
g_stub.StopService(random_cnf_service.token)
print('All good?')

with open('script_data.json', 'w') as file:
    file.write(json.dumps(''))