import setuptools
import os

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(name='jsonstore-socket',
	version='0.0.1',
	description='A socket-like connection over jsonstore.io',
	long_description=read("README.md"),
	url='https://github.com/AgeOfMarcus/jsonstore-socket',
	author='Marcus Weinberger',
	author_email='marcus@marcusweinberger.com',
	license='GPL',
	packages=setuptools.find_packages(),
	zip_safe=False,
	install_requires=[
		"json-store-client"
	])
