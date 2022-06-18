
MAKE_FE=$(MAKE) -C frontend
#
# Migration command
#

.PHONY: migration migrate

migration:
	python ./manage.py makemigrations
migrate:
	python ./manage.py migrate

.PHONY: run

run:
	python ./manage.py runserver

.PHONY: run_project
run_project:
	make run
	$(MAKE_FE) run
