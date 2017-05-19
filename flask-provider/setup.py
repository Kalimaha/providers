from setuptools import setup
from setuptools import find_packages


setup(
    name='flask-provider',
    version='0.1.0',
    author='Guido Barbaglia',
    author_email='guido.barbaglia@gmail.com',
    packages=find_packages(),
    license='LICENSE',
    description='Simple Flask application.',
    install_requires=['flask'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-sugar', 'pytest-pep8']
)
