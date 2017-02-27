import urllib.request, re, csv, operator
from tkinter import *



# takes a URL and opens it, scans it's source code
# for a title and returns the title
def getTitleFromURL(url) :
    #get the page text from the URL
    pageText = getPageText(url)
    #find <title>...</title> and remove html tags
    title = str(re.findall(r'<title>.*</title>', pageText, re.I))[9:-10]
    return title

# takes a string of an a href HTML attribute and
# extracts the title and returns it
def getTitleFromHTML(html) :
    # find the title and convert it to string
    title = str(re.findall(r'">[a-zA-Z0-9\s]*</a>', html, re.I))
    # remove extraneous characters
    title = title[4:-6]
    # return title
    return title

# takes a string of an a href HTML attribute and
# extracts the link and returns it
def getLinkFromHTML(html) :
    # find the link and convert it to string
    link = str(re.findall(r'"https?\S*">', html))
    # remove extraneous characters
    link = link[3:-4]
    # return the link
    return link

# takes the url of a webpage, opens it and converts its sourceand returns code as a string
def getPageText(url) :
    # attempt to collect information from the webpage
    try: page = urllib.request.urlopen(url)
    # catch any errors (404, etc)
    except urllib.error.URLError as e :
        # if the website has an error, return error message
        return "Error"
    else :
        # otherwise read the page and return its source code as a string
        pageText = str(page.read())
        return pageText

# takes the url of a webpage, opens it and converts its source
# code to a string. Finds all the links
# inside the text. Returns a list of tuples which are the links
# and their titles
def getURLsFromPage(url) :
    # get the source code text from the url
    pageText = getPageText(url)
    # create an empty tuple list of URL information (url, title)
    tupleListURLs = [ ]

    # if the website url is faulty or the page text is nonexistant
    if (not pageText) or (pageText == "Error"):
        # return the empty tuple list
        return (tupleListURLs)
    else :
        # otherwise search for all a href html attribute tags and their
        # associated URL and titles
        links = re.findall(r'<a href\s?=\s?"https?\S*>[a-zA-Z0-9\s]*</a>', pageText, re.I)
        # iterate through the links found
        for link in links :
            if checkAddressValidity(link) :
                # set up the title of the URL
                title = getTitleFromHTML(link)
                # set up the link to the URL
                url = getLinkFromHTML(link)
                # create a tuple (url, title) and add it to the list of link information
                tupleListURLs.append((url, title))
        # return the tuple list
        return (tupleListURLs)

def checkAddressValidity(link) :
    address = getLinkFromHTML(link)
    if address.endswith(".pdf") :
        return False
    return True


# takes a list of dictionaries and a url
# returns true if the list of dictionaries contains that url
# returns false if the list of dictionaries does not contain that url
def mainListContainsURL(mainList, url) :
    # iterate through the dictionaries in the list
    for dictionary in mainList :
        # if this website dictionary is the correct one
        if dictionary['URL'] == url :
            # return true
            return True
    # otherwise return false
    return False

# takes a list of dictionaries and a url
# if the list of dictionaries contains that url, update its references
# return the updated list
def updateDictionaryReferences(mainList, url) :
    # iterate through the dictionaries in the list
    for dictionary in mainList :
        # check if the current dictionary is the correct one
        if dictionary['URL'] == url :
            # if it is, increment the references for this website
            dictionary['References'] += 1
    # return the updated list
    return mainList

# take a list of dictionaries and a tuple of link information (url, title)
# create a new dictionary for that website and add it to the list
# return the updated list
def addNewDictionary(mainList, link) :
    # collect the title from the link information tuple
    title = link[1]
    # collect the url from the link information tuple
    url = link[0]
    # create a new dictionary
    newDictionary = {'Page': title, 'Links': [ ], 'References': 1, 'URL': url}
    # add the dictionary to the list
    mainList.append(newDictionary)
    # return the updated list
    return mainList

# take a list of dictionaries and a url
# return the title of the url page by iterating through dictionary
def getPageTitleFromDictionaryList(mainList, url) :
    # iterate through dictionaries in the list
    for dictionary in mainList :
        # if the current dictionary has the right url
        if dictionary['URL'] == url :
            # return the websites title
            return dictionary['Page']

