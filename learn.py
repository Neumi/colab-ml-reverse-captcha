from fastai.vision import *
from fastai.imports import *
from sklearn.utils import shuffle
import imageio


df_train=pd.read_csv("./train.csv")

df_train.head(3)


df_test=pd.read_csv("./test.csv")
df_test.head(5)
labels=df_train.label

images_df=df_train.drop("label", axis=1)
#plt.imshow(imageio.imread("./images/0_10007.jpg"))
# plt.show()



fnames = get_image_files("./images")
pat = r'/([^/]+)_\d+.jpg$'
tfms = get_transforms(do_flip=False)

data = ImageDataBunch.from_name_re("./images", fnames, pat, ds_tfms=tfms)
data.normalize(imagenet_stats)

# data.show_batch(rows=3, figsize=(7,6))


print(data.classes)
