from setuptools import setup, find_packages

with open("PAGE.md", "r") as f:
    page_description = f.read()

"""
Caso tenha que instalar pacotes de terceiros:

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
"""

setup(
    name="return-hello",
    version="0.0.1",
    author="Guilherme Bracero",
    author_email="guilhermebracero@gmail.com",
    description="Meu primeiro pacote, não possui muita efetividade",
    url="https://github.com/BraceroInSabot/Desafio-Pacote",
    packages=find_packages(),
    python_requires=">=3.10"
)