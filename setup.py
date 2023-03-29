from setuptools import setup
import os
with open("README.md", "r") as fh:
    long_description = fh.read()



# Extract tag name from GITHUB_REF environment variable
tag = os.environ['GITHUB_REF'].split('/')[-1]
if tag.startswith('v'):
    version = tag[1:]
else:
    version = tag

setup(
    name="sessender",
    version=version,
    author="Amit Dalal",
    description="A Python package for sending emails using AWS SES",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amitsdalal/sessender",
    py_modules=['sessender'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
