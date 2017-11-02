# https://packaging.python.org/en/latest/distributing.html

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # details
    name='animelyrics',
    version='1.0.0',
    description='Retrieving anime lyrics for songs',
    long_description=long_description,
    url='https://github.com/emily-yu/anime',

    # author
    author='Emily Yu',
    author_email='eyudeveloper@gmail.com',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='anime development http',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    python_requires='>=3',
    py_modules=["animelyrics"],
    include_package_data = True,
    zip_safe = False,

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['urllib.request', 'bs4', 'requests', 'google', 'urllib.parse'],
)