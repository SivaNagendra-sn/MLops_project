from setuptools import find_packages, setup
from typing import List

def get_requirements(filename:str)->List['str']:
    '''
    This function will retrun the list of requiremnts
    '''
    requirements = []
    with open(filename, 'r') as f:
       libs =  f.readlines()
       requirements = [lib.replace("\n", "") for lib in libs ]
    
    if '-e .' in requirements:
        requirements.remove('-e .')

    return requirements

setup(
name='mlproject_mlops',
version='0.0.1',
author='Siva Nagendra',
author_email='sivanagendra.paruchuri@gmail.com',
package = find_packages(),  # searches for__init__.py in all folders
install_requires=get_requirements('requirements.txt')
)