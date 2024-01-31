""" ----------------------------------------------------------------------------
******** Search Code for DFS and other search methods
******** Κώδικας για DFS και άλλες μεθόδους αναζήτησης
"""

import copy
import sys

sys.setrecursionlimit(8**6)

# ******** Operators
# ******** Τελεστές

# Μεταφορά ενοίκων από τον όροφο 1 στον ασανσέρ
def go_to_floor1(state):
    # Αν ο αριθμός των ενοίκων είναι μεγαλύτερος από τον διαθέσιμο χώρο στον ασανσέρ, μεταφέρονται μόνο οι διαθέσιμοι.
    if state[-1] < 8 and state[1] > 0:
        if state[1] > 8 - state[-1]:
            new_state = [1] + [state[1] + state[-1] - 8] + [state[2]] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [1] + [0] + [state[2]] + [state[3]] + [state[4]] + [state[1] + state[-1]]
        return new_state

# Αντίστοιχες συναρτήσεις για τους υπόλοιπους ορόφους
# go_to_floor2, go_to_floor3, go_to_floor4
def go_to_floor2(state):
    if state[-1] < 8 and state[2] > 0:
        if state[2] > 8 - state[-1]:
            new_state = [2] + [state[1]] + [state[2] + state[-1] - 8] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [2] + [state[1]] + [0] + [state[3]] + [state[4]] + [state[2] + state[-1]]
        return new_state
    
def go_to_floor3(state):
    if state[-1] < 8 and state[3] > 0:
        if state[3] > 8 - state[-1]:
            new_state = [3] + [state[1]] + [state[2]] + [state[3] + state[-1] - 8] + [state[4]] + [8]
        else:
            new_state = [3] + [state[1]] + [state[2]] + [0] + [state[4]] + [state[3] + state[-1]]
        return new_state 
    
def go_to_floor4(state):
    if state[-1] < 8 and state[4] > 0:
        if state[4] > 8 - state[-1]:
            new_state = [4] + [state[1]] + [state[2]] + [state[3]] + [state[4] + state[-1] - 8] + [8]
        else:
            new_state = [4] + [state[1]] + [state[2]] + [state[3]] + [0] + [state[4] + state[-1]]
        return new_state

# Βρίσκει τις πιθανές καταστάσεις-παιδιά από μια δεδομένη κατάσταση
def find_children(state):
    children = []

    floor1_state = copy.deepcopy(state)
    floor1_child = go_to_floor1(floor1_state)
    if floor1_child is not None:
        children.append(floor1_child)

    # Προσθήκη παιδιών για τους υπόλοιπους ορόφους

    floor2_state = copy.deepcopy(state)
    floor2_child = go_to_floor2(floor2_state)
    if floor2_child is not None:
        children.append(floor2_child)

    floor3_state = copy.deepcopy(state)
    floor3_child = go_to_floor3(floor3_state)
    if floor3_child is not None:
        children.append(floor3_child)
    
    floor4_state = copy.deepcopy(state)
    floor4_child = go_to_floor4(floor4_state)
    if floor4_child is not None:
        children.append(floor4_child)   
        
    return children

""" ----------------------------------------------------------------------------
**** FRONT
**** Διαχείριση Μετώπου / Ευριστική: Αναζητώ πάντα τον όροφο με τους περισσότερους ένοικους
"""
# Βρίσκει την κατάσταση με τους περισσότερους ενοίκους από μια λίστα καταστάσεων
def find_most_people(front):
    max = -1
    for i in front:
        if i[-1] > max:
            max = i[-1]
            res = i
    return res

""" ----------------------------------------------------------------------------
** initialization of front
** Αρχικοποίηση Μετώπου
"""
# Αρχικοποίηση του μετώπου με την αρχική κατάσταση
def make_front(state):
    return [state]

""" ----------------------------------------------------------------------------
**** expanding front
**** επέκταση μετώπου    
"""
# Επεκτείνει το μέτωπο με βάση τη μέθοδο αναζήτησης
def expand_front(front, method):
    if method == 'DFS':
        if front:
            print("Front:")
            print(front)
            node = front.pop(0)
            if node[-1] == 8 or node[1] + node[2] + node[3] + node[4] == 0:
                node[-1] = 0
                node[0] = 5
                front.insert(0, node)
            else:
                for child in find_children(node):
                    front.insert(0, child)
    elif method == 'BFS':
        if front:
            print("Front:")
            print(front)
            node = front.pop(0)
            if node[-1] == 8 or node[1] + node[2] + node[3] + node[4] == 0:
                node[-1] = 0
                node[0] = 5
                front.append(node)
            else:
                for child in find_children(node):
                    front.append(child)
    elif method == 'BESTFS':
        if front:
            print("Front:")
            print(front)
            node = front.pop(0)
            front = []
            if node[-1] == 8 or node[1] + node[2] + node[3] + node[4] == 0:
                node[-1] = 0
                node[0] = 5
                front.append(node)
            else:
                for child in find_children(node):
                    front.append(child)

        temp = copy.deepcopy(front)
        lead = find_most_people(temp)
        front.remove(lead)
        front.insert(0, lead)

    return front


