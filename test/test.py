import unittest, os, cv2
from pyzbar import pyzbar

class TestImageDecode(unittest.TestCase):

    def test_decode(self):
        bashDir = "./test_image"
        dirs = os.listdir(bashDir)
        failNum = 0
        for file in dirs:
            path = os.path.join(bashDir, file)
            img = cv2.imread(path)
            barcodes = pyzbar.decode(img)
            self.assertTrue(len(barcodes) > 0, ('%s decode failed' % file))
            if (len(barcodes) <= 0):
                failNum += 1
        print("decode %d images, failed %d times" % (len(dirs), failNum))
