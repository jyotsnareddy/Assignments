import urllib2, sys
outputDict = {}
UrlToRead = "google.com"
while UrlToRead != "":

    try:
        UrlToRead = input("Please enter the URL to download ")
        if UrlToRead == "":
            print "exiting the loop"
            break
        UrlName = input("Please enter a name corresponding to this URL " + UrlToRead + " ")
        weburl = urllib2.urlopen(UrlToRead).read()
        outputDict[UrlName] = weburl
    except:
        print "***************** An error occured*********************"
        print sys.exc_info()[0]
        askUser = input("An error occured do you wish to continue? YES/NO")
        if askUser == "NO":
            print "stopping the pgm"
            break
        else:
            print "continuing the pgm"
            continue
    print "inside the while "
print(outputDict.viewkeys())
print outputDict

