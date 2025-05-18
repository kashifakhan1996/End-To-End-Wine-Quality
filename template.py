import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name = "mlProject"
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "params.yaml",
    "config/config.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.py",
    "templates/index.html"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    fildir,filename = os.path.split(file_path)

    if fildir != "":
        os.makedirs(fildir,exist_ok=True)
        logging.info(f'creating directory {fildir}: for the file: {filename}')

    if(not os.path.exists(file_path) or os.path.getsize(file_path) is 0):
        with open(file_path,"w") as f:
            pass
            logging.info(f'creating empty file {file_path}')
    else:
        logging.info(f' file {filename} already exist')