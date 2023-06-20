import os, sys
import numpy as np

OUT_PATH = "dump_0620_google_search_images"

### Take all images
all_images = os.listdir(OUT_PATH)
print(len(all_images))
filtered_images = [x for x in all_images if ".png" in x]
print(len(filtered_images))

idx_to_take = np.arange(len(filtered_images))

for j in idx_to_take:
	print("<li class=\"loaded\"><a href=\"%s/%d_all.png\"><img src=\"%s/tmp/image%d-raw.png\" width=\"auto\" height=\"100\"></a></li>" % (OUT_PATH, j, OUT_PATH, j) )


