# Video Game Recommender (VGR)
# This is the main program

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
from vgsearch import vgs, gsearch, ipl, vgts
from vglist import ltm, rtl
from vgtext import prompts
game_on = True

while game_on == True:
  print(prompts[0])
  while game_on == True:
    input_1 = input("Please type a letter, word, or 'list' and press 'Enter': ")
    if input_1 == "list":
      print(prompts[1].format(L = ltm(types)))
      continue
    elif input_1 == "":
      continue
    elif input_1 == "q":
      game_on = False
      continue
    else:
      result = vgs(input_1)
      if len(result) > 1:
        R = ltm(result)
      elif len(result) < 1:
        R = prompts[5]
      else:
        R = result[0]
      print(prompts[2].format(S = input_1, R = R))
    input("Please press 'Enter' to continue...")
    print(prompts[3])
    input_2 = input("Please type 'n', 'q', or type in a search result: ")
    if input_2 == "n":
      continue
    elif input_2 == "q":
      game_on = False
      continue
    else:
      result = vgts(input_2)
      rtl(result, input_2)
      input("Please press 'Enter' to continue...")