from setuptools import setup


with open("README.md", "r") as readme:
	long_description = readme.read()

setup(
	name = "send_ip",
	version="0.0.1",
	description="python package to send its own IP to another machine through ssh",
	py_modules=["send_ip.py"],
	package_dir={'' : 'src'},
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent"
	],
	long_description=long_description,
	long_description_content_type="text/markdown",
	install_requires= [
		"PyYAML >= 5.3.1",
		"paramiko >= 2.6.0",
	],
	extras_require={
		"dev" : [
		"twine",
		"check-manifest",
		"PyYAML == 5.3.1",
		"paramiko == 2.6.0"]
		},
	url="github address",
	author="Matias Andina",
	author_email="matiasandina@gmail.com"
)