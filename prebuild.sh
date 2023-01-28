# run test with coverage report
coverage run -m pytest --doctest-modules
coverage report

# create html report for docs
coverage html -d docs/assets/coverage
rm docs/assets/coverage/.gitignore

# create coverage badge
coverage xml -o docs/assets/coverage-report.xml # not use `coverage.xml` to avoid ignore
genbadge coverage -i docs/assets/coverage-report.xml -o docs/assets/coverage-badge.svg

# update changelog
auto-changelog
[ -x "$(command -v prettier)" ] && prettier -w CHANGELOG.md
