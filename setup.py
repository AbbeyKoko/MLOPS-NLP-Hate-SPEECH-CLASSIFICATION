from setuptools import find_packages, setup
import os

setup(
  name=os.getenv("PROJECT_NAME"),
  version="0.0.1",
  author=os.getenv("AUTHOR"),
  author_email=os.getenv("AUTHOR_EMAIL"),
  packages=find_packages(),
  install_requires=[]
)