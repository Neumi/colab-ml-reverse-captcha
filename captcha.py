from claptcha import Claptcha
from random import choice
from string import ascii_uppercase
from string import digits


def generateRandString(length):
    # return ''.join(choice(ascii_uppercase) for i in range(length))
    return ''.join(choice(digits) for i in range(length))


def generateCaptcha(input):
    c = Claptcha(str(input), "DroidSansMono.ttf")
    text, image = c.image
    text, bytes = c.bytes
    text, file = c.write('captchas/' + str(input) + '.png')
    print(input)


# def splitCaptcha():
i = 0
while i < 10000:
    i += 1
    randString = generateRandString(5)
    generateCaptcha(randString)

