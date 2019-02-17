# OpenCV Canny Edge Detection

## How Does Canny Edge Detection work ?
Canny Edge Detection is a popular edge detection algorithm. It was developed by John F. Canny
It is a multi-stage algorithm and I will go through each stages.

1)Noise Reduction

Since edge detection is susceptible to noise in the image, first step is to remove the noise in the image with a 5x5 Gaussian filter. Smoothing using Well Known Gaussian filter Function
It is inevitable that all images taken from a camera will contain some amount of noise.
To prevent that noise is mistaken for edges, noise must be reduced.
Therefore the image is first smoothed by applying a Gaussian filter.

Finding Intensity Gradient of the Image

Smoothened image is then filtered with a Sobel kernel in both horizontal and vertical direction to get first derivative in horizontal direction ( Gx) and vertical direction ( Gy). Finding gradients
The Canny algorithm basically finds edges where the grayscale intensity of the image changes the most.
These areas are found by determining gradients of the image.
Gradients at each pixel in the smoothed image are determined by applying
what is known as the Sobel-operator.

2)Non-maximum Suppression

Non-maximum suppression Function. The purpose of this step is to convert the blurred edges
in the image of the gradient magnitudes
to sharp edges. Basically this is done by preserving all local maxima in the gradient image,
and deleting everything else. The algorithm is for each pixel in the gradient image
In short, the result you get is a binary image with "thin edges".

3)Hysteresis Thresholding

Edge tracking by hysteresis
Strong edges are interpreted as “certain edges”, and can immediately be included in the final edge image.
Weak edges are included if and only if they are connected to strong edges. The
logic is of course that noise and other small variations are unlikely to result
in a strong edge (with proper adjustment of the threshold levels).
Thus strong edges will (almost) only be due to true edges in the original image.
The weak edges can either be due to true edges or noise/color variations.
The latter type will probably be distributed independently of edges on the entire image,
and thus only a small amount will be located adjacent to strong edges. Weak edges due to true edges
are much more likely to be connected directly to strong edges.

In short, This stage also removes small pixels noises on the assumption that edges are long lines. [Read More On OpenCV](https://docs.opencv.org/3.1.0/da/d22/tutorial_py_canny.html)


# How to Use it ?

Example python command to run in terminal;
python edge_detector.py im01.jpg

#  Libs used!

  - Python:2.7, numpy, PIL, cv2 , m:tplotlib.pyplot
  
  
#  IDE used!

  - IDE: PyCh:rm 2018.2.4 (Community Edition)

#  Features!

  - All Canny Edge Detection's each stages are plotted on figure. The Stages are as following;
  1)Original Image
  2)After Gaussian Filter
  3)After Gradient
  4)After Non-Maximum Suppression
  5)After Edge Tracking
  6)After Edge Tracking using OpenCV Function for canny edge algorithm
  
## Authors

* **Fatih Şennik**

License
----
MIT License

Copyright (c) 2019 Fatih Şennik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

**Free Software [Senniksoft.com](http://www.senniksoft.com/)**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
