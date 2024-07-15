from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .' #This is used to call the setup.py automatically but we don't want that when are manually reading it from this func


def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements ]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Mercy',
    author_email = 'mercy2049@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)