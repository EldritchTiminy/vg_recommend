# V.G. Search
# Based on the recursive binary search model.
# This script tests the search input for length, then searches the input list for entries that match the search input.

from vgdata import types

def ipl(slist, imp): #ipl ("input list") cuts down list elements to the same length as input for easier searching.
  impl = len(imp)
  #nslist = [element[:impl] for element in slist if len(element) > impl]
  nslist = [element[:impl] if len(element) > impl else element for element in slist]
  #print(nslist)
  return nslist

def gsearch(sorted_list, left_pointer, right_pointer, target):
  # this condition indicates we've reached an empty "sub-list"
  if left_pointer >= right_pointer:
    return "value not found"
	
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

def vgs(imp):
  slist = ipl(types, imp) #list of elements cut down to length of 'imp'
  lpoint = 0
  rpoint = len(slist)-1
  result = gsearch(slist, lpoint, rpoint, imp)
  return result
  

#ipl(types, "Acti") #ipl test
#vgs("Com") #vgs test