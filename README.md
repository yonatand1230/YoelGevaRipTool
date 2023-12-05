# YoelGevaRipTool
A Python script created to archive digital books from Yoel Geva's website.

**The tool was created for educational purposes only.** \
**The tool is NOT meant to encourage piracy or be used for any illegal 
purpose.**

## How It Works

On the first part of the tool, it uses a breach in Yoel Geva's website in 
order to access all of the files and the different books. First, it 
downloads every page of the book - both the `textlayers` and the 
`html5-substrates` (which are the foreground and the background of every 
page). Then, using the `PIL` module, it merges both files to a single PNG 
picture, saved in the `pages` directory. 

On its second part, the tool makes a PDF from all of the PNGs saved
earlier. It's done using the `reportlab` module. This PDF is saved in the
current working directory, and its name will be the Book ID.

## Setup
1. Clone the repository by running the following command:
```bash
git clone https://github.com/yonatand1230/YoelGevaRipTool.git
```

2. Install dependencies using PyPi:
```bash
pip3 install -r requirements.txt
```

## Usage

To download a book, simply run **YoelGevaRipTool.py** with the `--book` argument specifying the Book ID.
```bash
python3 YoelGevaRipTool.py --book 806c
```

### Getting The Book ID

The Book ID is made out of 2 elements: \
The questionnaire number, and the volume. 

For example, Volume D of questionnaire 804 is `804d`.

*No need to specify the volume if the questionnaire only has one. \
*Keep in mind that the first two volumes of questionnaires 804 and 806 are the same (for example: `804-806a`).
