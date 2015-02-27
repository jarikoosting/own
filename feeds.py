#!/opt/local/bin/python3.4
# Jarik Oosting, 27-02-2015
# Script for filtering XML feeds

import sys
import xml.etree.ElementTree as ET

def main(argv):

    if len(argv) == 4:

        # Open XML file and get the root
        tree = ET.parse(argv[1])
        root = tree.getroot()

        # Loop every subchild in the child "product"
        for child in root.findall("product"):
            productCategory = child.find("categorie").text

            # Check if category is unequal to the subchild's category
            if productCategory != argv[3]:
                root.remove(child)

        # Make a new XML file with the filtered items
        tree.write(argv[2])

    elif len(argv) > 5:
        print("Please give only one category")
    else:
        print("Wrong command given")

if __name__ == "__main__":
    main(sys.argv)