# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.2.0dev1
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "amphoradata"
VERSION = "0.2.0.dev1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Amphora Data Api",
    author_email="",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Amphora Data Api"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    API for interacting with the Amphora Data platform.  # noqa: E501
    """
)
