from setuptools import setup, find_packages

setup(
    name='bovespa2csv',
    version='0.1',
    description='Parser for Bovespa data',
    author='Felipe Salvatore',
    author_email='felipessalvador@gmail.com',
    packages=find_packages(exclude=('tests')),
    install_requires=['pandas>=0.22.0', 'XlsxWriter>=1.0.7'],
    license='MIT',
    test_suite="tests",
    url="https://github.com/felipessalvatore/bovespa2csv",
    keywords=["bovespa", "parser" "csv", "excel"]
)
