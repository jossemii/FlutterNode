import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2, api_pb2_grpc, threading, json, sys
from time import sleep, time

if input('Clean json data? (y/n)') == 'y':
    print('\nClearing data ...')
    with open('script_data.json', 'w') as file:
        json.dump("", file)

SORTER = "6565343d16cc49f998f0313d787a43a1ec42324fb3f2103f661672a2745f0ed1"
RANDOM = '09fb4947e59b569eb3dd5726a4e52d7244dc562852559b2efda2a5234f6ff446'
FRONTIER = 'e0613ac5773a46f22d119b0c4fc1f6047f3f90c4cd677edee89bcab76960b208'
WALK = 'ddd36870083b58df28db54391552143e231f1b5d93937efd3cb1dae179dacae6'
WALL = '9d79082de68b72b8c2fb7bcc3a229374cca11794f1b5d2cb5f47a22b9a1c820b'

WHISKY = '192.168.1.114'
MOJITO = '192.168.1.143'
GATEWAY = MOJITO

def generator(hash):
    transport = gateway_pb2.ServiceTransport()
    transport.hash = 'sha3-256:'+hash
    transport.config.CopyFrom(gateway_pb2.ipss__pb2.Configuration())
    yield transport

g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel(GATEWAY+':8080')
    )

print(json.load(open('script_data.json', 'r')))
if type(json.load(open('script_data.json', 'r'))) != dict:

    print('Get new services....')
    # Get a classifier.
    classifier = g_stub.StartService(generator(
        hash=SORTER
    ))
    print(classifier)

    uri=classifier.instance.uri_slot[0].uri[0]
    c_uri = uri.ip +':'+ str(uri.port)
    c_stub = api_pb2_grpc.SolverStub(
        grpc.insecure_channel(c_uri)
        )

    print('Tenemos clasificador. ', c_stub)

    # Get random cnf
    random_cnf_service = g_stub.StartService(generator(
        hash=RANDOM
    ))

    print(random_cnf_service)
    uri=random_cnf_service.instance.uri_slot[0].uri[0]
    r_uri = uri.ip +':'+ str(uri.port)
    r_stub = api_pb2_grpc.RandomStub(
        grpc.insecure_channel(r_uri)
        )

    print('Tenemos random. ', r_stub)

    # save stubs on json.
    with open('script_data.json', 'w') as file:
        json.dump({
            'sorter': c_uri,
            'random': r_uri
        }, file)

else:
    print('Getting from json file.')
    with open('script_data.json', 'r') as file:
        data = json.load(file)
        print(data)
        c_stub = api_pb2_grpc.SolverStub(
            grpc.insecure_channel(data['sorter'])
        )
        r_stub = api_pb2_grpc.RandomStub(
            grpc.insecure_channel(data['random'])
        )

sleep(10) # Espera a que el servidor se levante.

if input("\nGo to train? (y/n)")=='y':
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

    sleep(100)

print('Termina el entrenamiento')
# En caso de que estubiera entrenando lo finaliza.
c_stub.StopTrain(api_pb2.Empty())

# Comprueba si sabe generar una interpretacion (sin tener ni idea de que tal
# ha hecho la seleccion del solver.)
def final_test(c_stub, r_stub, i, j):
    cnf = r_stub.RandomCnf(api_pb2.Empty())
    t = time()
    interpretation = c_stub.Solve(cnf)
    print(interpretation, str(time()-t)+'THE FINAL INTERPRETATION IN THREAD '+str(threading.get_ident()),' last time ', i, j)

def logs(c_stub):
    for file in c_stub.StreamLogs(api_pb2.Empty()):
        print('\n\nNEW FILE.', file.file)

for i in range(3):
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

print('waiting for kill solvers ...')
sleep(200)

# Stop the classifier.
g_stub.StopService(classifier.token)

# Stop Random cnf service.
g_stub.StopService(random_cnf_service.token)
print('All good?')

with open('script_data.json', 'w') as file:
    print('Clearing data ...')
    json.dump("", file)
