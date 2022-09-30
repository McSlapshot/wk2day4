#Given an array of strings and n (integer), 
#return a dictionary of ascending ordered random 'teams' or groupings of n size.
#any remainders should be in the last 'team'.
#function should return different 'teams' each time called.

ex_list = ['one', 'two', 'three', 'four', 'five']
#returns (n=2): 
# {1: ['two', 'five'], 2: ['three', 'one'], 3: ['four']}
ex_list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
#returns (n=5): 
# {1: ['one', 'five', 'two', 'four', 'nine'], 2: ['ten', 'three', 'seven', 'six', 'eight']}
ex_list3 = ['Aaron', 'Bridget', 'Caroline', 'Derek', 'Elaine']
#returns (n=2): 
# {1: ['Bridget', 'Caroline'], 2: ['Aaron', 'Elaine'], 3: ['Derek']}
def generateTeam(people, size):
    teams = {}

    return