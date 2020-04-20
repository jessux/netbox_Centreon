from setuptools import find_packages, setup

setup(
    name='netbox-Centreon-objects',
    version='0.1',
    description='A NetBox plugin for Centron objects',
    url='https://github.com/jessux/netbox-Centreon',
    author='Gabriel KAHLOUCHE',
    license='Apache 2.0',
    install_requires=["requests"],
    packages=find_packages(),
    include_package_data=True,
)