test:
	python -m unittest test_staging_project test_staged_request

autopep8:
	autopep8 --in-place --aggressive --aggressive *.py