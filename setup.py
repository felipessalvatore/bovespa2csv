from setuptools import setup, find_packages

setup(
    name='bovespa2csv',
    version='0.1',
    description='code to parse Bovespa data',
    author='Felipe Salvatore',
    packages=find_packages(),
    test_suite="tests"
)
