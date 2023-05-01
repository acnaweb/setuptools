# setup.py


from setuptools import setup, find_packages


# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


REQUIREMENTS = ['pandas']
EXTRAS_REQUIRE = ['jupyter', 'flake8']


setup(
    name='pkgbase',
    version='0.1.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Antonio Carlos de Lima Junior',
    author_email='antonioclj.ac@gmail.com',
    url='https://github.com/acnaweb',
    packages=find_packages(include=['pkgbase']),
    install_requires=REQUIREMENTS,
    extras_require={
        'interactive': EXTRAS_REQUIRE
    },
    platforms='any',
    entry_points={
        'console_scripts': [
            'pkgbase=pkgbase.main:main'
        ]
    },
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest'],
)
