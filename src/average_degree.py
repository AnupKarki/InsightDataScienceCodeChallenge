
# example of program that calculates the average degree of hashtags
import os,sys,json
import datetime
from dateutil import parser
from collections import Counter

def calculateAverage(hashList):
    #### takes the hash list and returns the average of the within the list
    totalConnectionList = []    
    for hashs in hashList:
        hashtags = [hashValues.lower() for hashValues in hashs['hashTag']] ## convert all the hashtags to lower case 
        hashlistTuple = getHashListTuple(hashtags)
        totalConnectionList +=hashlistTuple
    getTupleFlatList = flatten_tuple(totalConnectionList)
    count = Counter(getTupleFlatList)
    average = float(sum(count.values()))/len(hashList)
    return average

def flatten_tuple(tupleList):
    ### returns the flat list of the tuples constructed
    return list(reduce(lambda x,y: x+y,tupleList))

def getHashListTuple(listofHashs):
    ### GEt list of links within a single hash list    
    listTuples = []
    for i in range(len(listofHashs)-1):
        for j in range(i+1,len(listofHashs)):
            listTuples.append((listofHashs[i],listofHashs[j]))
    return listTuples
    
        

def main():
    #BasePath = os.path.dirname(os.getcwd())
    #inputFile = os.path.join(BasePath,'tweet_input','tweets.txt')
    #outputFile_featureOne = os.path.join(BasePath,'tweet_output','ft2.txt')
    inputFile = sys.argv[1]
    outputFile_featureTwo = sys.argv[2]
    target = open(outputFile_featureTwo,'w')
    hashList = []
    with open(inputFile) as data_file:
            for line in data_file:
                data_unprocessed = json.loads(line)
                if 'text' not in data_unprocessed:
                    pass
                else:
                    hashtags = [word for word in data_unprocessed['text'].split() if "#" in word]
                    if len(hashtags) > 1:         ### don't process if only single hastag is present
                        hashList.append({'hashTag':hashtags,'date':data_unprocessed['created_at']})
                        lastDate = parser.parse(hashList[-1]['date'])
                        for hashTags in hashList:
                            ##Checks if the current hastag is within the 60 secs 
                            ## of the first hashtag. If not removes the first hashtag
                            ## the same check is done for the subsequent hastags
                            firstDate = parser.parse(hashList[0]['date'])
                            if (lastDate-firstDate).total_seconds() >= 60:
                                del hashList[0]
                        average = calculateAverage(hashList)
                        target.write(str(average)+'\n')
            data_file.close()
            target.close()

if __name__ == '__main__':
    main()

