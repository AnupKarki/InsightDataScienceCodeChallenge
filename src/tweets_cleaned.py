# example of program that calculates the number of tweets cleaned

import os,sys,json



def writingToFile(target,string,date):
    toWrite = string.encode('ascii','ignore')  ## removes the uncode character
    target.write(toWrite+', (timestamp:'+str(date)+') \n')      
    return all(ord(char) < 128 for char in string) ## returns true if a unicode character is present
   
    
    

def main():
    #BasePath = os.path.dirname(os.getcwd())
    #inputFile = os.path.join(BasePath,'tweet_input','tweets.txt')
    #outputFile_featureOne = os.path.join(BasePath,'tweet_output','ft1.txt')
    inputFile = sys.argv[1]
    outputFile_featureOne = sys.argv[2]
    target = open(outputFile_featureOne,'w')
    unicodeCounter = 0
    with open(inputFile) as data_file:
        for line in data_file:
            data_unprocessed = json.loads(line)
            if 'text' not in data_unprocessed:
                pass
            else:
                unicodeExist = writingToFile(target,data_unprocessed['text'],data_unprocessed['created_at'])
                unicodeCounter += unicodeExist
        target.write('\n'+str(unicodeCounter) + ' tweets contained unicode.')
        target.close()
        data_file.close()
    
     
if __name__ == '__main__':
    main()

