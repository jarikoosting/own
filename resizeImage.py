#!/usr/bin/python
# Jarik Oosting, 27-03-2015
# Tested on Mac OS X, PIL is necessary
# Use: ./filename.py directory width
# Where width is the width of the resized image


from PIL import Image
import sys
import os

def main(argv):

    if len(argv) == 3:

        # Get directory and width
        dir = argv[1]
        width = argv[2]

        # Loop trough directory
        for image in os.listdir(dir):

            # For Mac folders where's a .DS_Store file
            if image != ".DS_Store":

                # Open the image
                img = Image.open(os.path.join(dir, image))

                # Calculate the height using the same aspect ratio
                widthPercent = (width / float(img.size[0]))
                height = int((float(img.size[1]) * float(widthPercent)))

                # Resize the image
                img = img.resize((width, height), Image.BILINEAR)

                # Save it with a new name
                img.save(os.path.join(dir, 'resized-' + image))

if __name__ == "__main__":
    main(sys.argv)