#Listing Functions for VGR

#from vgdata import types, video_games
from vgtext import prompts

def ltm(imp_list): #L.T.M. = List Thread Maker
  list_thread = ""
  imp_list_c = imp_list[:]
  imp_list_c.reverse()
  while len(imp_list_c) > 1:
    current_el = imp_list_c.pop()
    new_el = current_el + ", "
    list_thread += new_el
  current_el = imp_list_c.pop()
  new_el = "and " + current_el + "."
  list_thread += new_el
  return list_thread

#print(ltm(types))

def rtl(imp_list, genre): #R.T.L. = Result Thread Lister
  #pass
  print(prompts[6].format(G = genre))
  for result in imp_list:
    print(prompts[7].format(A = result[2], B = result[3], C = result[4]))