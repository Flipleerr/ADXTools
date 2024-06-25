from setuptools import setup, find_packages

setup(
    name='adxtools',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'adxtools=adxtools.main:main',
        ],
    },
    install_requires=[],
    author='memoryleak',
    author_email='theflipleerr@gmail.com',
    description='A set of lightweight command-line tools written in Python for modifying ADX files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Flipleerr/ADXTools',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: GPL v2.0',
        'Operating System :: Windows',
    ],
    python_requires='>=3.6',
)