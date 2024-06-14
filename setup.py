from setuptools import find_packages, setup

setup(
    name="log_analyzer",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "log-analyzer=log_analyzer.cli:main",
        ],
    },
    install_requires=[
        "pandas",
    ],
)
