from setuptools import setup, find_packages

with open('aoc2020/__init__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")

setup(
    name='aoc2020',
    version=version,
    packages=find_packages(include=['aoc2020*', 'utils']),
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pandas',
    ],
    entry_points={}
)