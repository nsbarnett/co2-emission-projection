# RELEVENT FOR LINUX/MAC SYSTEMS ONLY TO USE:
# 'make install'
# 'make lint'
# 'make format'
# 'make type-check'
# 'make test'

# FOR WINDOWS USE:
# 'pip install -r requirements.txt'
# 'ruff check .'
# 'black src tests'
# 'mypy src'
# 'pytest -q'


.PHONY: install lint format type-check test

# Install dependencies
install:
	pip install -r requirements.txt

# Run Ruff (linting)
lint:
	ruff check .

# Auto-format code with Black
format:
	black src tests

# Run type checks with mypy
type-check:
	mypy src

# Run tests with pytest
test:
	pytest -q
