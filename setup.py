from setuptools import find_packages, setup

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(name='nperf',
      version='0.0.1',
      description="Python network performance tools",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/jncraton/nperf',
      author='Jon Craton',
      author_email='jncraton@gmail.com',
      packages=find_packages(exclude=['contrib', 'docs', 'tests', 'bin']),
      classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License'
    ],
)
