#coding=utf-8
from __future__ import division
from numpy import array, zeros, max



# 2.4 Double thresholding Function
# The edge-pixels remaining after the non-maximum suppression step are (still)
# marked with their strength pixel-by-pixel. Many of these will probably be true edges in the image,
# but some may be caused by noise or color variations for instance due to rough surfaces.
# The simplest way to discern between these would be to use a threshold, so that only edges stronger
# that a certain value would be preserved. The Canny edge detection algorithm uses double thresholding.
# Edge pixels stronger than the high threshold are marked as strong; edge pixels weaker than the low
# threshold are suppressed and edge pixels between the two thresholds are marked as weak.



def double_thresholding(im):
    thres  = zeros(im.shape)
    strong = 1
    weak   = 0.6
    mmax = max(im)
    lo, hi = 0.1 * mmax,0.8 * mmax
    strongs = []
    for i in xrange(im.shape[0]):
        for j in xrange(im.shape[1]):
            px = im[i][j]
            if px >= hi:
                thres[i][j] = strong
                strongs.append((i, j))
            elif px >= lo:
                thres[i][j] = weak
    return thres, strongs








