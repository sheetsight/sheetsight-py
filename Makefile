.PHONY: install dev-install test lint format build clean

# Install package in development mode
install:
	pip install -e .

# Install with development dependencies
dev-install:
	pip install -e ".[dev]"

# Run tests
test:
	pytest tests/ -v

# Run tests with coverage
test-cov:
	pytest tests/ -v --cov=sheetsight_py --cov-report=html --cov-report=term

# Lint code
lint:
	flake8 sheetsight_py/ examples/
	mypy sheetsight_py/

# Format code
format:
	black sheetsight_py/ examples/
	isort sheetsight_py/ examples/

# Build package
build: clean
	python -m build

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

# Run example
example:
	python examples/basic_usage.py


