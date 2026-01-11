from setuptools import setup, find_packages

setup(
    name="lucidmind",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "plotly",
        "pyyaml",
        "autograd",
    ],
)
