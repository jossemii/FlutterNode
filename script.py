import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2, api_pb2_grpc, threading, json, solvers_dataset_pb2
from time import sleep, time


SORTER = "7f653471c8a51f1a10ebb50c9b61a2bf4d4844e871c98e217bc311271a7a5b18"
RANDOM = '4bae4b952f0b9fa4f658585965692caa1f530fb1dee2f01f94b451f4abae9c96'
FRONTIER = '038e4eb5ecf1166368ab1d4ee51168f689721ed4a39bbc90efa6eb4995b26953'
WALL = '7d05071d88751a6f378fe32bee204380cb3c95574c0cc47368efc00f81a81971'
WALK = '8012f59dd6ea6471ac9b8d18c6b7594237d1e03206e3e66693c2168793a5f6f2'

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.1.114'
MOJITO = '192.168.1.143'
TEQUILA = '192.168.1.63'
GATEWAY = TEQUILA

def generator(hash: str):
    transport = gateway_pb2.ServiceTransport()
    transport.hash.type = bytes.fromhex(SHA3_256)
    transport.hash.value = bytes.fromhex(hash)
    transport.config.CopyFrom(gateway_pb2.ipss__pb2.Configuration())
    yield transport


# Start the script.

if input('Clean json data? (y/n)') == 'y':
    print('\nClearing data ...')
    with open('script_data.json', 'w') as file:
        json.dump("", file)

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

try:
    dataset = solvers_dataset_pb2.DataSet()
    dataset.ParseFromString(open('dataset.bin', 'rb').read())
    c_stub.AddDataSet(dataset)
    print('Dataset añadido.')
except Exception as e:
    print('No tenemos dataset.')
    pass

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

for i in range(3):
    sleep(10)
    threads = []
    for j in range(10 if i%2==0 else 4):
        t = threading.Thread(target=final_test, args=(c_stub, r_stub, i, j, ))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

"""
print('Obtiene el tensor.')
counter = 6
for tensor in c_stub.GetTensor(api_pb2.Empty()):
    print('\n\nTENSOR -> ', tensor)
    sleep(10)
    if counter==0: break
    else: counter-=1
"""

print('Obtiene el data_set.')
dataset = c_stub.GetDataSet(api_pb2.Empty())
print('\n\DATASET -> ', dataset)
open('dataset.bin', 'wb').write(dataset.SerializeToString())


print('waiting for kill solvers ...')
for i in range(10):
    for j in range(10):
        sleep(10)
        print(i, j)

# Stop the classifier.
print('Stop the clasifier.')
g_stub.StopService(gateway_pb2.TokenMessage(token=classifier.token))

# Stop Random cnf service.
g_stub.StopService(gateway_pb2.TokenMessage(token=random_cnf_service.token))
print('All good?')

with open('script_data.json', 'w') as file:
    print('Clearing data ...')
    json.dump("", file)
