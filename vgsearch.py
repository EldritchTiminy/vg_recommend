# V.G. Search
# Based on the recursive binary search model.
# This script tests the search input for length, then searches the input list for entries that match the search input.

from vgdata import types, video_games

def ipl(slist, imp): #ipl ("input list") cuts down list elements to the same length as input for easier searching.
  impl = len(imp)
  #nslist = [element[:impl] for element in slist if len(element) > impl]
  nslist = [element[:impl] if len(element) > impl else element for element in slist]
  #print(nslist)
  return nslist

def gsearch(sorted_list, left_pointer, right_pointer, target): #function for searching through a list for a target value
  # this condition indicates we've reached an empty "sub-list"
  if left_pointer >= right_pointer:
    return None
	
  # We calculate the middle index from the pointers now
  mid_idx = (left_pointer + right_pointer) // 2
  mid_val = sorted_list[mid_idx]
  
  if mid_val == target:
    return mid_idx
    
  if mid_val > target:
    # we reduce the sub-list by passing in a new right_pointer
    return gsearch(sorted_list, left_pointer, mid_idx, target)
    
  if mid_val < target:
    # we reduce the sub-list by passing in a new left_pointer
    return gsearch(sorted_list, mid_idx + 1, right_pointer, target)

def vgs(imp, sorted_list=types, found=[]):
  slist = ipl(sorted_list, imp) #list of elements cut down to length of 'imp'
  #print(slist)
  found = found
  results_list = []
  lpoint = 0
  rpoint = len(slist)-1
  result_idx = gsearch(slist, lpoint, rpoint, imp)
  #result = slist[result_idx]
  if result_idx == None:
    return results_list
  else:
    result = slist.pop(result_idx)
    slist.insert(result_idx, "0")
    results = vgs(imp, slist, found)
    return results + [types[result_idx]]
  #return result_idx, result

def vgts(imp, sorted_list=video_games): #(vgts = video game title search)
  #this function searches for individual titles of the searched genre
  results = []
  for game in sorted_list:
    if game[0] == imp:
      results += [game]
  return results
  
  

#ipl(types, "Acti") #ipl test
#vgs("Com", types) #vgs test