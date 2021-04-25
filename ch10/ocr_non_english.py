import pytesseract
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to input image to be OCR'd")
ap.add_argument("-l", "--lang", required=True,
    help="language that Tesseract will use when OCR'ing")
ap.add_argument("-p", "--psm", type=int, default=13,
    help="Tesseract PSM mode")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# OCR the image, supplying the country code as the language parameter
options = "-l {} --psm {}".format(args["lang"], args["psm"])
text = pytesseract.image_to_string(rgb, config=options)

# show the original OCR'd text
print("ORIGINAL")
print("========")
print(text)
print("")