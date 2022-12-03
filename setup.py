from setuptools import find_packages,setup
from typing import List

REQ_FILE_NAME = "requirements.txt"
edot = "-e ."

def get_requirements() -> List[str]:
    with open(REQ_FILE_NAME) as f:
        req_list = f.readlines()
    req_list = [req_name.replace("\n","") for req_name in req_list]

    if edot in req_list:
        req_list.remove(edot)
    return req_list

setup(
    name="sensor",
    version="0.0.1",
    author="Atharv Kulkarni",
    author_email="atharv4study@gmail.com",
    packages=find_packages(),
    install_requirments= get_requirements(),
)