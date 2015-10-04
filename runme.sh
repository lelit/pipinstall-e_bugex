python3 -m venv plain
python3 -m venv edit

plain/bin/pip install .
plain/bin/python -c "import bugex.foo"

edit/bin/pip install -e .
edit/bin/python -c "import bugex.foo"
