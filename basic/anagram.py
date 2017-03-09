# they are made up of symbols from the 
# set of 26 lowercase alphabetic characters
# output True / False


def anagramSolution1(s1, s2):
    s1 = "".join(sorted(s1))
    s2 = "".join(sorted(s2))
    return s1 == s2


def anagramSolution2(s1, s2):
    alist = list(s2)

    stillOK = True
    pos1 = 0

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            # print("pos1:{},s1[pos1]:{}, pos2:{},s2[pos2]:{}".format(pos1, s1[pos1], pos2, alist[pos2]))
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1
    return stillOK


def anagramSolution3(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)
    
    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos < len(alist1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches


def anagramSolution4(s1, s2):
    c1 = [0]*26
    c2 = [0]*26
    
    for i in range(len(s1)):
        i = ord(s1[i]) - ord("a")
        c1[i] = c1[i] + 1

    for i in range(len(s2)):
        i = ord(s2[i]) - ord("a")
        c2[i] = c2[i] + 1
    
    stillOK = True
    pos = 0

    while pos < 26 and stillOK:
        if c1[pos] == c2[pos]:
            pos = pos + 1
        else:
            stillOK = False

    return stillOK
        

def main():
    s1 = "ab"
    s2 = "ba"
    print(anagramSolution4(s1, s2))


main()
