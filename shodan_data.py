import simplejson
import sys
import os.path

if(len(sys.argv) < 3):
        print "Usage: shodan_data.py <flags> <file>\n     use -h to see the flags that are available"
        sys.exit()
if(sys.argv[1] == "-h"):
        print " Available Flags:"
        print "         -ip: The IP Address of the host"
        print "         -isp: The ISP of the host"
        print "         -org: The org of the host"
        print "         -port: The open port on Host"
        print "         -data: The Data field reported on the host"
        sys.exit()
if(len(sys.argv) > 8):
        print "Too many arguments"
        sys.exit()
counter = 1

value = len(sys.argv)
while (counter < value ):
        varbs = sys.argv[counter]
        if str(varbs) in( "-ip", "-isp", "-org", "-port", "-data" ):
                counter = counter
        elif ( os.path.isfile(sys.argv[counter]) != True ):
                print "Invalid option: " + sys.argv[counter]
                sys.exit()
        counter = counter + 1
with open(sys.argv[value -1], 'r') as fin:
        for line in fin:
                data = simplejson.loads(line.strip())
                counter = 1
                value = len(sys.argv)
                output = ""
                while ( counter < value ):
                        if ( sys.argv[counter] == "-ip" ):
                                output = output + data["ip_str"] +","
                        elif ( sys.argv[counter] == "-isp" ):
                                output = output + data["isp"] +","
                        elif ( sys.argv[counter] == "-org" ):
                                output = output + data["org"] + ","
                        elif ( sys.argv[counter] == "-port"):
                                output = output + str(data["port"]) + ","
                        elif ( sys.argv[counter] == "-data"):
                                output = output + data["data"] + ","
                        counter = counter + 1
                print(output)
