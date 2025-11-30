'''
The setup.py file is essential for packaging Python projects.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    returns list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except:
        print("requirements.txt not found")
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Ali Elbeyali",
    author_email = "alielbeyali123@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)