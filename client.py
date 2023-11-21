import grpc
import sys

import keyvalue_pb2
import keyvalue_pb2_grpc

def insert_key_value(stub, key, value):
    request = keyvalue_pb2.KeyValueRequest(key=key, value=value)
    response = stub.Insert(request)
    print(response.result)

def consult_value(stub, key):
    request = keyvalue_pb2.KeyRequest(key=key)
    response = stub.Consult(request)
    print(response.value)

def activate_service(stub, address):
    # TODO
    print("Activation not yet implemented")

def terminate_server(stub):
    request = keyvalue_pb2.EmptyRequest()
    response = stub.Terminate(request)
    
    if response.result != 0:
        print("fail to terminate server")
    exit()

def run(address):
    with grpc.insecure_channel(address) as channel:
        stub = keyvalue_pb2_grpc.KeyValueServiceStub(channel)

        for line in sys.stdin:
            tokens = line.strip().split(',')
            if tokens[0] == 'I':
                key = int(tokens[1])
                value = tokens[2]
                insert_key_value(stub, key, value)

            elif tokens[0] == 'C':
                key = int(tokens[1])
                consult_value(stub, key)

            elif tokens[0] == 'A':
                service = tokens[1]
                actvate_service(stub, service)

            elif tokens[0] == 'T':
                terminate_server(stub)
                break

            else:
                continue
                
                # should ignore bad comamnds instead of printing the correct usage
                print("invalid operation") 
                print("================================================") 
                print("valid operations are:")
                print("\tI,int,string\t\t=> associate an integer to a string")
                print("\tC,int\t\t\t=> consult string associated with a int")
                print("\tA,string\t\t=> activate service")
                print("\tT\t\t\t=> terminate pair server")

if __name__ == '__main__':
    address = sys.argv[1]
    run(address)
