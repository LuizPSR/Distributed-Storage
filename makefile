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

clean:
	rm -r __pycache__