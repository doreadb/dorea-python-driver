from setuptools import setup, find_packages

setup(
    name='dorea-python-driver',
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "requests==2.26.0",
    ],
    url='https://github.com/doreadb/dorea-python-driver',
    license='MIT',
    author='ZhuoEr Liu',
    author_email='mrxzx.info@gmail.com',
    description='DoreaDB Python Driver'
)