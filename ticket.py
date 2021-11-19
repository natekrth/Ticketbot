import csv
from PIL import Image, ImageFont, ImageDraw

ticket_data = []
with open('Audience Application (Responses) - Guest Tickets.csv') as file:
    rows = csv.DictReader(file)
    for r in rows:
        ticket_data.append(r)


count = 1
for person in ticket_data:
    my_image = Image.open("tickets.png")
    name = person["ชื่อ-สกุล  "]
    ticket_num = person["Ticket No."]

    image_editable = ImageDraw.Draw(my_image)
    title_font = ImageFont.truetype('FC Subject Rounded Regular [Non-commercial use].ttf', 40)
    image_editable.text((1175,165), ticket_num, (255, 57, 15), font=title_font)Í

    if len(name) > 30:
        title_font = ImageFont.truetype('FC Subject Rounded Regular [Non-commercial use].ttf', 20)
        image_editable.text((1160, 420), name, (255, 57, 15), font=title_font)
    elif len(name) > 20:
        title_font = ImageFont.truetype('FC Subject Rounded Regular [Non-commercial use].ttf', 23)
        image_editable.text((1166, 420), name, (255, 57, 15), font=title_font)
    elif len(name) > 15:
        title_font = ImageFont.truetype('FC Subject Rounded Regular [Non-commercial use].ttf', 30)
        image_editable.text((1175, 420), name, (255, 57, 15), font=title_font)
    else:
        title_font = ImageFont.truetype('FC Subject Rounded Regular [Non-commercial use].ttf', 40)
        image_editable.text((1175, 400), name, (255, 57, 15), font=title_font)

    my_image.save(f"Guest ticket{count}.png")
    print(f"Guest ticket{count}.png")
    count += 1