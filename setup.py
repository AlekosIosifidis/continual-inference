#!/usr/bin/env python

from setuptools import find_packages, setup


def long_description():
    text = open("README.md", encoding="utf-8").read()
    # SVG images are not readable on PyPI, so replace them  with PNG
    text = text.replace(".svg", ".png")
    return text


def from_file(file_name: str = "requirements.txt", comment_char: str = "#"):
    """Load requirements from a file"""
    with open(file_name, "r") as file:
        lines = [ln.strip() for ln in file.readlines()]
    reqs = []
    for ln in lines:
        # filer all comments
        if comment_char in ln:
            ln = ln[: ln.index(comment_char)].strip()
        # skip directly installed dependencies
        if ln.startswith("http"):
            continue
        if ln:  # if requirement is not empty
            reqs.append(ln)
    return reqs


setup(
    name="continual-inference",
    version="0.2.0",
    description="Building blocks for Continual Inference Networks in PyTorch",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    author="Lukas Hedegaard",
    author_email="lukasxhedegaard@gmail.com",
    url="https://github.com/LukasHedegaard/continual-inference",
    install_requires=from_file("requirements.txt"),
    extras_require={
        "build": from_file("requirements/build.txt"),
        "dev": from_file("requirements/dev.txt"),
        "docs": from_file("requirements/docs.txt"),
    },
    packages=find_packages(exclude=["tests", "docs", "figures", "requirements"]),
    keywords=["deep learning", "pytorch", "AI", "online", "inference", "continual"],
    classifiers=[
        "Environment :: Console",
        "Natural Language :: English",
        # How mature is this project? Common values are
        #   3 - Alpha, 4 - Beta, 5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Information Analysis",
        # Pick your license as you wish
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
