import codecs
import os
import setuptools
import re


HERE = os.path.abspath(os.path.dirname(__file__))
META_PATH = os.path.join("pytidy", "__init__.py")


with open("README.md", "r") as fh:
    long_description = fh.read()


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta: str) -> str:
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


setuptools.setup(
    name=find_meta("title"),
    version=find_meta("version"),
    author=find_meta("author"),
    author_email=find_meta("email"),
    description=find_meta("description"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/taxpon/pytidy",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)