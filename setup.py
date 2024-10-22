from setuptools import setup, find_packages

setup(
    name='gendia',
    version='0.3.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'gendia=src.main:main',  # Adjust this to your CLI entry point
        ],
    },
    author='Silicon27',
    author_email='yangsilicon@gmail.com',
    description='A Python CLI to generate a tree structured diagram for any directory',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Silicon27/gendia',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)