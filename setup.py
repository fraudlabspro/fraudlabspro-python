import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="fraudlabspro-python",
	version="3.0.3",
	author="FraudLabs Pro",
	author_email="support@fraudlabspro.com",
	description="A Python module enables user to easily implement fraud detection feature into their solution using the API from https://www.fraudlabspro.com.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://www.fraudlabspro.com",
	packages=setuptools.find_packages(),
	tests_require=['pytest>=3.0.6'],
	classifiers=(
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	),
)