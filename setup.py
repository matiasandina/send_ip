from setuptools import setup, find_packages


with open("README.md", "r") as readme:
	long_description = readme.read()

setup(
	name = "send_ip",
	version="0.0.8",
	description="python package to send its own IP to another machine through ssh",
	package_dir={'' : 'src'},
	packages = find_packages("src"),
	#py_modules=["send_ip.py"],
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
		"python-crontab >= 0.23.0",
		"py_console",
		"scp"
	],
	extras_require={
		"dev" : [
		"twine",
		"check-manifest",
		"PyYAML == 5.3.1",
		"paramiko == 2.6.0"]
		},
	url="https://github.com/matiasandina/send_ip",
	author="Matias Andina",
	author_email="matiasandina@gmail.com"
)