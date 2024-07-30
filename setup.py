from setuptools import setup


with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='connectpyse',
      version='0.7',
      description='A ConnectWise API tool for the rest of us.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5'
      ],
      keywords='connectwise rest api',
      url='https://github.com/markciecior/ConnectPyse',
      author='Joshua M Smith (original), Mark Ciecior (forked), @wesgann',
      author_email='saether@gmail.com (original), mark@markciecior.com (forked)',
      license='MIT',
      packages=['.',
                'connectpyse.company',
                'connectpyse.expense',
                'connectpyse.finance',
                'connectpyse.marketing',
                'connectpyse.procurement',
                'connectpyse.project',
                'connectpyse.sales',
                'connectpyse.schedule',
                'connectpyse.service',
                'connectpyse.system',
                'connectpyse.time'],
      py_modules = ['connectpyse.cw_controller',
                    'connectpyse.config',
                    'connectpyse.cw_model',
                    'connectpyse.restapi'],
      install_requires=[
          'requests'
      ],
      include_package_data=True,
      zip_safe=False)
