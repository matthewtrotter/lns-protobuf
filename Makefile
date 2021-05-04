mkfile_abs_path := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
current_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))

proto:
	@echo "Compiling proto files..."
	protoc -I$(mkfile_abs_path) --python_out=$(mkfile_abs_path) lnsalerts.proto
	protoc -I$(mkfile_abs_path) --python_out=$(mkfile_abs_path) lnsalerts2.proto