from setuptools import setup

setup(
    name="genie-cli",
    version="1.0.0",
    description="A CLI for interacting with EnvGenie",
    url="https://github.com/parikshit-parspec/genie-cli",
    author="Parikshit Misra",
    author_email="parikshit@parspec.io",
    packages=["genie-cli"],
    install_requires=[
        "pytz",
        "requests",
        "typer",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.11",
    ],
)
