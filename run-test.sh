coverage run -m pytest --doctest-modules
coverage report

# create html report for docs
coverage html -d docs/assets/coverage
rm docs/assets/coverage/.gitignore

# not use default `coverage.xml` to avoid ignore
coverage xml -o docs/assets/coverage-report.xml
genbadge coverage -i docs/assets/coverage-report.xml -o docs/assets/coverage-badge.svg
