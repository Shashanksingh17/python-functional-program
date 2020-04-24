def permutation(lst):

    if len(lst) == 0:  # If lst is empty then there are no permutations
        return []


    if len(lst) == 1:   # If there is only one element in lst then, only
        return [lst]    # one permuatation is possible

    l = []  # empty list that will store current permutation

    for i in range(len(lst)):  # Iterate the input(lst) and calculate the permutation
        m = lst[i]

        remLst = lst[:i] + lst[i + 1:]   # Extract lst[i] or m from the list.  remLst is  # remaining list

        for p in permutation(remLst):          # Generating all permutations where m is first element
            l.append([m] + p)
    return l


# Driver program to test above function
data = list('abc')
for p in permutation(data):
    print(p)
