test:
	pytest -v

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing

dev:
	gulp --cwd vote/staticapp/

database:
	dropdb vote --if-exists
	createdb vote
