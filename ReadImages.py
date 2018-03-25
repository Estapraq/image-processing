
#this program is to read the hand writting pictures and average the pixcels.
import numpy as np
import matplotlib as ml
from PIL import Image
from functools import reduce #for reduce to be defines
np.seterr(over='ignore')#ignore warning that is already taken care of

def createDataFile01():
    ExamplesFile=open('ExampleFile01.txt', 'a')
    LabelsFile=open('LabelsFile01.txt', 'a')
    MeanRBGExamplesFile=open('MeanRBGFile.txt', 'a')
    images01=range(0,10)#we will read only 0, 1 pictures
    ImageVersions=range(1,9) #1-9 versions
    for eachPic01 in images01:
        for eachVesion in ImageVersions:
            imagePath='images/numbers/'+str(eachPic01)+'.'+str(eachVesion)+'.png'
            ImageRead= Image.open(imagePath)
            ImageReadAsArray=np.array(ImageRead)#Send to get the mean method
            ImageReadAsArray_String= str(ImageReadAsArray.tolist())+'\n'
            ImageLabel=str(eachPic01)+'\n'
            MeanRBGExamplesFile.write(GetTheRBGMean(ImageReadAsArray))
            LabelsFile.write(ImageLabel)
            ExamplesFile.write(ImageReadAsArray_String)
            
          


def GetTheRBGMean(ImageRead):
    AveList=list()
    newAr=ImageRead
    for row in newAr:
        for pix in row:
            AverRBG=reduce(lambda x, y: x+y, pix[:3])/len(pix[:3])#we need a library fpor reduce
            AveList.append(AverRBG)        
    AveListString= str(AveList)+'\n'    
    return AveListString




createDataFile01()

            
            
