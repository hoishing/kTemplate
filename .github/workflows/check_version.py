from pathlib import Path
import requests, os, toml
from packaging.version import parse

# get version from pyproject.toml
pyproject = toml.load("pyproject.toml")
pyproject_version = pyproject["tool"]["poetry"]["version"]
repo = pyproject["tool"]["poetry"]["repository"]
repo_name = Path(repo).name

# retrive the latest release version from the GitHub API
response = requests.get(
    f"https://api.github.com/repos/hoishing/{repo_name}/releases/latest"
)

# parse the response
data = response.json()
release_version = Path(data["html_url"]).name

if parse(pyproject_version) > parse(release_version):
    output_file = os.getenv("GITHUB_OUTPUT")

    with open(output_file, "a") as op:
        op.write(f"new_version={pyproject_version}\n")