# takes a list of links and a list of words
# adds words from link text to the list of words and returns
# an updated list of words
def collectWordsFromLinksToList(links, words) :
    # convert the list of links to a string
    links = str(links)
    # remove the 'http' or 'https' text
    links = re.sub(r'https?', "", links)
    # remove any possible domains (.****) where * may or may not be an alphanumeric character
    links = re.sub(r'\.[A-Za-z0-9]?[A-Za-z0-9]?[A-Za-z0-9]?[A-Za-z0-9]?/', "/", links)
    # split the link word text by any character that is not alphanumeric
    thewords = re.split(r'[^a-zA-Z\d]', links)
    # convert to string and remove brackets, apostrophes, and commas
    thewords = str(thewords).replace("[","").replace("]","").replace("'", "").replace(" ,", "")
    # split the words up by their spaces
    thewords = re.split(r'\s*,\s*', thewords)
    # remove beginning and ending entries to the list --- ('') and ('') ----
    thewords = thewords[1:-1]
    # iterate through the words in the link text
    for word in thewords :
        # add the word from the link text to the list of words
        words.append(word)
    # return an updated list of words
    return words

# takes a dictionary of words that consists of words as keys and their frequency as values
# collects the top 15 most frequent words (or if there are less than 15 words, all of them.
# returns a sorted list of the words with their frequencies
def getFifteenHighestValues(wordDictionary) :
    # sort the dictionary based on their values (reverse)
    values = sorted(wordDictionary.values(), reverse=True)
    # set the max number of words
    MAX = 15
    # create a counter
    counter = 0
    # create an empty list for the highest values
    highestValues = [ ]
    # iterate through the values 
    for value in values :
        # if we are within our max length
        if counter < MAX :
            # add the value to the list of highest values
            highestValues.append(value)
            # iterate the counter
            counter += 1

        # if we are at or over our max length
        else :
            # break out of this loop
            break

    # create an empty dictionary of words
    highestWordDictionary = {}
    # iterate through values in highest values
    for value in highestValues :
        # iterate through words in the word dictionary
        for word in wordDictionary :
            # if the word is equal to the value and it's not already in our highest word dictionary
            if wordDictionary[word] == value and word not in highestWordDictionary:
                # add it to the list of most frequent words
                highestWordDictionary[word] = value
    # sort the dictionary based on values
    sortedDictionary = sorted(highestWordDictionary.items(), key=operator.itemgetter(1), reverse = True)
    # return a sorted list of words and their frequency
    return sortedDictionary


# take a list of links and find the most frequently referenced webpage
# or if there is a tie, create a list of the most frequently referenced
# webpages. Return a 'list' with the text describing the results
def getReferenceList(mainList) :
    # set an initial reference count
    referenceCount = 0
    # create an empty list of most frequently referenced websites
    mostReferenced = []
    # set a flag to determine whether there is a tie
    tie = False
    # iterate through the websites in the list
    for dictionary in mainList :
        # if the current website has a higher reference count than the
        # current highest
        if dictionary['References'] > referenceCount :
            # break the tie (if it exists)
            tie = False
            # update the reference count
            referenceCount = dictionary['References']
            # update the most frequently referenced webpage
            mostReferenced = [dictionary['Page']]
        # if the current references are equal to the current reference count    
        elif dictionary['References'] == referenceCount :
            # there is a tie
            tie = True
            # add the current page to the list of most frequently referenced websites
            mostReferenced.append(dictionary['Page'])

    # convert the list to a string
    mostReferenced = str(mostReferenced)
    # remove the brackets and apostrophes
    mostReferenced = mostReferenced.replace("[", "")
    mostReferenced = mostReferenced.replace("]", "")
    mostReferenced = mostReferenced.replace("'", "")
    # if there is no tie
    if not tie :
        # describe most frequently referenced website
        referenceList = ["The most frequently referenced page is: " + mostReferenced
                      + ", with " + str(referenceCount) + " references"]
    # if there is a tie
    else :
        # describe most frequently referenced websites
        referenceList = ["There is a tie for most frequently referenced pages! The "
                         + "highest reference count is " + str(referenceCount)
                         + " and the urls most frequently referenced are: "
                         + mostReferenced]
    # return a 'list' of information about most frequently referenced website(s)
    return referenceList

