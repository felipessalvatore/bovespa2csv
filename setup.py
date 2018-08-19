from setuptools import setup, find_packages

setup(
    name='bovespa2csv',
    version='0.1',
    description='Code to parse Bovespa data into a csv or excel',
    author='Felipe Salvatore',
    author_email='felipessalvador@gmail.com',
    packages=find_packages(exclude=('tests')),
    install_requires=['pandas>=0.22.0', 'XlsxWriter>=1.0.7'],
    license='MIT',
    test_suite="tests"
)
