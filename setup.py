from setuptools import setup, find_packages

setup(
    name='randomquote',
    version='0.1',
    description='Get a random quote',
    url='http://github.com/tanmay019',
    author='Tanmay Gautam',
    author_email='github@trstringer.com',
    license='MIT',
    install_requires=['requests'],
    packages=find_packages(),
    entry_points=dict(
        console_scripts=['rq=src.main:main']
    )
)