import urllib2, sys

urltodownload = "https://fred.stlouisfed.org/categories/32255/downloaddata/STOCKMARKET_csv_2.zip"
localzipfilepath = "C:\Users\jyots\Downloads\STOCKMARKET_csv_2.zip"
# localzipfilepath = "C:\Users\jyots\PycharmProjects\Test\STOCKMARKET_csv_2.zip"


hdr = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

webrequest = urllib2.Request(urltodownload,headers=hdr)

################ DOWNLOADING THE ZIP FILE FROM THE URL #############################3#######################

try:
    page = urllib2.urlopen(webrequest)
    content = page.read()
    output = open(localzipfilepath,"wb")
    output.write(bytearray(content))
    output.close()

except urllib2.HTTPError, e:
    print("************************ error occured **************************")
    print e.fp.read()
    print "there was an error when trying to download the file from url ", urltodownload

import os, zipfile
# localextractfilepath = "C:\Users\jyots\PycharmProjects\Test"
localextractfilepath = "C:\Users\jyots\Downloads"

#########################3333 EXTRACTING THE ZIP FILE############################
if os.path.exists(localextractfilepath):
    print("local file path exists")
    ListofFiles = []
    fh = open(localzipfilepath,"rb")

    zipfilehandler = zipfile.ZipFile(fh)
    for filename in zipfilehandler.namelist():
        zipfilehandler.extract(filename, localextractfilepath)
        ListofFiles.append(localextractfilepath + filename)
        print "extracted" + filename + "from the zip file" + (localextractfilepath + filename)
        # print symbol, "{:,.1f}".format(float(tradedQty) / 1e6) + "M INR", "{:,.1f}".format(pctChange * 100) + "%"
print "we extracted " + str(len(ListofFiles))
fh.close()

################################### Reading the file ###########################################################

import csv

# oneFileName = ListofFiles[4]
oneFileName = "C:\Users\jyots\Downloads\STOCKMARKET_csv_2\data\RU3000TR.csv"
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
        value = row[1]
        oneResultRow = [date,value]
        ListofLists.append(oneResultRow)

        # print(date)
    # print ListofLists
    print "Done Iterating"
    print("we have stock info for " + str(len(ListofLists)))

listOfListsSortedByQty = sorted(ListofLists, key=lambda x:x[0], reverse=True)

listOfListsSortedByQty = sorted(ListofLists, key=lambda x: x[1], reverse=True)

import xlsxwriter
excelFileName = "C:\Users\jyots\Downloads\output.xlsx"
# excelFileName = "C:\Users\jyots\PycharmProjects\Test\output.xlsx"
workbook = xlsxwriter.Workbook(excelFileName)
worksheet = workbook.add_worksheet("summary")

worksheet.write_row("A1", ["Date"])
worksheet.write_row("B1", ["Value"])

for rownum in range(5):
    oneRowtowrite = listOfListsSortedByQty[rownum]

    worksheet.write_row("A" + str(rownum + 3),oneRowtowrite)

workbook.close()