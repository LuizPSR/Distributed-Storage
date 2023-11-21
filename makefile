

prereq:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. keyvalue.proto

clean:
	rm -r keyvalue_pb2.py keyvalue_pb2_grpc.py __pycache__