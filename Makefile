code-dir = async_tensorart
examples-dir = examples
test-dir = tests

.PHONY lint:
lint:
	@echo "Running black..."
	@black --config pyproject.toml --check --diff $(code-dir) $(examples-dir) $(test-dir)

	@echo "Running ruff..."
	@ruff --config pyproject.toml $(code-dir) $(examples-dir) $(test-dir)

	@echo "Running MyPy..."
	@mypy --config-file pyproject.toml async_tensorart

.PHONY format:
format:
	@echo "Running black..."
	@black --config pyproject.toml $(code-dir) $(examples-dir) $(test-dir)

	@echo "Running ruff..."
	@ruff --config pyproject.toml --fix $(code-dir) $(examples-dir) $(test-dir)


.PHONY test:
test:
	@echo "Running tests..."
	@pytest -v --config-file=pyproject.toml
