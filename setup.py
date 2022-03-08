from setuptools import setup, find_packages


# with open('.version', 'r') as f:
#     VERSION = f.read()


f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# config_folder = path.expanduser('~') + '/.grepsr'
# if not path.exists(config_folder):
#     mkdir(config_folder)

# if not path.exists(config_folder + '/tmp'):
#     mkdir(config_folder + '/tmp')

# print("\033[95mThankyou for installing gcli\033[0m\n")

setup(
    name='ht_ml',
    install_requires=requirements,
    version='1.0.0',
    description='Parsing Html via ML',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='codera21',
    author_email='ayul.nepal@gmail.com',
    url='https://github.com/codera21/ht_ml/',
    license='unlicensed',
    packages=find_packages(exclude=['tests*']),
    # package_data={'grepsrcli': ['templates/*']},
    include_package_data=True,
    # entry_points="""
    #     [console_scripts]
    #     gcli = grepsrcli.main:main
    # """
)
