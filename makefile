run_serv_pares_1:
	python server.py $(arg)
run_serv_pares_2:
	python server.py $(arg) anything
run_cli_pares:
	python client.py $(arg)

run_serv_central:
	python central_server.py $(arg)
run_cli_central:
	python central_client.py $(arg)

protobuffers:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. keyvalue.proto
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. centralstorage.proto

clean:
	rm -r __pycache__