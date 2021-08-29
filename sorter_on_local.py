import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2, api_pb2_grpc, threading, json, sys
from time import sleep, time

RANDOM = '2d90e2f2809eb085f3983cc81fb345047ed31d1ae4e2af9fadf3cc7a1a2f8ad7'
FRONTIER = 'ff5cd81386be3a547d9cba7799010f662e43a57c3cb78f074ee5b8d01100e08e'
WALK = '228fbdf8d636032535dbd81dd5a653b4e3a40c4bb43ea1f37d18b83f053d2833'
WALL = '28fc5ea20bbd9d1d7c5ba40614bab7c21202edf3911a3afe12cb054c42820bac'

SHA3_256 = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

WHISKY = '192.168.1.114'
MOJITO = '192.168.1.143'
GATEWAY = MOJITO

def generator(hash: str):
    transport = gateway_pb2.ServiceTransport()
    transport.hash.type = bytes.fromhex(SHA3_256)
    transport.hash.value = bytes.fromhex(hash)
    transport.config.CopyFrom(gateway_pb2.ipss__pb2.Configuration())
    yield transport



g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel(GATEWAY + ':8080')
)

print('Get new services....')

c_stub = api_pb2_grpc.SolverStub(
    grpc.insecure_channel('localhost:8080')
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
    for i in range(1): 
        for j in range(10):
            print(' time ', i, j)
            sleep(60)
        
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
sleep(200)

# Stop Random cnf service.
g_stub.StopService(random_cnf_service.token)
print('All good?')

with open('script_data.json', 'w') as file:
    print('Clearing data ...')
    json.dump("", file)
