from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

requirements = ['ipython>=7.9', 'requests>=2.22']

setup(
    name='clb-nb-utils',
    version='0.1.0-dev',
    description='Collaboratory Notebook Utils',
    long_description=long_description,
    author="Jonathan Villemaire-Krajden, EPFL",
    author_email="jonathan.villemaire-krajden@epfl.ch",
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=requirements,
)
