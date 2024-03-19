import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"

list_of_file = [
	".github/workflows/.gitkeep",
	f"src/{project_name}/__init__.py",
	f"src/{project_name}/components/__init__.py",
	f"src/{project_name}/utils/__init__.py",
	f"src/{project_name}/config/__init__.py",
	f"src/{project_name}/config/configuration.py",
	f"src/{project_name}/pipeline/__init__.py",
	f"src/{project_name}/entity/__init__.py",
	f"src/{project_name}/constants/__init__.py",
	"config/config.yaml",
	"dvc.yaml",
	"param.yaml",
	"requirements.txt",
	"setup.py",
	"research/trails.ipynb",
	"templates/index.html"
]


def create_file(filepath):
	if not filepath.exists() or filepath.stat().st_size == 0:
		filepath.touch()
		logging.info(f"Created empty file: {filepath}")
	else:
		logging.info(f"{filepath.name} already exists")


def create_directory(directory):
	directory.mkdir(parents=True, exist_ok=True)
	logging.info(f"Created directory: {directory}")


for item in list_of_file:
	path = Path(item)
	if path.is_dir():
		create_directory(path)
	elif path.is_file():
		create_file(path)
	else:
		logging.warning(f"Illegal path: {path}")
