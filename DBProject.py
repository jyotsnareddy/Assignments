import urllib2, cookielib
import zipfile, os
import time
import sqlite3
from datetime import datetime

conn = sqlite3.connect('example.db')
# c = conn.cursor()
#
# c.execute('CREATE TABLE prices (SYMBOL text, SERIES text, OPEN real, HIGH real, LOW real, CLOSE real, LAST real, PREVCLOSE real, TOTTRDQTY real, TOTTRDVAL real, TIMESTAMP date, TOTALTRADES real, ISIN text, PRIMARY KEY (SYMBOL, SERIES, TIMESTAMP))')
# conn.commit()
#
######################### DOWNLOAD AND UNZIP THE FILES ###########################3

# def download(localzipfilepath, urltodownload):
#     hdr = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
#
#     webrequest = urllib2.Request(urltodownload, headers=hdr)
#
#     ################ DOWNLOADING THE ZIP FILE FROM THE URL #############################3#######################
#
#     try:
#         page = urllib2.urlopen(webrequest)
#         content = page.read()
#         output = open(localzipfilepath, "wb")
#         output.write(bytearray(content))
#         output.close()
#
#     except urllib2.HTTPError, e:
#         print("************************ error occured **************************")
#         print e.fp.read()
#         print "there was an error when trying to download the file from url ", urltodownload
#
#     import os, zipfile
    # localextractfilepath = "C:\Users\jyots\PycharmProjects\Test"
    # localextractfilepath = "C:\Users\jyots\Downloads"

# def unzip(localzipfilepath, localextractfilepath):
#
#     #########################3333 EXTRACTING THE ZIP FILE############################
#     if os.path.exists(localextractfilepath):
#         print("local file path exists")
#         ListofFiles = []
#         fh = open(localzipfilepath, "rb")
#
#         zipfilehandler = zipfile.ZipFile(fh)
#         for filename in zipfilehandler.namelist():
#             zipfilehandler.extract(filename, localextractfilepath)
#             ListofFiles.append(localextractfilepath + filename)
#             print "extracted" + filename + "from the zip file" + (localextractfilepath + filename)
#             # print symbol, "{:,.1f}".format(float(tradedQty) / 1e6) + "M INR", "{:,.1f}".format(pctChange * 100) + "%"
#     print "we extracted " + str(len(ListofFiles))
#     fh.close()
#
# def downloadandUnzipforPeriod(listOfMonths, listOfYears):
#     for year in listOfYears:
#         for month in listOfMonths:
#             for dayofMonth in range(31):
#                 date = dayofMonth + 1
#                 dateStr = str(date)
#                 if date < 10:
#                     dateStr = "0" + dateStr
#                 print dateStr, "-", month, "-", year
#                 filename = "cm" + str(dateStr) + str(month) + str(year) + "bhav.csv.zip"
#                 # urltodownload = "http://www.nseindia.com/content/historical/Equities/" + year + "/" + month + "/" + filename
#                 localzipfilepath = "C:\Users\jyots\PycharmProjects\Test\Database\Files/" + filename
#                 # download(localzipfilepath, urltodownload)
#                 if os.path.exists(localzipfilepath):
#                     unzip(localzipfilepath, localextractfilepath)
#                     time.sleep(3)
#                 else:
#                     continue
#
#     print "ok all downloading and extracting"
#
# localextractfilepath = "C:\Users\jyots\PycharmProjects\Test\Database\Extractedfiles"
# listofMonths = ['JAN', 'FEB', 'MAR']
# listofYears = ['2014']
# downloadandUnzipforPeriod(listofMonths,listofYears)

#######################################################################################
# Parse each file and inserteach row of file into Database
#######################################################################################
#
# def insertRows(fileName, conn):
#     c = conn.cursor()
#     lineNum = 0
#     with open(fileName, 'rb') as csvfile:
#         lineReader = csv.reader(csvfile, delimiter = ',', quotechar = "\"")
#         for row in lineReader:
#             lineNum = lineNum + 1
#             if lineNum == 1:
#                 print "Header row, skipping"
#                 continue
#             date_object = datetime.strptime(row[10], '%d-%b-%Y')
#             # oneTuple = [row[0], row[1], float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]),float(row[8]), float(row[9]), date_object, float(row[11]), float(row[12])]
#             oneTuple = [row[0], row[1], float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7]),float(row[8]),float(row[9]),date_object,float(row[11]),row[12]]
#             # c.execute("INSERT INTO prices VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?", oneTuple)
#             c.execute("INSERT INTO prices VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",oneTuple)
#         conn.commit()
#         print "Done iterating over the file - the file has been cosed now"
#
# import os, csv, datetime
# from datetime import datetime
# localextractfilepath = "C:\Users\jyots\PycharmProjects\Test\Database\Extractedfiles"
#
#
# for file in os.listdir(localextractfilepath):
#     if file.endswith(".csv"):
#         insertRows(localextractfilepath+"/"+file,conn)

################# TEST QUERY ##############################

t1 = "ICICIBANK"
series = "EQ"
c = conn.cursor()
cursor = c.execute('SELECT symbol, max(close), min(close),max(timestamp), min(timestamp), count(timestamp) FROM prices WHERE symbol = ? and series = ? GROUP BY symbol ORDER BY timestamp', (t1, series))
for row in cursor:
    print row

#################### Run a query to get all data for given stock and create an excel ##################################

import xlsxwriter

def createExcelwithDailyPricemoves(ticker,conn):
    c = conn.cursor()
    cursor = c.execute('SELECT symbol, timestamp, close FROM prices where symbol = ? and series = ? ORDER BY timestamp',(ticker,series))
    excelFilename = "C:\Users\jyots\PycharmProjects\Test\Database\Output/" +ticker+".xlsx"
    workbook = xlsxwriter.Workbook(excelFilename)
    worksheet = workbook.add_worksheet("Summary")
    worksheet.write_row("A1", ["Top traded stocks"])
    worksheet.write_row("A2", ['Stock','Date','Closing'])
    lineNum = 3

    for row in cursor:
        worksheet.write_row("A",str(lineNum),list(row))
        print "A" + str(lineNum), list(row)
        lineNum = lineNum + 1

    chart1 = workbook.add_chart({'type': 'line'})
    chart1.add_series({
        'categories': '=Summary!$B$3:$B$' + str(lineNum),
        'values': '=Summary!$C$3:$C$' + str(lineNum)
    })
    # Add a chart title and some axis labels
    chart1.set_title({'name': ticker})
    chart1.set_x_axis({'name': 'Date'})
    chart1.set_y_axis({'name': 'Closing Price'})

    # Insert the chart into the worksheet (with an offset)
    worksheet.insert_chart('F2', chart1, {'x_offset': 25, 'y_offset': 10})
    workbook.close()


conn = sqlite3.connect('example.db')
# Call the function above to create an excel file for the ticker
# RELIANCE which is one of Indias most actively traded stocks
createExcelwithDailyPricemoves('RELIANCE', conn)
# Close the connection. We only queried (read) from the database
# so there is no need to commit

#
# # In[1]:
#
# ################################################################
# # Step 6: We will also see how to drop a table to clear up
# ##################################################################
#
# # Drop table
# # Step 1: open up a connection
# conn = sqlite3.connect('example.db')
# # Step 2: get a cursor
# c = conn.cursor()
# # Step 3 : Drop the table so we leave the database in the same state in which we started with
# c.execute('DROP TABLE prices')
# # Step 4 : OK - we wrote to the database, so we must commit our changes
# conn.commit()
# # Step 5 : Close the connection
# conn.close()




