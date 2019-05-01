import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dxclient",
    version="0.0.1",
    author="Sushant Aggarwal",
    author_email="sushant.aggarwal@ihsmarkit.com",
    description="DxOpen Client for Python 2.7",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ihsmarkit.com",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    )
)