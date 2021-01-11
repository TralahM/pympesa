import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="daraja-mpesa",
    version="1.2",
    author="Tralah M Brian",
    author_email="briantralah@gmail.com",
    description="A Python wrapper for Mpesa Daraja APIs abstracting raw https request",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TralahM/pympesa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "certifi",
        "chardet",
        "future",
        "idna",
        "requests",
        "six",
        "urllib3",
    ],
)
