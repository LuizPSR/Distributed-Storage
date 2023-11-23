import grpc
import sys
import socket

import keyvalue_pb2
import keyvalue_pb2_grpc

import centralstorage_pb2
import centralstorage_pb2_grpc

def map_value(stub, key):
    request = centralstorage_pb2.KeyRequest(key=key)
    response = stub.Map(request)

    host = response.host 
    port = response.port
    if host != "":
        with grpc.insecure_channel(host + ':' + port) as channel:
            host_stub = keyvalue_pb2_grpc.KeyValueServiceStub(channel)
            request = keyvalue_pb2.KeyRequest(key=key)
            response = host_stub.Consult(request)

            value = response.value
            print(host+':'+port, ':', value)

    # no print if key is not registered

def terminate_server(stub):
    request = centralstorage_pb2.EmptyRequest()
    response = stub.Terminate(request)
    
    if response.result != 0:
        print("fail to terminate central server")
    exit()

def run(address):
    with grpc.insecure_channel(address) as channel:
        stub = centralstorage_pb2_grpc.CentralStorageServiceStub(channel)

        for line in sys.stdin:
            tokens = line.strip().split(',')
            if tokens[0] == 'C' and len(tokens) == 2:
                key = int(tokens[1])
                map_value(stub, key)

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
