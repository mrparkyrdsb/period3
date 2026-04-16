# Recursion
# Exponentiation
# Base Case
def power(base, exponent):
    if base == 0 and exponent == 0:
        return 1
    elif base == 0 or base == 1:
        return base
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        # write recursion here
        return base * power(base, exponent-1)

# PALINDROME
# words that are spelt the same forwards and backwards
# return true if the given string is a palindrome
def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif len(word) <= 3:
        return word[0] == word[-1]
    else:
        if word[0] != word[-1]:
            return False
        else:
            # word[1:len(word)-1]
            print(word, word[1:-1])
            return True and is_palindrome(word[1:-1])

def reverse_str(word):
    def helper(text, result="", i=-1):
        if i == (-1 * len(text)):
            return result + text[i]
        else:
            return helper(text, result + text[i], i - 1)

    # Base Case 1&2-> Single and empty
    if len(word) <= 1:
        return word
    else:
        return helper(word)

print(reverse_str("Park"))

def maximum(array):
    def helper(arr, largest, i=1):
        if i >= len(arr):
            return largest
        else:
            if arr[i] > largest:
                return helper(arr, arr[i], i+1)
            else:
                return helper(arr, largest, i+1)
    # end of helper()
    if not array:
        return None
    elif len(array) == 1:
        return array[0]
    else:
        return helper(array, array[0])

def maximum2(array):
    if not array:
        return None
    elif len(array) == 1:
        return array[0]
    else:
        # uhoh WTF do I do here?
        largest = array[0]
        if largest > maximum2(array[1:]):
            return largest
        else:
            return maximum2(array[1:])

def mergeIt(arr1, arr2):
    if not arr1 and not arr2:
        return []
    elif not arr1:
        return arr2
    elif not arr2:
        return arr1
    else:
        # code here
        if arr1[0] < arr2[0]:
            return [arr1[0]] + mergeIt(arr1[1:], arr2)
        else:
            return [arr2[0]] + mergeIt(arr1, arr2[1:])

print(mergeIt([1,3,5], [2,4,6]))

def mergeIt2(arr1, arr2):
    def helper(array1, array2, result=[], i=0, j=0):
        if i >= len(array1) and j >= len(array2):
            return result
        elif j < len(array2):
            return result + array2[j:]
        elif i < len(array1):
            return result + array1[i:]
        else:
            if array1[i] < array2[j]:
                return helper(array1, array2, result+[array1[i]], i+1, j)
            else:
                return helper(array1, array2, result+[array2[j]], i, j+1)

    if not arr1 and not arr2:
        return []
    elif not arr1:
        return arr2
    elif not arr2:
        return arr1
    else:
        return helper(array1, array2)

def primeFactors(num, divider=2):
    if num == 1:
        return []
    elif num % divider == 0:
        return [divider] + primeFactors(num//divider, divider)   
    else:
        return primeFactors(num, divider + 1)

print(primeFactors(90))