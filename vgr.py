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

# To-do:
# DONE - 1. refine search. needs to return more than just one option. For instance if we just search for 'c' it should return 'crpg' and 'comedy' as possible option suggestions.
# DONE - 2. Need to create actual list function for users to see possible options from the main menu.
# DONE - 3. Return the initial search answer as a naked string instead of a string in an isolated list.
# DONE - 4. Ask the user if that was what they were looking for.
# DONE - 5. Move text prompts to seperate file for readability.
# DONE - 6. Fix blank search "max recursion" error.
# DONE - 7. Secondary search for search result category. Return all games withing category.
# DONE - 8. Add 'quit' function.


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
    #print(vgs(input_1))
    #game_on = False
    print(prompts[3])
    
    input_2 = input("Please type 'n', 'q', or type in a search result: ")
    
    if input_2 == "n":
      continue
      
    elif input_2 == "q":
      game_on = False
      continue
      
    else:
      #pass #put secondary search function here
      result = vgts(input_2)
      #print(result)
      rtl(result, input_2)
      input("Please press 'Enter' to continue...")