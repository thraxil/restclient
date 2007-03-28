from setuptools import setup, find_packages

setup(
    name="restclient",
    version="0.9.8",
    author="Anders Pearson",
    author_email="anders@columbia.edu",
    url="http://microapps.sourceforge.net/restclient/",
    description="convenient library for writing REST clients",
    long_description="makes it easy to invoke REST services properly",
    install_requires = ["httplib2"],
    scripts = [],
    license = "BSD",
    platforms = ["any"],
    zip_safe=False,
    packages=find_packages(),
    test_suite='nose.collector',
    )
    
