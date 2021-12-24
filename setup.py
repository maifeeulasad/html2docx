from setuptools import setup
from setuptools import find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="htmldocx",
    version="0.0.7",
    description="Convert html to docx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pqzx/html2docx",
    author="pqzx",
    author_email="pqzx@github.com",
    license="MIT",
    packages=find_packages(),
    zip_safe=False,
    install_requires=[],
)
