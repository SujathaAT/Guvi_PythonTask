To run
Execute command
pip install pytest-playwright
playwright install
pytest --browser-channel chrome --headed tests/test_guvi.py

$env:PYTHONPATH = "."
pytest --browser-channel chrome --headed tests/test_guvi.py

pytest --browser-channel chrome --html=reports/report.html --self-contained-html