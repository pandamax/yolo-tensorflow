import numpy as np
from datasets import PascalVOC


def getbboxes(basepath):
    bboxes = []
    dataset = PascalVOC.PascalVOC('PascalVOC2012', basepath)
    for category in dataset.categorynames:
        imagefiles = dataset.imagesfromcategory(category, subset="trainval")
        for i in imagefiles.index.tolist():
            annotationdict = dataset.annotationdictfor(imagefiles[i])
            for key, value in annotationdict.items():
                for v in value:
                    bboxes += v
        print('Done for the category of {}'.format(category))
    bboxes = np.reshape(bboxes, (int(len(bboxes) / 4), 4))
    return bboxes
