from setuptools import setup, find_packages

setup(
    name='ht_ml',
    # install_requires=requirements,
    version='1.0.0',
    description='Parsing HTML using ML',
    # long_description=LONG_DESCRIPTION,
    # long_description_content_type='text/markdown',
    author='atul n',
    author_email='atul.nepal@gmail.com',
    url='',
    license='unlicensed',
    packages=find_packages(exclude=['tests*']),
    # package_data={'grepsrcli': ['templates/*']},
    # include_package_data=True,
    entry_points="""
        [console_scripts]
        ht_ml = ht_ml.main:main
    """
)