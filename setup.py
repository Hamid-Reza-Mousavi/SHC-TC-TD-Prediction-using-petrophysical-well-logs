#
from setuptools import setup

setup(
        name="SHC|TC|TD Prediction",
        version="1.1.0",
        url="https://github.com/Esfahani98/SHC-TC-TD-Prediction.git",
        author="Hamid Reza Mousavi",
        license="IUST",
        packages=["Models"],
        include_package_data=True,
        install_requires=["numpy, pandas, sklearn"]
)
