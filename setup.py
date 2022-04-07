from setuptools import setup, find_packages

setup(
    name='flww',
    description='Python suite for the design of femtosecond-written circuit.',
    version='1.0',
    packages=find_packages(include=['flww',
                                    'compiler',
                                    'compiler.*',
                                    'objects',
                                    'objects.*']),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'plotly',
        'openpyxl',
        'scipy'
    ],
)