try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from glob import glob

path_input = r"C:\Git\OCRProto\tests\data\*.png"
files = glob(path_input)

for file in files:

    # Simple image to string
    data_string = pytesseract.image_to_string(Image.open(file))
    with open(file.replace("png", "txt"), 'w') as f:
        f.write(data_string) # pdf type is bytes by default
