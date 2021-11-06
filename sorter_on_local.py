from gateway_pb2_grpcbf import StartService_input
import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2, api_pb2_grpc, threading, json, solvers_dataset_pb2
from time import sleep, time

from main import GATEWAY, RANDOM, FRONTIER, WALL, WALK, client_grpc, generator



g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel(GATEWAY + ':8080'),
)

print('Get new services....')

c_stub = api_pb2_grpc.SolverStub(
    grpc.insecure_channel('localhost:8080')
    )

print('Tenemos clasificador. ', c_stub)

# Get random cnf
random_cnf_service = next(client_grpc(
    method = g_stub.StartService,
    output_field = gateway_pb2.Instance,
    input = generator(hash = RANDOM),
    indices_serializer = StartService_input
))

print(random_cnf_service)
uri=random_cnf_service.instance.uri_slot[0].uri[0]
r_uri = uri.ip +':'+ str(uri.port)
r_stub = api_pb2_grpc.RandomStub(
    grpc.insecure_channel(r_uri)
    )

print('Tenemos random. ', r_stub)

#sleep(10) # Espera a que el servidor se levante.

try:
    dataset = solvers_dataset_pb2.DataSet()
    dataset.ParseFromString(open('dataset.bin', 'rb').read())
    next(client_grpc(
        method=c_stub.AddDataSet,
        input=dataset
    ))
    print('Dataset añadido.')
except Exception as e:
    print('No tenemos dataset.')
    pass

if True:#if input("\nGo to train? (y/n)")=='y':
    print('Iniciando entrenamiento...')
    # Inicia el entrenamiento.
    next(client_grpc(
        method=c_stub.StartTrain,
        input=api_pb2.Empty()
    ))

    print('Subiendo solvers al clasificador.')
    # Añade solvers.
    for s in [FRONTIER, WALL, WALK]:
        print('     ', s)
        next(client_grpc(
            method = c_stub.UploadSolver,
            input = ('__registry__/'+s, gateway_pb2.celaut__pb2.Any) # TODO
        ))


    print('Wait to train the model ...')
    for i in range(50): 
        for j in range(10):
            print(' time ', i, j)
            sleep(200)
        
        cnf = next(client_grpc(
            method=r_stub.RandomCnf,
            input=api_pb2.Empty(),
            output_field=api_pb2.Cnf
        ))
        # Comprueba si sabe generar una interpretacion (sin tener ni idea de que tal
        # ha hecho la seleccion del solver.)
        print('\n ---- ', i)
        print(' SOLVING CNF ...')
        t = time()
        interpretation = next(client_grpc(
            method=c_stub.Solve,
            output_field=api_pb2.Interpretation,
            input=cnf
        ))
        print(interpretation, str(time()-t)+' OKAY THE INTERPRETATION WAS ')

    sleep(60)

print('Termina el entrenamiento')
# En caso de que estubiera entrenando lo finaliza.
next(client_grpc(
    method=c_stub.StopTrain,
    input=api_pb2.Empty
))

# Comprueba si sabe generar una interpretacion (sin tener ni idea de que tal
# ha hecho la seleccion del solver.)
def final_test(c_stub, r_stub, i, j):
    cnf = next(client_grpc(
        method=r_stub.RandomCnf,
        input=api_pb2.Empty,
        output_field=api_pb2.Cnf
    ))
    t = time()
    interpretation = next(client_grpc(
        method=c_stub.Solve,
        input=cnf,
        output_field=api_pb2.Interpretation
    ))
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
dataset = next(client_grpc(
    method=c_stub.GetDataSet,
    input=api_pb2.Empty,
    output_field=api_pb2.solvers__dataset__pb2.DataSet
))
print('\n\DATASET -> ', dataset)
open('dataset.bin', 'wb').write(dataset.SerializeToString())


print('waiting for kill solvers ...')
sleep(700)

# Stop Random cnf service.
next(client_grpc(
    method=g_stub.StopService,
    input=gateway_pb2.TokenMessage(token=random_cnf_service.token)
))
print('All good?')

with open('script_data.json', 'w') as file:
    print('Clearing data ...')
    json.dump("", file)
