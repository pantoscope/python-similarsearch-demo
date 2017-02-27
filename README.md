# python-similarsearch-demo
A simple example showing how the Similar Image Search API is used
#How to get started
Simply clone this repo or download apiDemo.py.<br>
You will need Python2.7 installed with the [requests](http://docs.python-requests.org/en/master/) library
#Usage
First you need to register at http://developer.scopemedia.com/.<br>
When you are registered, create an application and you will receive your client ID and client Secret which you will use to authenticate your requests.<br>
Open apiDemo.py in a text editor and replace 'your ID here' and 'your SECRET here' with your client ID and Secret for the variables <code>clientId</code> and <code>clientSecret</code>. Save the file.<br>
Once you have your credentials set, run the script with two commandline arguments, the path to or url of the image to search on, and the search mode. <br>
The search mode should be one of: "local", "remote", indicating that the input image is an absolute URI, a local path to an image, or the URI of an image, respectively.<br>
The output will be a list of image URLs with features similar to the input image.
#Sample execution
* Help
```
python apiDemo.py --help
```

* Remote Url
```
python apiDemo.py -m remote -r http://goo.gl/8fgVc4
```

* Local File
```
python apiDemo.py -m local -l ./example_output.png
```

#Sample output
![alt tag](https://github.com/pantoscope/python-similarsearch-demo/blob/master/example_output.png)
#More information
Check out http://developer.scopemedia.com/docs/similar-image-search/ for more information!


