import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0.0"
Repo_Name = "cnnClassifier"
Author_Name = "Theory903"
SRC_REPO = "cnnClassifier"
Author_Email = "abhijha903@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=Author_Name,
    author_email=Author_Email,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{Author_Name}/{Repo_Name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Author_Name}/{Repo_Name}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
