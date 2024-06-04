# Video Game Recommender (VGR)

# Program Skeleton:
# Primary Program Loop
#   - Get input from user (maybe offer lists of possibilities)
#   - Search 'types' for input
#   - if input exists:
#     - Get input from user
#     - if user interested in genre:
#       - Search 'video_games' for original input
#       - List findings

from vgdata import types, video_games
from vgsearch import vgs, gsearch, ipl
game_on = True

while game_on == True:
  print("""
  
  
Welcome to Video Game Recommender!

Please input a letter and press 'Enter' to search for video game genres.
(Your search query should be in all lowercase letters.)

To select from a list instead, please type 'list' and press 'Enter'.
""")
  input_1 = input("Please type a letter, word, or 'list' and press 'Enter': ")
  print(vgs(input_1))
  game_on = False