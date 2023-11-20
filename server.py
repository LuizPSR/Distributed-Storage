import grpc
import sys
from concurrent import futures

import keyvalue_pb2
import keyvalue_pb2_grpc

class KeyValueServicer(keyvalue_pb2_grpc.KeyValueServiceServicer):
    def __init__(self):
        self.key_value_storage = {}

    def Insert(self, request, context):
        key = request.key
        value = request.value

        # check if key already in use
        if key in self.key_value_storage:
            return keyvalue_pb2.KeyValueResponse(result=-1)
        
        self.key_value_storage[key] = value
        return keyvalue_pb2.KeyValueResponse(result=0)

    def Consult(self, request, context):
        key = request.key
        value = self.key_value_storage.get(key, "")
        return keyvalue_pb2.ValueResponse(value=value)
    
    def Activate(self, request, context):
        service = request.address
        # TODO 
        return keyvalue_pb2.EmptyResponse()
    
    def Terminate(self, request, context):
        self.server.stop(0)
        return keyvalue_pb2.EmptyResponse()

def serve(port):

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    keyvalue_pb2_grpc.add_KeyValueServiceServicer_to_server(KeyValueServicer(), server)
    
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    
    if sys.argc > 2:
        print("Central server not yet implemented")
        exit()

    else:
        port = int(sys.argv[1])
        serve(port)
