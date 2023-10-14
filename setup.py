import setuptools
import os
with open('README.md') as file:
    read_me_discription = file.read()

if __name__ == '__main__':
    setuptools.setup(name = 'test_package_group_10_00', 
                     version = '0.1', 
                     description = 'This test package help with work sqlite',
                     long_description = read_me_discription,
                     url = '')