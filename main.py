from Deck import Deck
from Hand import Hand
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from Card import Card
# deck1 = Deck()
# hand1 = Hand()
# poker_game = []
# five_card = deck1.deal_card()
# for i in five_card:
#     .add_card(i)
# for i in hand1.get_hand():
#     print(i.get_value())


def get_row(im1, im2, im3, im4, im5):
    new_image = Image.new('RGB', (im1.width * 6, im1.height))
    new_image.paste(im1, (0, 0))
    new_image.paste(im2, (im1.width, 0))
    new_image.paste(im3, (im1.width * 2, 0))
    new_image.paste(im4, (im1.width * 3, 0))
    new_image.paste(im5, (im1.width * 4, 0))
    return new_image


def get_column(im1, im2, im3, im4):
    new_image = Image.new('RGB', (im1.width, im1.height * 4))
    new_image.paste(im1, (0, 0))
    new_image.paste(im2, (0, im1.height))
    new_image.paste(im3, (0, im1.height * 2))
    new_image.paste(im4, (0, im1.height * 3))
    return new_image


poker_game = []
my_deck = Deck()
hand1 = Hand()
poker_game.append(hand1)
hand2 = Hand()
poker_game.append(hand2)
hand3 = Hand()
poker_game.append(hand3)
hand4 = Hand()
poker_game.append(hand4)

for j in range(5):
    for i in poker_game:
        i.add_card(my_deck.deal_card())

row1 = get_row(Image.open(hand1.get_hand()[0].image_file_name()), Image.open(hand1.get_hand()[1].image_file_name()),
               Image.open(hand1.get_hand()[2].image_file_name()), Image.open(hand1.get_hand()[3].image_file_name()),
               Image.open(hand1.get_hand()[4].image_file_name()))
row2 = get_row(Image.open(hand2.get_hand()[0].image_file_name()), Image.open(hand2.get_hand()[1].image_file_name()),
               Image.open(hand2.get_hand()[2].image_file_name()), Image.open(hand2.get_hand()[3].image_file_name()),
               Image.open(hand2.get_hand()[4].image_file_name()))
row3 = get_row(Image.open(hand3.get_hand()[0].image_file_name()), Image.open(hand3.get_hand()[1].image_file_name()),
               Image.open(hand3.get_hand()[2].image_file_name()), Image.open(hand3.get_hand()[3].image_file_name()),
               Image.open(hand3.get_hand()[4].image_file_name()))
row4 = get_row(Image.open(hand4.get_hand()[0].image_file_name()), Image.open(hand4.get_hand()[1].image_file_name()),
               Image.open(hand4.get_hand()[2].image_file_name()), Image.open(hand4.get_hand()[3].image_file_name()),
               Image.open(hand4.get_hand()[4].image_file_name()))
my_picture = get_column(row1, row2, row3, row4)


winner = []
winner.append(hand1)
if winner[0].compare(hand2) == -1:
    winner.clear()
    winner.append(hand2)
if winner[0].compare(hand2) == 0:
    winner.append(hand2)
if winner[0].compare(hand3) == -1:
    winner.clear()
    winner.append(hand3)
if winner[0].compare(hand3) == 0:
    winner.append(hand3)
if winner[0].compare(hand4) == -1:
    winner.clear()
    winner.append(hand4)
if winner[0].compare(hand4) == 0:
    winner.append(hand4)
the_winner = "Winner!"
my_draw = ImageDraw.Draw(my_picture)
my_font = ImageFont.truetype('Arial', 13)
winner_font = ImageFont.truetype('Arial', 25)
my_draw.text((my_picture.width - 90, 75), hand1.get_hand_type(), font=my_font, fill=(255, 255, 255))
my_draw.text((my_picture.width - 90, 215), hand2.get_hand_type(), font=my_font, fill=(255, 255, 255))
my_draw.text((my_picture.width - 90, 360), hand3.get_hand_type(), font=my_font, fill=(255, 255, 255))
my_draw.text((my_picture.width - 90, 505), hand4.get_hand_type(), font=my_font, fill=(255, 255, 255))

if hand1 in winner:
    my_draw.text((my_picture.width - 90, 90), the_winner, font=winner_font, fill=(255, 0, 0))
if hand2 in winner:
    my_draw.text((my_picture.width - 90, 230), the_winner, font=winner_font, fill=(255, 0, 0))
if hand3 in winner:
    my_draw.text((my_picture.width - 90, 375), the_winner, font=winner_font, fill=(255, 0, 0))
if hand4 in winner:
    my_draw.text((my_picture.width - 90, 520), the_winner, font=winner_font, fill=(255, 0, 0))
my_picture.show()












