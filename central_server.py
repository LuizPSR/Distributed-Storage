import grpc
import sys
from concurrent import futures

import keyvalue_pb2
import keyvalue_pb2_grpc

import centralstorage_pb2
import centralstorage_pb2_grpc

class CentralStorageServicer(centralstorage_pb2_grpc.CentralStorageServiceServicer):
    def __init__(self):
        self.key_host_storage = {}

    def Register(self, request, context):
        host = request.host

        keys = list(request.keys)

        for k in keys:
            # overwrite all entries, inclueding self
            self.key_host_storage[k] = host

        return centralstorage_pb2.ConfirmationResponse(result=len(keys))

    def Map(self, request, context):
        key = request.key
        host = self.key_host_storage.get(key, "")
        return centralstorage_pb2.HostResponse(host=host)
    
    def Terminate(self, request, context):
        server.stop(0)
        return centralstorage_pb2.ConfirmationResponse(result=0)

def serve(port):
    centralstorage_pb2_grpc.add_CentralStorageServiceServicer_to_server(CentralStorageServicer(), server)
    server.add_insecure_port("localhost:" + port)
    server.start()
    server.wait_for_termination()

# make the server a global
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) 
if __name__ == '__main__':
    port = sys.argv[1]
    serve(port)
