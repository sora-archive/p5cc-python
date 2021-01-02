from PIL import Image, ImageDraw, ImageFont
import textwrap, sys

# configuration
FONT_PATH     = "./assets/earwig-factory.ttf"
FONT_SIZE     = 120
WRAPPER_WIDTH = 24
BACKGROUND    = "./assets/background.png"
P5_LOGO       = "./assets/logo.png"

def p5cc(message, savePath):
    lines = message.split("\n")
    lists = (textwrap.TextWrapper(width=WRAPPER_WIDTH,break_long_words=False).wrap(line) for line in lines)
    para  = "\n".join("\n".join(list) for list in lists)

    bg = Image.open(BACKGROUND)
    logo = Image.open(P5_LOGO)
    MAX_W, MAX_H = bg.size
    
    draw = ImageDraw.Draw(bg)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    w, h = draw.textsize(para, font=font)
    draw.text(((MAX_W-w)/2,(MAX_H-h)/2), para, font=font, fill="white", align='center', stroke_width=12, stroke_fill='black')

    im.paste(logo, (MAX_W - 300, MAX_H - 300), logo)
    im.save(savePath)
    
if __name__ == "__main__":
    if len(sys.argv <= 2):
        print("Usage: {} <filePath> <message>".format(sys.argv[0]))
    else:
        p5cc(sys.argv[2:], sys.argv[1])
        print("Your calling card has been saved at " + sys.argv[1])