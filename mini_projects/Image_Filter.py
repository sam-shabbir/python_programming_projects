# Image Filter
#
# This started as ImageFilter.py, which only had `import sys`.
# It applies a filter to an image from the command line:
#
#   python Image_Filter.py photo.jpg blur
#   python Image_Filter.py photo.jpg grayscale
#   python Image_Filter.py photo.jpg            <- lists the filters
#
# The result is saved next to the original as e.g. photo_blur.jpg
#
# pip install pillow   (Pillow is imported as "PIL" - an old name kept for compatibility)

import os
import sys # sys.argv holds the words typed after "python" on the command line
from PIL import Image, ImageFilter, ImageOps

# A dictionary that maps a filter NAME (what the user types) to a FUNCTION that applies it.
# `lambda img: ...` is a tiny unnamed function: it takes an image and returns the filtered image.
FILTERS = {
    "blur":      lambda img: img.filter(ImageFilter.GaussianBlur(radius=4)),
    "sharpen":   lambda img: img.filter(ImageFilter.SHARPEN),
    "contour":   lambda img: img.filter(ImageFilter.CONTOUR),
    "edges":     lambda img: img.filter(ImageFilter.FIND_EDGES),
    "emboss":    lambda img: img.filter(ImageFilter.EMBOSS),
    "grayscale": lambda img: ImageOps.grayscale(img),
    "invert":    lambda img: ImageOps.invert(img),
    "mirror":    lambda img: ImageOps.mirror(img),
}


def apply_filter(input_path, filter_name):
    # "with" closes the image file automatically when we're done, like with open()
    with Image.open(input_path) as img:
        # Some filters only work on plain RGB images (not PNGs with transparency, etc.)
        img = img.convert("RGB")
        result = FILTERS[filter_name](img) # look up the function in the dictionary, then call it

    # os.path.splitext("photo.jpg") -> ("photo", ".jpg"), so we can insert the filter name
    name, extension = os.path.splitext(input_path)
    output_path = f"{name}_{filter_name}{extension}"
    result.save(output_path)
    return output_path


def main():
    # sys.argv[0] is the script's own name, so the user's words start at sys.argv[1]
    if len(sys.argv) != 3:
        print("Usage: python Image_Filter.py <image file> <filter>")
        print("Filters:", ", ".join(FILTERS)) # looping over a dictionary gives its keys
        sys.exit(1) # exit code 1 tells the terminal "something went wrong"

    input_path = sys.argv[1]
    filter_name = sys.argv[2].lower()

    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        sys.exit(1)

    if filter_name not in FILTERS:
        print(f"Unknown filter '{filter_name}'. Choose from:", ", ".join(FILTERS))
        sys.exit(1)

    try:
        output_path = apply_filter(input_path, filter_name)
    except OSError: # Pillow raises this when the file isn't an image it can read
        print(f"Could not open '{input_path}' as an image.")
        sys.exit(1)

    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
