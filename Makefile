SCRIPTS := scripts
help: 
	sh $(SCRIPTS)/help.sh

clean:
	sh $(SCRIPTS)/clean.sh
	
PHONY: help clean
