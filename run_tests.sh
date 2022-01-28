pytest -v --junitxml=test_report.xml --cov-report xml --cov  confite
coverage report -m
coverage xml -i
coverage html