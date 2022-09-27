import json
from PIL import Image, ImageDraw, ImageFont

NAME_FONT_SIZE = 200
NAME_FONT = ImageFont.truetype(
    "./font/ITC Avant Garde Gothic Std Book.otf", NAME_FONT_SIZE
)

DESC_FONT_SIZE = 85
DESC_FONT = ImageFont.truetype(
    "./font/ITC Avant Garde Gothic Std Book.otf", DESC_FONT_SIZE
)


def add_beers(json_file, image):
    y_pos_beer = 1600
    for beer in json_file["beers"]:
        image.text(
            (950, y_pos_beer),
            beer["name"],
            fill="white",
            font=NAME_FONT,
            anchor="lm",
        )

        image.text(
            (3750, y_pos_beer),
            beer["price"] + "€",
            fill="white",
            font=NAME_FONT,
            anchor="rm",
        )
        y_pos_beer += 225


def add_cokctails(json_file, image):
    y_pos_cocktail = 2950
    x_pos_coktail_name = 950

    for cocktail in json_file["cocktails"]:
        image.text(
            (x_pos_coktail_name, y_pos_cocktail),
            cocktail["name"],
            fill="white",
            font=NAME_FONT,
            anchor="lm",
        )

        image.text(
            (
                NAME_FONT.getlength(cocktail["name"]) + x_pos_coktail_name + 25,
                y_pos_cocktail,
            ),
            cocktail["desc"],
            fill="white",
            font=DESC_FONT,
        )

        image.text(
            (3750, y_pos_cocktail),
            cocktail["price"] + "€",
            fill="white",
            font=NAME_FONT,
            anchor="rm",
        )

        y_pos_cocktail += 225


def add_wines(json_file, image):
    y_pos_wine = 1600

    for wine in json_file["wines"]:
        image.text(
            (4000, y_pos_wine),
            wine["name"],
            fill="white",
            font=NAME_FONT,
            anchor="lm",
        )

        image.text(
            (7100, y_pos_wine),
            wine["price"] + "€",
            fill="white",
            font=NAME_FONT,
            anchor="rm",
        )

        y_pos_wine += 225


def add_mocktails(json_file, image):
    y_pos_mocktail = 2950
    x_pos_mocktail_name = 4000

    for mocktail in json_file["mocktails"]:
        image.text(
            (x_pos_mocktail_name, y_pos_mocktail),
            mocktail["name"],
            fill="white",
            font=NAME_FONT,
            anchor="lm",
        )

        image.text(
            (
                NAME_FONT.getlength(mocktail["name"]) + x_pos_mocktail_name + 25,
                y_pos_mocktail,
            ),
            mocktail["desc"],
            fill="white",
            font=DESC_FONT,
        )

        image.text(
            (7100, y_pos_mocktail),
            mocktail["price"] + "€",
            fill="white",
            font=NAME_FONT,
            anchor="rm",
        )
        y_pos_mocktail += 225


def main():

    image_menu = Image.open("menu.png")
    image = ImageDraw.Draw(image_menu)

    with open("menu.json") as menu:
        menu = json.load(menu)

        add_beers(menu, image)
        add_cokctails(menu, image)
        add_wines(menu, image)
        add_mocktails(menu, image)

    # 8K to 4K
    image_menu = image_menu.resize((image_menu.width // 2, image_menu.height // 2))
    image_menu.save("menu_output.png")


if __name__ == "__main__":
    main()
