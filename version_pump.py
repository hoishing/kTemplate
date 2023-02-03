#!/usr/bin/env python3

import toml
import argparse
from subprocess import getoutput

data = toml.load("pyproject.toml")
version = data["tool"]["poetry"]["version"]

major, minor, patch = map(int, version.split("."))

parser = argparse.ArgumentParser(description="Pump Version")
parser.add_argument("to_pump", type=str, help="major, minor, patch")
args = parser.parse_args()

locals()[args.to_pump] += 1

new_version = f"{major}.{minor}.{patch}"
data["tool"]["poetry"]["version"] = new_version

# update pyproject.toml
with open("pyproject.toml", "w") as f:
    toml.dump(data, f)


# update github tag
getoutput(f"git tag {new_version} && git push --tag")


# publish to pypi, update github release and commit changelog
getoutput("./publish.sh")
