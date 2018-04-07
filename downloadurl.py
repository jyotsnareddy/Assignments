import urllib2, sys

urltodownload = "http://www.sharecsv.com/dl/04a9c977e80226a7632fc2c0ba178081/aapl.csv"
localzipfilepath = "C:\Users\jyots\Downloads\aapl.csv"

hdr = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

webrequest = urllib2.Request(urltodownload,headers=hdr)
try:
    page = urllib2.urlopen(webrequest)
    print "open url successful"
    content = page.read()
    output = open("aap.csv","wb+")
    output.write(bytearray(content))
    output.close()

except urllib2.HTTPError, e:
    print("************************ error occured **************************")
    print e.fp.read()
    print "there was an error when trying to download the file from url ", urltodownload

import csv

oneFileName = "aap.csv"

lineNum = 0

ListofLists = []
with open(oneFileName,'rb') as csvfile:

    lineReader = csv.reader(csvfile, delimiter = ",", quotechar = "\"")
    for row in lineReader:
        lineNum = lineNum + 1

        if lineNum == 1:
            print "skipping header row"
            continue
        date = row[0]
        open = row[1]
        close = row[4]
        volume = row[5]
        oneResultRow = [volume, date, open, close]
        ListofLists.append(oneResultRow)

        print(date)
    print ListofLists
    print "Done Iterating"
    print("we have stock info for " + str(len(ListofLists)))

# listOfListsSortedByQty = sorted(ListofLists, key=lambda x:x[2], reverse=True)


