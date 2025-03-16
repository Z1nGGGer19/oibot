import datetime
from Google_sheets.manager_sheets import input_value_sheet
from PIL import Image, ImageDraw


async def input_date(date):
    try:
        date_format = "%d.%m.%Y"
        datetime.datetime.strptime(date, date_format)
        input_value_sheet(date)

        return "succes"
    
    except ValueError:
        return "error"


async def generate_image(weeks):
    sq_size = 20
    cols = 52
    rows = (weeks // cols) + 1

    image = Image.new('RGB', (cols * sq_size, rows * sq_size), 'white')
    draw = ImageDraw.Draw(image)

    for i in range(weeks):
        x = (i % cols) * sq_size
        y = (i // cols) * sq_size
        draw.rectangle([x, y, x + sq_size - 1, y + sq_size - 1], fill='black')

    return image
