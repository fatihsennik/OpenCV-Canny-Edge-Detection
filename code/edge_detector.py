# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
import cv2
from gaussian_filter import gaussianfilter
from gradient import findinggradient
from nonmax_suppression import nonmax_suppression
from double_thresholding import double_thresholding
from numpy import array, zeros
from PIL import Image

from matplotlib.pyplot import imshow, show, subplot, gray, title, axis, figure, text


# 2.5 Edge tracking by hysteresis
# Strong edges are interpreted as “certain edges”, and can immediately be included in the final edge image.
#  Weak edges are included if and only if they are connected to strong edges. The
# logic is of course that noise and other small variations are unlikely to result
# in a strong edge (with proper adjustment of the threshold levels).
# Thus strong edges will (almost) only be due to true edges in the original image.
# The weak edges can either be due to true edges or noise/color variations.
# The latter type will probably be distributed independently of edges on the entire image,
# and thus only a small amount will be located adjacent to strong edges. Weak edges due to true edges
# are much more likely to be connected directly to strong edges.

class edge_tracking:
    def __init__(self, tr):
        self.im = tr[0]
        strongs = tr[1]

        self.vis = zeros(im.shape, bool)
        self.dx = [1, 0, -1,  0, -1, -1, 1,  1]
        self.dy = [0, 1,  0, -1,  1, -1, 1, -1]
        for s in strongs:
            if not self.vis[s]:
                self.dfs(s)
        for i in xrange(self.im.shape[0]):
            for j in xrange(self.im.shape[1]):
                self.im[i, j] = 1.0 if self.vis[i, j] else 0.0

    def dfs(self, origin):
        q = [origin]
        while len(q) > 0:
            s = q.pop()
            self.vis[s] = True
            self.im[s] = 1
            for k in xrange(len(self.dx)):
                for c in xrange(1, 16):
                    nx, ny = s[0] + c * self.dx[k], s[1] + c * self.dy[k]
                    if self.exists(nx, ny) and (self.im[nx, ny] >= 0.5) and (not self.vis[nx, ny]):
                        q.append((nx, ny))
        pass

    def exists(self, x, y):
        return x >= 0 and x < self.im.shape[0] and y >= 0 and y < self.im.shape[1]


if __name__ == '__main__':
    from sys import argv
    if len(argv) < 2:
        print "Usage: python %s <image>" % argv[0]
        exit()
    im = array(Image.open(argv[1]))


    im = im[:, :, 0]
    gim = gaussianfilter(im)
    grim, gphase = findinggradient(gim)
    gmax = nonmax_suppression(grim, gphase)
    thres = double_thresholding(gmax)
    edge = edge_tracking(thres)
    img = cv2.imread(argv[1], 0)
    opencvedges = cv2.Canny(img, 100, 200)
    gray()

    figure(figsize=(12, 12)).text(0.02, 0.2, 'Fatih ŞENNİK', fontsize=75, weight=1000, va='center')

    subplot(3, 3, 1)
    imshow(im)
    axis('off')
    title('Original Image')

    subplot(3, 3, 2)
    imshow(gim)
    axis('off')
    title('After Gaussian Filter')

    subplot(3, 3, 3)
    imshow(grim)
    axis('off')
    title('After Gradient')

    subplot(3, 3, 4)
    imshow(gmax)
    axis('off')
    title('After Non-Maximum Suppression')

    subplot(3, 3, 5)
    imshow(edge.im)
    axis('off')
    title('After Edge Tracking')


    subplot(3, 3, 6)
    imshow(opencvedges)
    axis('off')
    title('After Edge Tracking in OpenCV Version')

    show()
