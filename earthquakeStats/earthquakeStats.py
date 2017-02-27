# takes the dictionary and prints its contents to the screen
# sorted by the key
def frequencyTable(countdict):
    
    print("ITEM", "\t", "FREQUENCY")

    ## print the dictionary sorted by the key
    list = countdict.items()
    list = sorted(list);
    for i in list :
        print(i[0], "\t", i[1])
        

# takes a list of numbers and an empty dictionary
# builds the dictionary with earthquake frequencies
# returns a mode 
def mode(alist, countdict):

    ## iterate over alist and build a dictionary called countdict
    ## to store the frequency of each value in alist
    for i in alist :
        if i in countdict :
            count = countdict[i]
            countdict[i] = count + 1
        else :
            countdict[i] = 1;

    ## find the highest value in a value componet of the dictionary
    maxcount = max(countdict.values())
    
    modelist = [ ]      ## creates a list of modes since there may be more than one mode
    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)
    
    return modelist

# takes a list of numbers and returns a median value
def median(alist):
    # deep copy of a list and then sort the copy
    newlist = alist[:]
    newlist = sorted(newlist)

    length = len(newlist)
    if length%2 is not 0 :
        ## find the median value - middle value if the length odd
        medianValue = newlist[length // 2]
    else :
        ## average of 2 middle values otherwise
        middleOne = newlist[length // 2]
        middleTwo = newlist[(length // 2) + 1]
        median = (middleOne + middleTwo) / 2

    return median

# this function is complete
# opens a file and extracts all earthquake magnitudes
# into a list and returns that list
def makeMagnitudeList():
        quakefile = open("earthquakes.txt","r")
        headers = quakefile.readline()
        
        maglist = [ ]
        for aline in quakefile:
            vlist = aline.split()
            maglist.append(float(vlist[1]))
        return maglist
# Driver
def my_main():
    magList = makeMagnitudeList()
    ## print(magList)
    ## print mean (use built in functions sum and len)
    print("mean: ", (sum(magList) / len(magList)))
    frequencyDict = {}
    med = median(magList)
    print("median: ", med)
    mod = mode(magList, frequencyDict)
    print("mode: ", mod)
    frequencyTable(frequencyDict)

        
if __name__ == '__main__':
        my_main()

