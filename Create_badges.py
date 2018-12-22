from PIL import Image, ImageDraw, ImageFont
import os
from member import Member


def init_badges_directory():
    badges_path = "badges"
    badges_output = "badges_output"
    if not os.path.isdir(badges_path):
        os.mkdir(badges_path)
    if not os.path.isdir(badges_output):
        os.mkdir(badges_output)


def get_badges_images(badges_path="badges"):
    images = [str(badges_path+"/"+f) for f in os.listdir(badges_path) if os.path.isfile(os.path.join(badges_path, f))]
    return images


def combine_badges(badges_path="badges"):
    images = get_badges_images()
    result = Image.new("RGB", (1800, 2700))
    images_to_add = {}
    i = 0
    j = 0
    for image in images:
        images_to_add[i] = image
        if len(images_to_add) == 9:
            for index, image in images_to_add.items():
                img = Image.open(image)
                img.thumbnail((1800, 2700), Image.ANTIALIAS)
                x = index // 3 * 600
                y = index % 3 * 900
                w, h = img.size
                result.paste(img, (x, y, x + w, y + h))
            j += 1
            i = 0
            images_to_add = {}
            result.save(os.path.expanduser("badges_output/image"+str(j)+".jpg"))
        else:
            i += 1

def letters_width():
    letters = {"A": 26,"B": 24,"C": 31,"D": 30,"E": 24,"F": 24,"G": 33,"H": 28,"I": 12,"J": 24,
               "K": 28,"L": 22,"M": 33,"N": 30,"O": 35,"P": 24,"Q": 35,"R": 26,"S": 27,"T": 26,
               "U": 33,"V": 30,"W": 46,"X": 30,"Y": 25,"Z": 22, " ": 12, "-": 16}
    return letters


def read_badge_template(badge_path="badge_template.png"):
    pattern = Image.open(badge_path, "r").convert('RGBA')
    return pattern


def read_members_list(list_path = "omc_list.csv"):
    file = open(list_path, "r")
    list_members = []
    file.readline()
    for line in file:
        member = Member(line)
        list_members.append(member)
    return list_members


def get_word_width(word):
    list_letters = letters_width()
    width = 0
    for letter in word:
        width += list_letters[letter]
    return width


def write_infos_on_badge(member, badge):
    fname, faname, id = member.get_infos()
    badge = read_badge_template()
    width, height = badge.size
    font_size = 40
    fname_width = width/2 - get_word_width(fname.upper())/2
    faname_width = width/2 - get_word_width(faname.upper())/2
    f = ImageFont.truetype("fonts/qsl.ttf", font_size)
    f_id = ImageFont.truetype("fonts/qs.ttf", font_size)
    badge_writter = ImageDraw.Draw(badge)
    badge_writter.text((fname_width, 750), fname.upper(), font=f, fill=(0,0,0))
    badge_writter.text((faname_width, 800), faname.upper(), font=f, fill=(0,0,0))
    badge_writter.text((170, 850), id, font=f_id, fill=(0,0,0))
    badge_path = "badges/"+id+".png"
    badge.save(badge_path)


init_badges_directory()
badge = read_badge_template()
list_members = read_members_list()
for member in list_members:
    write_infos_on_badge(member, badge)
combine_badges()
