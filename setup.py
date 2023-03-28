from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sessender",
    version="0.3",
    author="Amit Dalal",
    author_email="amit+pypi@serverlessguy.com",
    description="A Python package for sending emails using AWS SES",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/sessender",
    packages=['sessender'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
