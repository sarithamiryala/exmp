import os
from  pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s: ')

package_name = "deepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/_init__.py",
    f"src/{package_name}/components/_init__.py",
    f"src/{package_name}/utils/_init__.py",
    f"src/{package_name}/config/_init__.py",
    f"src/{package_name}/pipeline/_init__.py",
    f"src/{package_name}/entity/_init__.py",
    f"src/{package_name}/components/_init__.py",
    f"src/{package_name}/constants/_init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py"
    "configs/config.yaml",
    "dvc.yaml", #data versioning
    "params.yaml",
    "init_setup.sh", #creates enviroments
    "requirements.txt",
    "requirements_dev.txt", #devlopment related requirements
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb"


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath) 
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating directory: {filedir} for file: {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass 
            logging.info(f'creating empty file: {filepath}')

    else:
        logging.info(f"{filename} already exists")