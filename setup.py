from setuptools import setup, find_packages

setup(
    name="zenoo-cli",
    version="0.0.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "zenoo=src.main:cli",
        ],
    },
)