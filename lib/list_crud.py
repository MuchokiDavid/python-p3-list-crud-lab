def create_an_empty_list():
    return []

def create_a_list():
    return ["Me","You", "Us", "We"]

def add_element_to_end_of_list(l, element):
    newlist= l.append(element)
    return newlist
old_list= create_a_list()
add_element_to_end_of_list(old_list, "Them")
# print(old_list)

def add_element_to_start_of_list(l, element):
    newlist= l.insert(0, element)
    return newlist
old_lists= create_a_list()
add_element_to_start_of_list(old_lists, "I")
print (old_lists)

def remove_element_from_end_of_list(l):
    newlist= l.pop()
    return newlist
rmv_list = create_a_list()
print(rmv_list)
# print(remove_element_from_end_of_list(rmv_list))

def remove_element_from_start_of_list(l):
    if len(l) > 0:
        del l[0]
    return l

def retrieve_first_element_from_list(l):
    element= l.pop(0)
    return element
print(retrieve_first_element_from_list(old_lists))

def retrieve_element_from_index(l, index):
    element= l[index]
    return element

def retrieve_last_element_from_list(l):
    element = l[-1]
    return element
print(retrieve_last_element_from_list(old_lists))
