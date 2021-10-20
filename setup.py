from setuptools import setup

setup(name='apyrva',
      version='0.1',
      description='bare-bones python',
      url='http://github.com/apoorvalal/apyrva',
      author='Flying Circus',
      author_email='lal.apoorva@gmail.com',
      license='MIT',
      packages=['apyrva'],
      install_requires=[
          'requests', 'pandas', 'numpy', 'requests_html'
      ],
      zip_safe=False)
