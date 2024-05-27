from setuptools import setup, find_packages

setup(name = "mushroom",
         version = "0.0.1",
         author = "Simran",
         author_email = "shivangithakur7300@gmail.com",
         packages = find_packages(),
         install_requires = ["pandas","numpy","flask"]
         )