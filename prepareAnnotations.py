import json
import sys
import os
from pprint import pprint

dataDir = './data'
category_id = 13 # stop sign



for dataType in ["train2014", "val2014"]:
    annotationFile = '%s/annotations/instances_%s.json' % (dataDir, dataType)
    annotationFileBackup = '%s/annotations/instances_%s-bak.json' % (dataDir, dataType)

    if os.path.exists(annotationFileBackup):
        print("Delete", annotationFileBackup, "first")
        sys.exit(1)

    newAnnots = []
    newImgIds = []
    newImg = []
    newCats = []
    with open(annotationFile) as data_file:    
        data = json.load(data_file)
        print("Loaded", dataType)

    for category in data["categories"]:
        if category["id"] == category_id:
            newCats.append(category)

    for annotation in data["annotations"]:
        if annotation["category_id"] == category_id:
            newAnnots.append(annotation)
            newImgIds.append(annotation["image_id"])

    for image in data["images"]:
        if image["id"] in newImgIds:
            newImg.append(image)

    data["images"] = newImg
    data["annotations"] = newAnnots
    data["categories"] = newCats
    print("Processed")

    os.rename(annotationFile, annotationFileBackup)

    with open(annotationFile, 'w') as outfile:
        json.dump(data, outfile)       
        print("Saved", dataType) 
