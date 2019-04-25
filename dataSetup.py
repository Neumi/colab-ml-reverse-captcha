from claptcha import Claptcha
from random import choice
from string import ascii_uppercase
from string import digits
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import re
import os
import config
import learn
import numpy as np

print("imports done!")



import config
captchasDir = 'captchas/'
imgXorigin = 200
imgYorigin = 80
offset = 15
imgX = imgXorigin - (2 * offset)
imgY = imgYorigin

captchaLength = 5






def generateRandString(length):
    # return ''.join(choice(ascii_uppercase) for i in range(length))
    return ''.join(choice(digits) for i in range(length))


def generateCaptcha(input):
    c = Claptcha(str(input), "DroidSansMono.ttf")
    text, image = c.image
    text, bytes = c.bytes
    text, file = c.write('captchas/' + str(input) + '.png')
    return


def generateCaptchaFamily(amount, length):
    i = 0
    while i < amount:
        i += 1
        randString = generateRandString(length)
        generateCaptcha(randString)


def generateTestFiles():
    i = 0
    amountFiles = 100
    while i < amountFiles:
        i += 1
        randString = generateRandString(captchaLength)
        try:
            generateCaptcha(randString)
            print(str(i) + '/' + str(amountFiles) + ' files generated')
        except:
            print('error while generating captcha')


def crop(image_path, coords, img_name):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(img_name)
    # cropped_image.show()


def extracktNumbersFromImage(image, number):
    digits = [int(d) for d in str(number)]
    crop(image, (offset, 0, imgXorigin - offset, imgYorigin), 'test_img.png')

    for (key, digit) in enumerate(digits):
        startX = (imgX / captchaLength) * key
        cutoffX = (imgX / captchaLength) * (key + 1)
        savePath = './numbers/' + str(digit) + '/'
        path, dirs, files = next(os.walk(savePath))
        file_count = len(files)
        crop('test_img.png', (startX, 0, cutoffX, imgY), savePath + 'img_' + str(file_count) + '.png')

def extractTestTrainImages(image, number, testOrTrain):
    digits = [int(d) for d in str(number)]
    crop(image, (offset, 0, imgXorigin - offset, imgYorigin), 'test_img.png')

    for (key, digit) in enumerate(digits):
        startX = (imgX / captchaLength) * key
        cutoffX = (imgX / captchaLength) * (key + 1)
#        savePath = './numbers/' + str(testOrTrain) + '/' + str(digit) + '-'
        savePath = './numbers/' + str(testOrTrain) + '/'
        path, dirs, files = next(os.walk(savePath))
        file_count = len(files)
        crop('test_img.png', (startX, 0, cutoffX, imgY), savePath + str(digit) + '.' + str(file_count) + '.png')

def generateNumbers():
    path, dirs, files = next(os.walk(captchasDir))
    for file in files:
        numberString = str(file.title()[:captchaLength])
        filePath = str(captchasDir + file.format())

        if not file.startswith('.'):
            print(numberString)
            print(filePath)
            extractTestTrainImages(filePath, numberString, 'test')
            #extracktNumbersFromImage(filePath, numberString)


def getStarted():
    generateCaptchaFamily(200, captchaLength)
    generateNumbers()
