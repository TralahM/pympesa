import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="daraja-mpesa",
    version="0.1",
    author="Tralah M Brian",
    author_email="briantralah@gmail.com",
    description="A Python wrapper for Mpesa Daraja APIs abstracting raw https request",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TralahM/pympesa",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'certifi', 'chardet>=3.0.4', 'future>=0.16.0', 'idna>=2.7', 'requests>=2.20.0',
        'six>=1.11.0', 'urllib3>=1.24.2', 'pytest>=3.6.1 '
    ],
)
