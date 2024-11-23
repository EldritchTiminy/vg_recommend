# V.G. List
# These functions are for turning lists of results into printed out threads.

from vgtext import prompts

def ltm(imp_list): #L.T.M. = List Thread Maker -> Turns a list of results into a thread list sentence.
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

def rtl(imp_list, genre): #R.T.L. = Result Thread Lister -> Presents video game search results.
  #pass
  print(prompts[6].format(G = genre))
  for result in imp_list:
    print(prompts[7].format(A = result[1], B = result[2], C = result[3]))