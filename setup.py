# In Python, setup.py is a module used to build and distribute Python packages. It typically contains information 
# about the package, such as its name, version, and dependencies, as well as instructions for building and installing the package.
'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''
# (d:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\venv) 
# D:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines>pip install -r requirements.txt

# It built the model in mlopsproject.egg-info

from setuptools import find_packages,setup # type:ignore

def get_requirements():
    try:
        with open('requirements.txt','r') as file:
            requirements = file.readlines()
            requirements_lst = [i.replace("\n", "") for i in requirements]
            if "-e ." in requirements_lst:
                requirements_lst.remove("-e .")
    except FileNotFoundError:
        print("Requirements.txt file not found")

    return requirements_lst

# parameters of setup
setup(name='networksecurityprojectpackage',
version='0.0.1',
author='Anwesha',
author_email='anwesha.bose2021@gmail.com',
packages=find_packages(), # initializing the module find_packages # where is the parameter of find_packages
install_requires=get_requirements())