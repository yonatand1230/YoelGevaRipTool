import requests, io, argparse, os
from PIL import Image
from reportlab.pdfgen import canvas


# init args parser
parser = argparse.ArgumentParser(description='Yoel Geva Rip Tool')
parser.add_argument('-b', '--book', help='Book ID')
args = parser.parse_args()

if not args.book:
    parser.print_help()
    exit()

BOOK_NAME = args.book


## PART 1. DOWNLOAD AS PNG ##

def textlayer(page: int):
    pageNum = str(page).zfill(4)
    return f'https://my.geva.co.il/flippbooks/{BOOK_NAME}/files/assets/common/page-textlayers/page{pageNum}_4.png'
def background(page: int):
    ext='png'
    if BOOK_NAME=='801': ext='jpg'
    pageNum = str(page).zfill(4)
    return f'https://my.geva.co.il/flippbooks/{BOOK_NAME}/files/assets/common/page-html5-substrates/page{pageNum}_4.{ext}'

if not os.path.exists('pages'): os.mkdir('pages')
else:
    for f in os.listdir('pages'): os.remove(os.path.join('pages',f))
"""
try:
    for page in range(3,1500+1):
        # Get Remote Images
        response = requests.get(background(page))
        print("Page", page, response)
        bg = response.content
        
        response = requests.get(textlayer(page))
        if response.status_code == 200:
            txt = response.content

            # Init Image Objects
            bgImg = Image.open(io.BytesIO(bg))
            txtImg = Image.open(io.BytesIO(txt))

            txtImg = txtImg.resize(bgImg.size)

            bgImg = bgImg.convert("RGBA")
            bgImg.paste(txtImg, (0,0), txtImg.convert("RGBA"))
            finalPage = bgImg
            finalPage.save(f'pages\\{page}.png')
        else:
            bgImg = Image.open(io.BytesIO(bg))
            bgImg = bgImg.convert("RGBA")
            finalPage = bgImg
            finalPage.save(f'pages\\{page}.png')
except Exception:
    pass # means its finished downloading"""

## PART 2. CONVERT TO PDF ##

png_files = os.listdir('pages')
png_files = sorted(png_files, key=lambda x: int(x.replace('.png','')))

output_pdf = f'{BOOK_NAME}.pdf'
page_size = (1410, 2050)

# Create a PDF file with the specified page size
c = canvas.Canvas(output_pdf, pagesize=page_size)

# Loop through the PNG files and add each one to the PDF
for f in png_files:
    print(f)
    png_file = os.path.join(f'C:\\Yonatan\\YGBooksRip\\pages', f)

    img = Image.open(png_file)
    img_width, img_height = img.size

    # Create a page with the specified size
    c.setPageSize(page_size)
    
    # Calculate the position to center the image on the page
    x_offset = (page_size[0] - img_width) / 2
    y_offset = (page_size[1] - img_height) / 2

    c.drawImage(png_file, x_offset, y_offset, img_width, img_height)
    c.showPage()

# Save the PDF
c.save()