code-dir = async_tensorart
examples-dir = examples
test-dir = tests

.PHONY lint:
lint:
	@echo "Running black..."
	@poetry run black --config pyproject.toml --check --diff $(code-dir) $(examples-dir) $(test-dir)

	@echo "Running ruff..."
	@poetry run ruff check --config pyproject.toml --diff $(code-dir) $(examples-dir) $(test-dir)

	@echo "Running MyPy..."
	@poetry run mypy --config-file pyproject.toml async_tensorart

.PHONY format:
format:
	@echo "Running black..."
	@poetry run black --config pyproject.toml $(code-dir) $(examples-dir) $(test-dir)

	@echo "Running ruff check with --fix..."
	@poetry run ruff check --config pyproject.toml --fix --unsafe-fixes $(code_dir) $(examples-dir) $(tests_dir)

	@echo "Running ruff..."
	@poetry run ruff format --config pyproject.toml $(code_dir) $(examples-dir) $(test-dir)

.PHONY test:
test:
	@echo "Running tests..."
	@poetry run pytest -v --config-file=pyproject.toml

.PHONY poetry-show:
poetry-show:
	@poetry show --top-level --latest

.PHONY poetry-show-outdated:
poetry-show-outdated:
	@poetry show --top-level --outdated
