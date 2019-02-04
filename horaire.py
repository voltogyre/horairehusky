import json
import os

def xstr(s):
    if s is None:
        return ''.encode('utf-8')
    return str(s).encode('utf-8')

with open(os.path.dirname(os.path.abspath(__file__))+'/outputpretty.json', 'r') as fp:
    obj = json.load(fp)
fp.close
teamlist = {}
#print("json loaded")
for event in obj:
    for teams in event["TeamList"]:
        #print(teams["Name"].encode('utf-8'))
        teamlist[teams["Name"].encode('utf-8')] = 1

#print("teams loaded")
for team in teamlist :
    #print(team)
    file = open(os.path.dirname(os.path.abspath(__file__)) + "/"+ team +".txt","w")
    file.write( "************************************************************\n")
    file.write( "                        "+ team +"\n")
    file.write( "************************************************************\n")
    number = 0
    for event in obj:
        #print(event)
        number += 1
        for teams in event["TeamList"]:
            if  teams["Name"].encode('utf-8') == team :
                file.write( "=============================\n")
                file.write( event["Title"].encode('utf-8') + "\n")
                file.write( event['Date'].encode('utf-8') + "\n")
                file.write( xstr(event['StartTime']) + " - " + xstr(event['EndTime']) + " ( " +  xstr(event['Duration']) + " )" + "\n")
                file.write( event['SportCenterAbr'].encode('utf-8') + " - " + event['SportCenterName'].encode('utf-8') + "\n")
                for teams in event["TeamList"]:
                    file.write( "    " + teams["Name"].encode('utf-8') + "\n")
    file.close
