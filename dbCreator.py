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
import pyArango
#uuid
import uuid
#csv
import csv
import datetime

from pyArango.connection import *

dbServer = ""
dbPassword = ""
#command for tar : tar cf <tar_val> --no-recursion <dir_val>


mainArchiveObj = {
    "name": "",
    "id": "",
    "dateTime":"",
    "baseLocation":"",
    "locationSize":"",
    "archiveSizeAvg":"",
    "fileList": [],
    "clusterList":[]
}

def main(args):
    

    conn = Connection(arangoURL='http://'+ dbServer + ':8529',username="root", password=dbPassword)    
    db = conn.createDatabase(name=sys.argv[1]+"_mazpack") #create database
    #db = conn["mazpack"] #connect to database
    ##create collections:
    clusterListCollection = db.createCollection(name="clusterList")
    fileListCollection = db.createCollection(name="fileList")
    metaListCollection = db.createCollection(name="metaList")

    metaListDoc = metaListCollection.createDocument()
    metaListDoc['name'] = sys.argv[1]
    metaListDoc['id'] = str(uuid.uuid4())
    metaListDoc['dateTime'] = datetime.now()
    metaListDoc._key = "meta_" + sys.argv[1]
    metaListDoc.save()





    #####end
    return 0




if __name__ == '__main__':
    import sys #redundant
    sys.exit(main(sys.argv))