# takes a list of words and creates a gui showing those words
# with their text size equivalent to their frequency
def displayWordCloud(listOfWords) :
    # create GUI
    myGUI = Tk()
    # set up title for GUI window
    myGUI.title("Word Cloud")
    # set size for GUI window
    myGUI.geometry('800x600')

    # create a counter
    count = 0
    # set the end point for the counter as the length of the list of words
    MAX = len(listOfWords)
    # while the counter is less than the number of words
    while count < MAX :
        # create the text size based on the frequency of the word
        size = listOfWords[count][1]
        # set up the text for the label
        thetext = listOfWords[count][0]
        # iterate the counter
        count = count +1
        # set up font type and size for label
        labelfont = ('times', size)
        
        # create a new label in the GUI window with the word as text and the frequency as the size
        newLabel = Label(myGUI, text=thetext, anchor=CENTER, justify=CENTER, font=labelfont)
        # add the label to the GUI window
        newLabel.pack()

# Driver#----------------------------------------------------------------
def my_main():

    # make an empty list to hold data for the CSV file
    csvList = [ ]
    # make an empty list to hold the dictionary's for each website
    mainList = [ ]
    # open the hardcoded url text file
    urlfile = open("urls.txt", "r")
    # iterate through URLs in text file
    for url in urlfile :
        # remove new line character
        url = url[:-1]
        # create a dictionary for the url
        mainList = addNewDictionary(mainList, (url, getTitleFromURL(url)))

    # iterate through the dictionaries in the list
    for dictionary in mainList :
        # get the links and titles within the current dictionary's webpage
        newURLs = getURLsFromPage(dictionary['URL'])

        # iterate through the link information in the current webpage
        for x in newURLs :
            # update the current dictionary's Links values
            dictionary['Links'].insert(len(dictionary['Links']), x[0])
            # if the link already exists within the list of dictionaries
            if mainListContainsURL(mainList, x[0]) :
                # update the reference count for that link's dictionary
                mainList = updateDictionaryReferences(mainList, x[0])
            else :
                # otherwise
                # if we are under the total websites we need to parse
                if len(mainList) < 6 :
                    # add a new dictionary to the list of dictionaries
                    mainList = addNewDictionary(mainList, x)

        # add a new entry for the CSV list
        csvList.append([dictionary['URL'], dictionary['Links']])


    
    # create/open a new CSV file
    myCSV = open('websiteCSV.csv', 'w', newline='')
    # set up a csv writer
    writer = csv.writer(myCSV, quoting=csv.QUOTE_ALL)
    # create a header for the csv file
    header = ["Page", "Links"]
    # write the header for the csv file
    writer.writerow(header)

    # create an empty list of words
    words = [ ]

    # iterate through the entries in the csv list
    for alist in csvList :
        # convert the list of links to a string and remove the opening and closing brackets
        alist[1] = str(alist[1])[1:-1]
        # remove all the apostrophe's in the links
        alist[1] = alist[1].replace("'", "")
        # collect words from the link text
        words = collectWordsFromLinksToList(alist[1], words)
        # write the page and link to the csv file
        writer.writerow(alist)

    # create an empty dictionary for words
    wordDictionary = {}

    # iterate through the words in the list
    for word in words :
        # if the word is already in the dictionary
        if word in wordDictionary :
            # update the number of times the word is seen
            wordDictionary[word] += 1
        # otherwise
        else :
            # add a new key and value to the dictionary
            wordDictionary[word] = 1

    # get the fifteen highest used words
    highestValues = getFifteenHighestValues(wordDictionary)

    displayWordCloud(highestValues)
    
    print(highestValues)
           
    # write a row in the CSV to give information about the most frequently
    # referenced pages
    writer.writerow(getReferenceList(mainList))
    
    # close the CSV file
    myCSV.close()


#----------------------------------------------------------------       
if __name__ == '__main__':
        my_main()
