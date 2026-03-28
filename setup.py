from setuptools import setup, find_packages

setup(
    name="fitsms",
    version="1.0.0",
    author="Danuja Dilanka",
    description="Official Python SDK for FitSMS.lk Gateway",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires='>=3.6',
)