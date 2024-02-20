from setuptools import find_packages, setup
from typing import List

'''
Setup.py is the main file which contains the meta data about the project and also is
responsible for building all the packages in the project..
'''
'''
We can directly install setup.py which intern installs all the packages and 
requirements or just add a '-e .' in requirements.txt so while installing 
requirements.txt setup.py will also be installed!!
'''
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function returns the libraries to be installed in the form
    of List given the path of requirements.txt
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
     
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'UDB',
    author_email= 'udyanrajebhosale@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)