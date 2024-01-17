# a function that takes a list and a target parameter
# multiple variables: middle, start, end, steps
# recursion or while loop
# increase the step each time a split is done
# conditions to truck target position
def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 1

    while(start <= end):
        print("Steps",steps,": ",str(list[start:end+1]), '\n')

        steps = steps+1
        middle= (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle-1
        else:
            start = middle+1
    return -1

my_list = list(range(1, 1001))
target = 999
binary_search(my_list, target)