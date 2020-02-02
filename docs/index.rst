.. Tasveer documentation master file, created by
   sphinx-quickstart on Fri Jan 31 08:21:33 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
===================================
Tasveer: An image-downloading package in python
===================================
It is a python package to quickly download a few images for testing/validation purposes.
The following documentation will guide you through installation and usage of tasveer.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
=================
Installing Tasveer
=================

First you need to install tasveer on your system using the pip package manager.::

	pip install tasveer
This installs the package to your local machine.

=========
Using Tasveer 
=========

After installing tasveer, you need to import it to use in python codes.::

	import tasveer as tsv
	
Once this is done, the package can be used under the name 'tsv' in your python code.To initiate the download of images, we use the ``download`` funtion in the tasveer module.There are 2 ways to work with this function:

#. **Without arguments**
	If the function is called without arguments as ``tsv.download()``,a prompt asking the following is generated-
	
	* *Query*: The query for which the images are to be generated. Example, if you enter "chocolates", images of chocolates will be downloaded.

	* *Number of downloads*: The number of images to be downloaded.

	* *Size*: The size of images.

#. **With arguments**
	The call to the function can also be done as- 
	::
		tsv.download(query="<SEARCH_STRING>", count="<NUM_IMAGES_AS_INT>",width="<WIDTH>",height="<HEIGHT>")
	
	specifying the parameters within the call.

After this,the specified number of images will be downloaded in the current directory under the **downloads** folder.



