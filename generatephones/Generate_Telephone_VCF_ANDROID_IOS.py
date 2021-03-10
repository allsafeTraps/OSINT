import time
from datetime import datetime
import argparse
import os.path
from colored import fg, bg

COLOR = fg('#c0c0c0') + bg('#00005f')

def functionCallMethod():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-android", "--android", type = str, help="Filename with telephone list")
    parser.add_argument("-ios", "--ios", type = str, help="Filename with telephone list")

    
    args = parser.parse_args()
    if args.android:
        transformVCFForAndroid(args.android)
    elif args.ios:
        transformVCFForPPLE(args.ios)
    else:
        print(COLOR + "usage: GenerateTelephoneNumbers.py [-h] for to select correct method")        

#FUNCTION CREATE VCF ANDROID
def transformVCFForAndroid(fileTXTToReadForToWriteVCF):
    
    
    try:
    
            if checkFileExist(fileTXTToReadForToWriteVCF):
                #FILENAME TO BE GENERATED
                fileVCFCreatedName = 'PHONE_%s_.vcf' % time.strftime("%H%M%S_%m%d%Y")    
        #       Open the plain text file and load all content into memory
                linestring = open(fileTXTToReadForToWriteVCF, 'r').readlines()
                #lines = linestring.split('\n')
                count = 0
                vcf = open(fileVCFCreatedName,"w")
                for i in linestring:
                    print(COLOR + "PHONE: "+str(count)+" "+i)
                    # File saving
                    vcf.write( 'BEGIN:VCARD' + "\n")
                    vcf.write( 'VERSION:2.1' + "\n")
                    vcf.write( 'N:' + str(count) +"\n")
                    vcf.write( 'FN:' + str(count) + "\n")
                    vcf.write( 'ORG:' + 'TRASTEO' + "\n")
                    vcf.write( 'TEL;CELL:' + i + "\n")
                    vcf.write( 'END:VCARD' + "\n")
                    count = count + 1
                print ("\n" + COLOR + "FILE %s CREATED" % fileVCFCreatedName)
                vcf.close()    
        
    except Exception as inst:    
        print(type(inst))    
        print(inst.args)     
        print(inst)

       
        

#FUNCTION CREATE VCF APPLE
def transformVCFForPPLE(fileTXTToReadForToWriteVCF):
    
    
    try:
    
        if checkFileExist(fileTXTToReadForToWriteVCF):
            #FILENAME TO BE GENERATED
            fileVCFCreatedName = 'PHONE_%s_.vcf' % time.strftime("%H%M%S_%m%d%Y")    
    #       Open the plain text file and load all content into memory
            linestring = open(fileTXTToReadForToWriteVCF, 'r').readlines()
            #lines = linestring.split('\n')
            count = 0
            vcf = open(fileVCFCreatedName,"w")
                   
            for i in linestring:
                print(COLOR+ "PHONE: "+str(count)+" "+i)
                # File saving
                vcf.write( 'BEGIN:VCARD' + "\n")
                vcf.write( 'VERSION:3.0' + "\n")
                vcf.write( 'PRODID:-//Apple Inc.//iOS 12.2//EN' + "\n")
                vcf.write( 'N:' + str(count) +"\n")
                vcf.write( 'FN:' + str(count) + "\n")
                vcf.write( 'TEL;type=HOME;type=VOICE;type=pref:' + i)
                vcf.write( 'REV:' + datetime.utcnow().isoformat() + "\n")
                vcf.write( 'END:VCARD' + "\n")
                count = count + 1
                
            print ("\n" + COLOR + "FILE %s CREATED" % fileVCFCreatedName)
            vcf.close()       
                    
        
    except Exception as inst:    
        print(type(inst))    
        print(inst.args)     
        print(inst)
    

                
         
def checkFileExist(filename):
    
    if(os.path.isfile(filename)):
        return True
    else:
        print ("\n" + COLOR + "FILE %s, NOT EXIST" % filename)
        return False

if __name__ == '__main__':
    functionCallMethod()
