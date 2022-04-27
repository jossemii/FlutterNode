from random import randint
from celaut_pb2 import Configuration
import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2, api_pb2_grpc, threading, json, solvers_dataset_pb2, celaut_pb2
from time import sleep, time
from grpcbigbuffer import Dir


SORTER = '6d5623124bdc0c06a4347056adbf013a3ca512f9e7916dd7f1d1e0b62c172ef5'
RANDOM = '05f6562f4a0a0e1ae92fa9b238fce2a978fbdc204a0d6a58989871b4f0fe95c3'
FRONTIER = 'e56f7e2503319d8d6b8b4bb11fb7fbd2c0a892628878fea1faed32e202adf85f'
WALL = '81694e37a0a4d9dc98dcf649ce5e9db1f9108e0b24cc16524561472f3bbdb6a8'
WALK = 'ba54c6053ee21d7eb819331515aede8d5ce7e9c46c614e36abcc81a9cf73c6dc'
LISIADO_UNDER = ''
LISIADO_OVER = ''

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.1.16'
MOJITO = '192.168.1.20'
GATEWAY = WHISKY

def is_good(cnf, interpretation):
    def good_clause(clause, interpretation):
        for var in clause.literal:
            for i in interpretation.variable:
                if var == i:
                    return True
        return False

    for clause in cnf.clause:
        if not good_clause(clause, interpretation):
            return False
    return True

def generator(hash: str, mem_limit: int = 50*pow(10, 6)):
    yield gateway_pb2.HashWithConfig(
        hash = celaut_pb2.Any.Metadata.HashTag.Hash(
            type = bytes.fromhex(SHA3_256),
            value = bytes.fromhex(hash)
        ),
        config = celaut_pb2.Configuration(),
        min_sysreq = celaut_pb2.Sysparams(
            mem_limit = mem_limit
        )
    )

    # Send partition model.
    yield ( 
        gateway_pb2.ServiceWithMeta,
        Dir('__registry__/'+hash)
    ) 


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
    classifier = g_stub.StartService(
        generator(
            hash = SORTER
        )
    )
    print(classifier)
    uri=classifier.instance.uri_slot[0].uri[0]
    c_uri = uri.ip +':'+ str(uri.port)
    c_stub = api_pb2_grpc.SolverStub(
        grpc.insecure_channel(c_uri)
        )
    print('Tenemos clasificador. ', c_stub)

    # Get random cnf
    random_cnf_service = g_stub.StartService(generator(
        hash=RANDOM,
        mem_limit = 150*pow(10, 6)
    ))
    print(random_cnf_service)
    uri=random_cnf_service.instance.uri_slot[0].uri[0]
    r_uri = uri.ip +':'+ str(uri.port)
    r_stub = api_pb2_grpc.RandomStub(
        grpc.insecure_channel(r_uri)
        )
    print('Tenemos random. ', r_stub)

    if FRONTIER != '':
        # Get the frontier for test it.
        uri=g_stub.StartService(generator(
            hash=FRONTIER
        )).instance.uri_slot[0].uri[0]
        frontier_uri = uri.ip +':'+ str(uri.port)
        frontier_stub = api_pb2_grpc.SolverStub(
            grpc.insecure_channel(frontier_uri)
            )

        print('Tenemos frontier ', frontier_stub)

    # save stubs on json.
    with open('script_data.json', 'w') as file:
        json.dump({
            'sorter': c_uri,
            'random': r_uri,
            #'frontier': frontier_uri,
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
        frontier_stub = api_pb2_grpc.SolverStub(
            grpc.insecure_channel(data['frontier'])
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
    for s in  [LISIADO_UNDER, LISIADO_OVER ]:#, FRONTIER, WALL, WALK]:
        print('     ', s)
        any = api_pb2.celaut__pb2.Any()
        any.ParseFromString(open('__registry__/'+s, 'rb').read())
        service = api_pb2.celaut__pb2.Service()
        service.ParseFromString(any.value)
        c_stub.UploadSolver(
            api_pb2.ServiceWithMeta(
                meta = any.metadata,
                service = service
            )
        )


    print('Wait to train the model ...')
    for i in range(10): 
        for j in range(5):
            print(' time ', i, j)
            sleep(200)
        
        cnf = r_stub.RandomCnf(api_pb2.Empty())
        # Comprueba si sabe generar una interpretacion (sin tener ni idea de que tal
        # ha hecho la seleccion del solver.)
        print('\n ---- ', i)

        print(' SOLVING CNF ...')
        t = time()
        interpretation = c_stub.Solve(cnf)
        print(str(time()-t)+' OKAY THE INTERPRETATION WAS ', interpretation, '.', is_good(interpretation))

        print(' SOLVING CNF ON DIRECT SOLVER ...')
        t = time()
        try:
            interpretation = frontier_stub.Solve(cnf)
        except(grpc.RpcError):
                # Get the frontier for test it.
                uri=g_stub.StartService(generator(
                    hash=FRONTIER
                )).instance.uri_slot[0].uri[0]
                frontier_uri = uri.ip +':'+ str(uri.port)
                frontier_stub = api_pb2_grpc.SolverStub(
                    grpc.insecure_channel(frontier_uri)
                    )
                interpretation = frontier_stub.Solve(cnf)
        print(str(time()-t)+' OKAY THE FRONTIER SAID ', interpretation, '.', is_good(interpretation))

        print('Obtiene el data_set.')
        open('dataset.bin', 'wb').write(c_stub.GetDataSet(api_pb2.Empty()).SerializeToString())

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
    for j in range(10):
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
