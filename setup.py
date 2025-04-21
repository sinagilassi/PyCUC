from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

APP_NAME = 'PyCUC'
VERSION = '2.0.0'
AUTHOR = 'Sina Gilassi'
AUTHOR_EMAIL = "<sina.gilassi@gmail.com>"
DESCRIPTION = 'PyCUC: A lightweight Python package for creating custom unit conversions.'
LONG_DESCRIPTION = "PyCUC: A lightweight Python package for creating custom unit conversions. Easily define and convert between units with simplicity and flexibility"

# Setting up
setup(
    name=APP_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
    license='MIT',
    license_files=[],
    # require files
    package_data={'': ['*.yml']},
    install_requires=['pandas', 'numpy', 'PyYAML'],
    keywords=['python', 'chemical engineering', 'custom unit conversion',
              'PyCUC'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3.10",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.10',
)
