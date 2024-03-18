import setuptools

with open("README.md", "r", encoding="utf=-8") as f:
	long_description = f.read()

__version__ = "0.0.0.0"
Repo_Name = "Chicken-Disease-Classification"
Author_Name = "Theory903"
SRC_REPO = "cnnClassifier"
Author_Email = "abhijha903@gmail.com"

setuptools.setup(
	name=Repo_Name,
	version=__version__,
	author=Author_Name,
	author_email=Author_Email,
	description="A small Python package for CNN classifier",
	Long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Theory903/Chicken-Disease-Classification",
	project_urls={
		"Bug Tracker": f"https://github.com/Theory903/Chicken-Disease-Classification/issues"
	},
	package_dir={"": "src"},
	packages=setuptools.find_packages(where="src")
)
