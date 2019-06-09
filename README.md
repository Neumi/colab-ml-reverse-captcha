# colab-ml-reverse-captcha

## Motivation
At first this only started as a proof-of-concept project, as I thought that a simple MNIST Dataset is too easy to solve.
As [MNIST](https://en.wikipedia.org/wiki/MNIST_database) is the most implemented Machine Learning 'Hello World', I was able to get it running quite fast. Using [FastAis](https://www.fast.ai/) CNN-learner and a pretrained [resnet18](https://download.pytorch.org/models/resnet18-5c106cde.pth) model I got an impressive success rate on the standard MNIST dataset. 

The next step was to geneate my own dataset using [Claptchas](https://pypi.org/project/claptcha/) captcha generator. I started with a simple 5-digit numerical dataset and only upgraded in a second step to alphanumerical lower + uppercase 5-digit dataset. To generate individual images of the characters I simply (by simply I mean the most time-consuming part 🙄) used some [imageio](https://pypi.org/project/imageio/) image copping functions and some seemingly never ending loops.

After getting this running the rest was easy... retrain the restnet18 and go for it! 
In the end I was able to get some really promising (by promising I mean dead-evil) results. A friend of mine tweaked the model to an error_rate of 0.034 by using the densenet201 insted the weaker resnet18. This is obviously enough to provide an important part to break a large quantity of online security systems (postbank and ebay are proven) in a few milliseconds.


## Why do I publish code for attacking anti-fraud systems?
A few days ago I tried to login to my ebay account but instead my account had a brand new russian email adress. After accidently telling ebay to send the new password to the new adress, I instantly realized my blunter and used their second stage of security (SMS). In the end I was lucky the russian guy was too slow and I was able to change my password before he was. But if I had not been as fast, all my 180+ Top-Star reviews and my payment method would be gone. 

*Happy End*


My Ebay Account had a new owner for a few hours:
![ebay screenshot](/ebay.png "ebay screenshot" )


### But:
The problem still exists and is a real danger in online security. Captchas are there for a reason but in the current shape useless (even Googles reCAPTCHA is machine-solveable). 

What I tried to prove was to show that captchas are not save by any means. 

Please Ebay, Postbank and all the other large companys with security systems online, update your security strategy!



## Try it yourself:
Run the [jupyter notebook](https://colab.research.google.com/github/Neumi/colab-ml-reverse-captcha/blob/master/captch_ml_solver_all_chars.ipynb) in a free [Google colab](https://colab.research.google.com) instance with GPU support to test it!

This is an example of a captcha it can solve:
![Image of Captcha](https://raw.githubusercontent.com/Neumi/colab-ml-reverse-captcha/master/222656830282970083.png)
