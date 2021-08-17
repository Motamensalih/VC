import setuptools
with open("README.md" , "r" , encoding = "utf-8") as fh:
	long_description = fh.read()

setuptools.setup(name = "MyFirstPackage , 
		version = "0.0.1" , 
		author = "Motamen Salih" ,
		author_email = "motamen.salih@hotmail.com" , 
		description = "A small Example Package" , 
		long_description = long_description , 
		long_description_content_type = "text/markdown" , 
		url = "https://github.com/pypa/sampleproject" , 
		classifiers = [ "Programming Language ::Python::3" , 
				"License :: OSI Approved :: MIT License" ,
				"Operating System :: OS Independent"] ,
		packages = setuptools.find_packages() ,
		python_requires = '>=3.6")