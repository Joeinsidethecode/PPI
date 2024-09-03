from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    descricao_pagina = f.read()

with open('requerimentos.txt') as f:
    requerimentos = f.read().splitlines()

setup(
    name='pacote_processamento_imgaens',
    version='0.0.1',
    author='Valmir Ribeiro',
    author_email='joeinsidethecode@gmail.com',
    description='Criação de Pacote de Processamentos de Imagens',
    long_description='Este projeto foi criado seguindo as aulas do curso "Criando um Pacote de Processamentode Imagens com Python" apresentado por Karina Kato para a DIO.',
    url='https://github.com/Joeinsidethecode/simple-package-template',
    packages=find_packages(),
    install_requiriments=requerimentos,
    python_requires='',
)