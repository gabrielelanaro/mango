from setuptools import setup, find_packages

setup(name='mango',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      install_requires=['click', 'numpy'],
      packages=find_packages(),
      zip_safe=False)
