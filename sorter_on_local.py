from celaut_pb2 import Service
import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2, api_pb2_grpc, threading, json, solvers_dataset_pb2
from time import sleep, time

RANDOM = 'b7b31b23f9c236b2bee3e27e48f8e592128e33e7c9519922db151c4d6c6d8ec3'
FRONTIER = '1b843c8c42ccc6f364f2e8382e01733c2653c27b425e702e3c9b1de9d93bddbd'
WALL = '8c24a0726ff2a82ff1e66a65cb287ac7ab36262d171e56faf8784ffb5aef9748'
WALK = 'b1376051fcb0218eb66b97f7efee150880edb7434f3afc04252641c43551897f'
LISIADO_UNDER = ''
LISIADO_OVER = ''

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.1.54'
MOJITO = '192.168.1.144'
TEQUILA = '192.168.1.63'
GATEWAY = MOJITO

def generator(hash: str):
    yield gateway_pb2.ServiceTransport(
        hash = gateway_pb2.celaut__pb2.Any.Metadata.HashTag.Hash(
            type = bytes.fromhex(SHA3_256),
            value = bytes.fromhex(hash)
        ),
        config = gateway_pb2.celaut__pb2.Configuration()
    )



g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel(GATEWAY + ':8080')
)

print('Get new services....')

c_stub = api_pb2_grpc.SolverStub(
    grpc.insecure_channel('localhost:8080')
    )

print('Tenemos clasificador. ', c_stub)

# Get random cnf
random_cnf_service = g_stub.StartService(
    generator(
        hash = RANDOM
    )
)

print(random_cnf_service)
uri=random_cnf_service.instance.uri_slot[0].uri[0]
r_uri = uri.ip +':'+ str(uri.port)
r_stub = api_pb2_grpc.RandomStub(
    grpc.insecure_channel(r_uri)
    )

print('Tenemos random. ', r_stub)

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
    for s in [FRONTIER, WALK, WALL]:
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
    for i in range(50): 
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

    sleep(60)

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


for i in range(1):
    sleep(10)
    threads = []
    for j in range(4):
        t = threading.Thread(target=final_test, args=(c_stub, r_stub, i, j, ))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

print('Obtiene el data_set.')
dataset = c_stub.GetDataSet(api_pb2.Empty())
print('\n\DATASET -> ', dataset)
open('dataset.bin', 'wb').write(dataset.SerializeToString())


print('waiting for kill solvers ...')
sleep(700)

# Stop Random cnf service.
g_stub.StopService(gateway_pb2.TokenMessage(token=random_cnf_service.token))
print('All good?')

with open('script_data.json', 'w') as file:
    print('Clearing data ...')
    json.dump("", file)
