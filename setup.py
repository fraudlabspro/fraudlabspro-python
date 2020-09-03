import setuptools

with open("readme.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="fraudlabspro-python",
	version="1.2.0",
	author="FraudLabs Pro",
	author_email="support@fraudlabspro.com",
	description="A Python module enables user to easily implement fraud detection feature into their solution using the API from https://www.fraudlabspro.com.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://www.fraudlabspro.com",
	packages=setuptools.find_packages(),
	classifiers=(
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	),
)