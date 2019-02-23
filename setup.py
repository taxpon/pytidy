import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytidy",
    version="0.1.0",
    author="Takuro Wada",
    author_email="taxpon@gmail.com",
    description="Dependency Injection library based on type hints",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/taxpon/pytidy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)