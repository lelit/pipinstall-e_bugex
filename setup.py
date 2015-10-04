from setuptools import setup

setup(name='bugex.foo',
      version='1.0',
      description='Demo of pip -e not working with package_dir',
      long_description='',
      packages=['bugex.foo'],
      package_dir={'bugex.foo': 'src'},
      namespace_packages=['bugex'],
      zip_safe=False,
      install_requires=['setuptools']
      )
