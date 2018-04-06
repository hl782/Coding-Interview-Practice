# Chapter 1 - Arrays & Strings

#Problem 1 - Is Unique
def isUnique(s1):
    sorted_s1 = ''.join(sorted(s1.lower()))
    for x in range(0, len(sorted_s1)):
        if sorted_s1[x] == sorted_s1[x-1]:
            return False
    return True

#Problem 2 - Permutations

def permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        sorted_s1 = ''.join(sorted(s1.lower()))
        sorted_s2 = ''.join(sorted(s2.lower()))
        if sorted_s1 == sorted_s2:
            return True
        else:
            return False



#Main Function
def main():
    # print isUnique('abcde')
    # print isUnique('abece')
    # print isUnique('ABcDb')
    #
    # print permutation('abcde', 'dbcea')

if __name__ == "__main__":
    main()
