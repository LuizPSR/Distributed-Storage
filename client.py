import grpc
import sys

import keyvalue_pb2
import keyvalue_pb2_grpc

def insert_key_value(stub, key, value):
    request = keyvalue_pb2.KeyValueRequest(key=key, value=value)
    response = stub.Insert(request)
    print(response.message)

def consult_value(stub, key):
    request = keyvalue_pb2.KeyRequest(key=key)
    response = stub.Consult(request)

    print("The value for key {key} is: {response.value}")

def activate_service(stub, address):
    # TODO
    
    print("Activation not yet implemented")

def teminate_server(stub):
    request = keyvalue_pb2.EmptyRequest()
    response = stub.Terminate(request)

    print("Server terminated")
    print("Exiting program")
    exit()

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = keyvalue_pb2_grpc.KeyValueServiceStub(channel)

    for line in sys.stdin:
        tokens = line.split(',')
        
        if tokens[0] == 'I':
            key = int(tokens[1])
            value = tokens[2]
            insert_key_value(stub, key, value)

        elif tokens[0] == 'C':
            key = int(tokens[i])
            consult_value(stub, key)

        elif tokens[0] == 'A':
            service = tokens[1]
            actvate_service(stub, service)

        elif tokens[0] == 'T':
            terminate_server(stub)
            break

        else:
            print("invalid operation") 

if __name__ == '__main__':
    run()
