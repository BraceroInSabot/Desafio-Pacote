from setuptools import setup, find_packages

with open("PAGE.md", "r") as f:
    page_description = f.read()

"""
Caso tenha que instalar pacotes de terceiros:

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
"""

setup(
    name="package_name"
)