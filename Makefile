SCRIPTS := scripts
help: 
	sh $(SCRIPTS)/help.sh

clean:
	sh $(SCRIPTS)/clean.sh

test:
	sh $(SCRIPTS)/test.sh

install:
	sh $(SCRIPTS)/install.sh
	
build:
	sh $(SCRIPTS)/build.sh

publish:
	uv publish
PHONY: help clean test install typecheck build publish
