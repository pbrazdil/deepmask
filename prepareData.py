from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import os.path
import sys

if len(sys.argv) <= 1:
  print("Data Type argument needs to be `val2014` or `train2014`.")
  sys.exit(1)

dataDir = './data'
dataType = sys.argv[1]

fdir = '%s/%s' % (dataDir, dataType)
if not os.path.exists(fdir):
  os.makedirs(fdir)

annotationFile = '%s/annotations/instances_%s.json' % (dataDir, dataType)

coco = COCO(annotationFile)
catIds = coco.getCatIds(catNms=['stop sign']);
imgIds = coco.getImgIds(catIds=catIds);

i = 1
for val in imgIds:
  print("%d / %d" % (i, len(imgIds)))
  id = str(val)
  fname = '%s/COCO_%s_%s.jpg' % (fdir, dataType, "0" * (12-len(id)) + id)
  if not os.path.exists(fname):
    img = io.imread('http://mscoco.org/images/%s' % (id))
    io.imsave(fname, img)
  
  i += 1

print("Download done")
