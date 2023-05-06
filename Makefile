
.PHONY: compile

# Compile dependencies from setup.cfg and write them to requirements.txt
compile:
	@pip install pip-tools
	@pip-compile --upgrade -o requirements.txt --resolver backtracking pyproject.toml

# Build the python packages
build:
	@python -m build


# Install all requirements and keep pip up to date
install:
	@pip install -U pip
	@pip install --no-deps -r requirements.txt
