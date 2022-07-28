from setuptools import setup, find_namespace_packages

setup(name='sorting_func_yp',
      version='1',
      description='Sorting your files',
      url='https://github.com/YeliseiPolishchuk/Go-It_7module',
      author='Yelisei Polishchuk',
      author_email='yelisei.polishchuk@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      include_package_data=True,
      entry_points={'console_scripts': ['helloworld = sorting_func_yp.main:sort_this']}
      )