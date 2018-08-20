from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='bovespa2csv',
    version='0.0.2',
    description='Parser for Bovespa data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Felipe Salvatore',
    author_email='felipessalvador@gmail.com',
    packages=find_packages(),
    license='MIT',
    test_suite="tests",
    url="https://github.com/felipessalvatore/bovespa2csv",
    keywords=["bovespa", "parser" "csv", "excel"],
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
