# YoelGevaRipTool
A Python script created to archive digital books from Yoel Geva's website.

**The tool was created for educational purposes only.** \
**The tool is NOT meant to encourage piracy or be used for any illegal purpose.**

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
