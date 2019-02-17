#coding=utf-8
from __future__ import division
from gaussian_filter import gaussianfilter
from numpy import array, zeros, abs, sqrt, arctan2, arctan, pi, real
from numpy.fft import fft2, ifft2


# 2.2 Function for Finding gradients
# The Canny algorithm basically finds edges where the grayscale intensity of the image changes the most.
# These areas are found by determining gradients of the image.
# Gradients at each pixel in the smoothed image are determined by applying
# what is known as the Sobel-operator.


def findinggradient(im):
    # Given Sobel operator kernels
    op1 = array([[-1, 0, 1],
                 [-2, 0, 2],
                 [-1, 0, 1]])
    op2 = array([[-1, -2, -1],
                 [ 0,  0,  0],
                 [ 1,  2,  1]])
    kernel1 = zeros(im.shape)
    kernel1[:op1.shape[0], :op1.shape[1]] = op1
    kernel1 = fft2(kernel1)

    kernel2 = zeros(im.shape)
    kernel2[:op2.shape[0], :op2.shape[1]] = op2
    kernel2 = fft2(kernel2)

    fim = fft2(im)
    Gx = real(ifft2(kernel1 * fim)).astype(float)
    Gy = real(ifft2(kernel2 * fim)).astype(float)

    G = sqrt(Gx**2 + Gy**2)
    Theta = arctan2(Gy, Gx) * 180 / pi
    # The direction is rounded to one of four possible angles (namely 0, 45, 90 or 135)
    # https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/canny_detector/canny_detector.html
    return G, Theta




