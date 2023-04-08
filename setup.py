from setuptools import find_packages,setup
from typing import List

def get_req(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','')for req in requirements]
setup(
    name="Rproject",
    version="0.0.1",
    author="Dhruv",
    author_email="heydhruvdave@gmail.com",
    install_reqires=get_req('requirements.txt'),
    packages=find_packages()

)