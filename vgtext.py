# V.G. Text
# This is a file that contains all of the text prompts, separated for code readability.

intro = """
  
  
Welcome to Video Game Recommender!

Please input a letter and press 'Enter' to search for video game genres.
(Your search query should be in all lowercase letters.)

To select from a list instead, please type 'list' and press 'Enter'.

To quit the program input 'q' whenever prompted for an input.


"""

list_prompt = """



===============================================
You can choose from the following list options:

{L}


"""#.format(L = ltm(types))

search_res = """



==============================================
Here are the categories that start with "{S}":


{R}


"""

confirm_prompt = """



================================================================================================
If you would like to see recommendations for one of your search results, please type the result.

To search for something else, type "n".

To quit the program, type "q".


"""

error_code = """


==================================
Looks like something went wrong...

Please try again.


"""

no_res = """


==========================
We didn't find anything...


"""

vg_results = """
=================================================================
Here are the video games that we recommend under the {G} genre...

"""


video_game_result = """
Video Game: {A}
Developer:  {B}
Reviews:    {C}

"""#.format(A = result[2], B = result[3], C = result[4])

#Quick reference list for calling these threads.
prompts = [intro, list_prompt, search_res, confirm_prompt, error_code, no_res, vg_results, video_game_result]