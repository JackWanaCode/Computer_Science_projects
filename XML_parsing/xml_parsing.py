import csv
import requests
import xml.etree.ElementTree as ET

def loadRSS():
    #url or rss feed
    url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'

    #craete HTTP response object from given url
    res = requests.get(url)

    #saving the xml file
    with open('topnewsfeed.xml', 'wb') as f:
        f.write(res.content)

def parseXML(xmlfile):
    #create element tree object
    tree = ET.parse(xmlfile)

    #get root element
    root = tree.getroot()

    #create empty list for news items
    newsitems = []

    #iterate news items
    for item in root.findall('./channel/item'):
        #empty news dictionary
        news = {}

        #iterage child elements of item
        for child in item:
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')

        #append news dictionary to news items list
        newsitems.append(news)

    return newsitems

def savetoCSV(newsitems, filename):
    #specifying the fields for csv file
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']

    #writing to csv file
    with open(filename, 'w') as csvfile:
        #creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        #writing headers (field names)
        writer.writeheader()

        #writing data rows
        writer.writerows(newsitems)

def main():
    loadRSS()

    #parse xml file
    newsitems = parseXML('topnewsfeed.xml')

    #store news items in a csv file
    savetoCSV(newsitems, 'topnews.csv')

if __name__ == "__main__":
    main()


