import grpc
import sys
import socket
from concurrent import futures

import keyvalue_pb2
import keyvalue_pb2_grpc

import central_pb2
import central_pb2_grpc

#========================================================================================#
#=================================== Logic ==============================================#
#========================================================================================#

class KeyValueServicer(keyvalue_pb2_grpc.KeyValueServiceServicer):
    def __init__(self):
        self.key_value_storage = {}

    def Insert(self, request, context):
        key = request.key
        value = request.value

        # check if key already in use
        if key in self.key_value_storage:
            return keyvalue_pb2.ConfirmationResponse(result=-1)
        
        self.key_value_storage[key] = value
        return keyvalue_pb2.ConfirmationResponse(result=0)

    def Consult(self, request, context):
        key = request.key
        value = self.key_value_storage.get(key, "")
        return keyvalue_pb2.ValueResponse(value=value)
    
    def Activate(self, request, context):
        # default return
        keys = -1

        if CENTRAL_STORAGE_SERVER_FLAG:
            host = request.host
            with grpc.insecure_channel(host) as channel:
                central_stub = centralstorage_pb2_grpc.CentralStorageServiceStub(channel)
                
                self_host = socket.getfqdn()
                request = centralstorage_pb2.RegisterRequest(host=self_host, keys=key_value_storage.keys)
                response = central_stub.Consult(request)
                keys = response.result

        return keyvalue_pb2.ConfirmationResponse(result=keys)
    
    def Terminate(self, request, context):
        server.stop(0)
        return keyvalue_pb2.ConfirmationResponse(result=0)

def serve(port):
    keyvalue_pb2_grpc.add_KeyValueServiceServicer_to_server(KeyValueServicer(), server)
    server.add_insecure_port("localhost:" + port)
    server.start()
    server.wait_for_termination()

#========================================================================================#
#===================================== Main =============================================#
#========================================================================================#

# make the server a global
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) 
# implemented Activation as a feature flag
CENTRAL_STORAGE_SERVER_FLAG = False

if __name__ == '__main__':
    
    if len(sys.argv) > 2:
        CENTRAL_STORAGE_SERVER_FLAG = True

    else:
        port = sys.argv[1]
        serve(port)
