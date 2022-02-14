from gateway_pb2_grpcbf import StartService_input
import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2, api_pb2_grpc, threading, json, solvers_dataset_pb2
from time import sleep, time

from main import GATEWAY, MOJITO, RANDOM, FRONTIER, WALL, WALK, generator
from grpcbigbuffer import Dir, client_grpc



g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel('localhost' + ':8090'),
)

print('Get new services....')

c_stub = api_pb2_grpc.SolverStub(
    grpc.insecure_channel('localhost:8081')
    )

print('Tenemos clasificador. ', c_stub)

print('Subiendo solvers al clasificador.')
# Añade solvers.
for s in [FRONTIER, WALL, WALK]:
    print('     ', s)
    next(client_grpc(
        method = c_stub.UploadSolver,
        input = (gateway_pb2.ServiceWithMeta, Dir('__registry__/'+s)),
        indices_parser = api_pb2.Empty
    ))

# Get random cnf
random_cnf_service = next(client_grpc(
    method = g_stub.StartService,
    indices_parser = gateway_pb2.Instance,
    partitions_message_mode_parser=True,
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
        input=dataset,
        indices_parser=api_pb2.Empty
    ))
    print('Dataset añadido.')
except Exception as e:
    print('No tenemos dataset.', str(e))
    pass

print('\nObtiene el data_set.')
dataset = next(client_grpc( # TODO check bug. Iterating requests.
    method=c_stub.GetDataSet,
    input=api_pb2.Empty,
    indices_parser = solvers_dataset_pb2.DataSet,
    partitions_message_mode_parser = True
))
print('\n\DATASET -> ', dataset)
open('dataset.bin', 'wb').write(dataset.SerializeToString())

exit()
if True:#if input("\nGo to train? (y/n)")=='y':
    print('Iniciando entrenamiento...')
    
    # Inicia el entrenamiento.
    next(client_grpc(
        method=c_stub.StartTrain,
        input=api_pb2.Empty(),
        indices_parser = api_pb2.Empty
    ))

    print('Wait to train the model ...')
    for i in range(50): 
        for j in range(10):
            print(' time ', i, j)
            sleep(200)
        
        print('Obtiene el data_set.')
        dataset = next(client_grpc(
            method=c_stub.GetDataSet,
            input=api_pb2.Empty,
            indices_parser=api_pb2.solvers__dataset__pb2.DataSet,
            partitions_message_mode_parser=True
        ))
        print('\n\DATASET -> ', dataset)
        open('dataset.bin', 'wb').write(dataset.SerializeToString())

        cnf = next(client_grpc(
            method = r_stub.RandomCnf,
            indices_parser = api_pb2.Cnf,
            partitions_message_mode_parser = True,
            input = gateway_pb2.Empty()
        ))
        print('cnf -> ', cnf)
        # Comprueba si sabe generar una interpretacion (sin tener ni idea de que tal
        # ha hecho la seleccion del solver.)
        print('\n ---- ', i)
        print(' SOLVING CNF ...')
        t = time()
        try:
            interpretation = next(client_grpc(
                method=c_stub.Solve,
                indices_parser=api_pb2.Interpretation,
                partitions_message_mode_parser=True,
                input=cnf,
                indices_serializer=api_pb2.Cnf
            ))
            print(interpretation, str(time()-t)+' OKAY THE INTERPRETATION WAS ')
        except StopIteration: print('tensor is not ready yet.')

    sleep(60)

print('Termina el entrenamiento')
# En caso de que estubiera entrenando lo finaliza.
next(client_grpc(
    method=c_stub.StopTrain,
    input=api_pb2.Empty,
    indices_parser=api_pb2.Empty
))

# Comprueba si sabe generar una interpretacion (sin tener ni idea de que tal
# ha hecho la seleccion del solver.)
def final_test(c_stub, r_stub, i, j):
    cnf = next(client_grpc(
        method=r_stub.RandomCnf,
        input=api_pb2.Empty,
        indices_parser=api_pb2.Cnf,
        partitions_message_mode_parser=True
    ))
    t = time()
    interpretation = next(client_grpc(
        method=c_stub.Solve,
        input=cnf,
        indices_parser=api_pb2.Interpretation,
        partitions_message_mode_parser=True
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
    indices_parser=api_pb2.solvers__dataset__pb2.DataSet,
    partitions_message_mode_parser=True
))
print('\n\DATASET -> ', dataset)
open('dataset.bin', 'wb').write(dataset.SerializeToString())


print('waiting for kill solvers ...')
sleep(700)

# Stop Random cnf service.
next(client_grpc(
    method=g_stub.StopService,
    input=gateway_pb2.TokenMessage(token=random_cnf_service.token),
    indices_parser=api_pb2.Empty
))
print('All good?')

with open('script_data.json', 'w') as file:
    print('Clearing data ...')
    json.dump("", file)
