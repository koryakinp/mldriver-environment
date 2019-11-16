from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
  name='mldriver-environment',
  version='0.0.1',
  description='Open AI gym-like wrapper around MLDriver Unity Environment',
  py_modules=['mldriver_environment'],
  package_dir={'': 'src'},
  classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7'
  ],
  long_description=long_description,
  long_description_content_type="text/markdown",
  python_requires='>=3.7'
)
