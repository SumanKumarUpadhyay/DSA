# balloons problem to count how many balloons can be formed from a given string in python
def maxNumberOfBalloons(text: str) -> int:
    # create a hash map to store the count of each character in the text 
    hm = {}
    for char in text:
        if char in hm:
            hm[char] += 1
        else:
            hm[char] = 1

    # check required letters for balloon
    b = hm.get('b', 0)
    a = hm.get('a', 0)
    l = hm.get('l', 0)//2
    o = hm.get('o', 0)//2
    n = hm.get('n', 0)

    # calculate the maximum number of balloons that can be formed
    return min(b, a, l, o, n)
text = "loonbalxballpoon"
print(maxNumberOfBalloons(text)) 
