test:
	python -m unittest test_staging_project test_staged_request test_excluded_request

autopep8:
	autopep8 --in-place --aggressive --aggressive *.py

clean:
	rm *.pyc
