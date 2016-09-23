run:
	python django/./manage.py runserver 0.0.0.0:8080 --settings=mathias.settings.development

test:
	coverage run --branch --source=django/mathias  django/./manage.py test django/mathias/ -v 2 --failfast --settings=mathias.settings.test
	coverage report --omit=django/mathias/*/migrations*,django/mathias/settings/*,django/mathias/urls.py,django/mathias/wsgi.py,django/manage.py,django/mathias/*/tests/*,django/poc/__init__.py

html:
	coverage html --omit=django/mathias/*/migrations*,django/mathias/settings/*,django/mathias/urls.py,django/mathias/wsgi.py,django/manage.py,django/mathias/*/tests/*,django/poc/__init__.py
	open htmlcov/index.html

doc:
	$(MAKE) -C docs/ html
	open docs/build/html/index.html

clean:
	rm -f .coverage
	rm -rf htmlcov/
	rm -rf docs/build/

migrate:
	python django/./manage.py migrate --settings=mathias.settings.development

makemigrate:
	python django/./manage.py makemigrations --settings=mathias.settings.development

superuser:
	python django/./manage.py createsuperuser --settings=mathias.settings.development

requirements-development:
	@pip install -r django/requirements/development.txt