""" ----------------------------------------------------------------------------
**** QUEUE
**** Διαχείριση ουράς
"""

""" ----------------------------------------------------------------------------
** initialization of queue
** Αρχικοποίηση ουράς
"""
# Αρχικοποίηση της ουράς με την αρχική κατάσταση
def make_queue(state):
    return [[state]]


""" ----------------------------------------------------------------------------
**** expanding queue
**** επέκταση ουράς
"""

# Επεκτείνει την ουρά με βάση τη μέθοδο αναζήτησης
def extend_queue(queue, method, bestfs_state):
    if method == 'DFS':
        print("Queue:")
        for i in queue:
            print(i)
        node = queue.pop(0)
        queue_copy = copy.deepcopy(queue)
        path = copy.deepcopy(node)

        last = copy.deepcopy(node[-1])
        if last[-1] == 8 or last[1] + last[2] + last[3] + last[4] == 0:
            last[-1] = 0
            last[0] = 5
            path = copy.deepcopy(node)
            path.append(last)
            queue_copy.insert(0, path)
        else:
            children = find_children(node[-1])
            for child in children:
                path = copy.deepcopy(node)
                path.append(child)
                queue_copy.insert(0, path)
    elif method == 'BFS':
        print("Queue:")
        for i in queue:
            print(i)
        node = queue.pop(0)
        queue_copy = copy.deepcopy(queue)
        path = copy.deepcopy(node)

        last = copy.deepcopy(node[-1])
        if last[-1] == 8 or last[1] + last[2] + last[3] + last[4] == 0:
            last[-1] = 0
            last[0] = 5
            path = copy.deepcopy(node)
            path.append(last)
            queue_copy.append(path)
        else:
            children = find_children(node[-1])
            for child in children:
                path = copy.deepcopy(node)
                path.append(child)
                queue_copy.append(path)
    elif method == 'BESTFS':
        print("Queue:")
        print(queue)
        queue_copy = copy.deepcopy(queue)
        queue_copy.append(bestfs_state)

    return queue_copy


""" ----------------------------------------------------------------------------
**** Basic recursive function to create search tree (recursive tree expansion)
**** Βασική αναδρομική συνάρτηση για δημιουργία δέντρου αναζήτησης (αναδρομική επέκταση δέντρου)
"""

# Βρίσκει τη λύση με βάση την επιλεγμένη μέθοδο αναζήτησης
def find_solution(front, queue, closed, goal, method):
    if not front:
        print('_NO_SOLUTION_FOUND_')

    elif front[0] in closed:
        new_front = copy.deepcopy(front)
        new_front.pop(0)
        new_queue = copy.deepcopy(queue)
        if(new_queue):
            new_queue.pop(0)
        find_solution(new_front, new_queue, closed, goal, method)

    elif front[0] == goal:
        print('_GOAL_FOUND_')
        print(front[0])
        print("The path was: ")
        if(method == 'BESTFS'):
            print(queue)
        else:
            print(queue[0])

    else:
        closed.append(front[0])
        front_copy = copy.deepcopy(front)
        front_children = expand_front(front_copy, method)
        queue_copy = copy.deepcopy(queue)
        queue_children = extend_queue(queue_copy, method, front_children[0])
        closed_copy = copy.deepcopy(closed)
        find_solution(front_children, queue_children, closed_copy, goal, method)

# Εκτυπώνει τα μονοπάτια από την ουρά
def print_queue_paths(path):
    print("Queue Paths:")
    for p in path:
        print(p)


"""" ----------------------------------------------------------------------------
** Executing the code
** κλήση εκτέλεσης κώδικα
"""

def main():
    # Αρχική κατάσταση
    initial_state = [0, 9, 4, 12, 7, 0]
    """ ----------------------------------------------------------------------------
    **** [όροφος ασανσέρ, ένοικοι 1ου, ένοικοι 2ου, ένοικοι 3ου, ένοικοι 4ου, άτομα στο ασανσέρ]
    """
    # Στόχος προς επίτευξη
    goal = [5, 0, 0, 0, 0, 0]
    
    # Επιλογή μεθόδου αναζήτησης από τον χρήστη
    method = input("Choose method, DFS or BFS or BestFS\n")

    """ ----------------------------------------------------------------------------
    **** starting search
    **** έναρξη αναζήτησης
    """

    print('____BEGIN__SEARCHING____')
    
    # Κλήση της συνάρτησης αναζήτησης με τις αρχικές καταστάσεις
    find_solution(make_front(initial_state), make_queue(initial_state), [], goal, method.upper())


if __name__ == "__main__":
    main()
