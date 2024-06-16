from setuptools import find_packages, setup

from config import constants as cons

setup(
    name="log_analyzer",
    version=cons.VERSION,
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
