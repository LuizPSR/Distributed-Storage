run_serv_pares_1: prereq
	python server.py $(arg)
run_serv_pares_2: prereq
	python server.py $(arg) any_extra_arg
run_cli_pares: prereq
	python client.py $(arg)

run_serv_central: prereq
	python central_server.py $(arg)
run_cli_central: prereq
	python central_client.py $(arg)

prereq:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. keyvalue.proto
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. centralstorage.proto

clean:
	rm -r __pycache__