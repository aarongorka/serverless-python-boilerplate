ifdef GO_PIPELINE_NAME
	USER_SETTINGS=--user 0:0
else
	ifeq ($(shell uname -s),Linux)
		USER_SETTINGS=--user $(shell id -u):$(shell id -g)
	endif
endif

################
# Entry Points #
################
test: clone recursive

clone:
	docker-compose run $(USER_SETTINGS) --rm cookiecutter --no-input --overwrite-if-exists . project_name='Python Test Project'
	$(MAKE) -C python-test-project .env

recursive:
	$(MAKE) -C python-test-project deps build styleTest run #deploy smokeTest remove

_clean:
	rm -fr python-test-project
