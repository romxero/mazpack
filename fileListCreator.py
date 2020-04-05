#!/usr/bin/env python
# -*- coding: utf-8 -*-
#mazPack json creator
##
## Created by Randall White for Stanford Earth Sciences CEES
##
#os
import os
#system
import sys
#async io
import asyncio
#json
import json
#base 64
import base64
#randomization
import random
#date time library
import datetime #importing library
#hashes
import hashlib
#arangodb driver
#import pyarango
#uuid
import uuid
#csv
import csv

#command for tar : tar cf <tar_val> --no-recursion <dir_val>



# Get environment variables
MAZ_DB_SRV = os.getenv('MAZ_DB_SRV')
MAZ_SSH_KEY = os.getenv('MAZ_SSH_KEY')
MAZ_TMP_DIR = os.getenv('MAZ_TMP_DIR')
MAZ_COMP_THRD = os.getenv('MAZ_COMP_THRD')
MAZ_PROC_THRD = os.getenv('MAZ_PROC_THRD')

collectionName = ""
documentName = ""
################

#import os  
#path="abc.txt"  
#if os.path.isdir(path):  
#    print("\nIt is a directory")  
#elif os.path.isfile(path):  
#    print("\nIt is a normal file")  
#else:  
#    print("It is a special file (socket, FIFO, device file)" )
#print()





##################
def main(args):
    
    mainList = [] #the main list for file objects


    reader = csv.reader(open(sys.argv[1]),
                        delimiter='\t')
    for row in reader:
        tmpFileListObj = {} #main tmpbuffer
        tmpFileListObj['fileId'] = str(uuid.uuid4())
        tmpFileListObj['filePath'] = row[1]
        tmpFileListObj['fileSize'] = row[0]
        if os.path.isdir(row[1]):
            tmpFileListObj['isFileDirectory?'] = "true"
        else:
            tmpFileListObj['isFileDirectory?'] = "false"  
        mainList.append(tmpFileListObj)


    with open(sys.argv[1] + '.json', 'w') as outfile:
        json.dump(mainList, outfile)
        return 0

if __name__ == '__main__':
    import sys #redundant
    sys.exit(main(sys.argv))
