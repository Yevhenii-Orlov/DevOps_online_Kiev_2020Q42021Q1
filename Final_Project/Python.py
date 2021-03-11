import urllib.parse
import requests

main_api = "http://www.mapquestapi.com/directions/v2/route?"

#key
key = "F8zn5GJu5M8QijBZJyE8l906IrADG7pB"


while True:
    orig = input("Start Location: ")
    if orig == "q" or orig == "quit":
        break 
    dest = input("Finish Location: ")


    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    json_data = requests.get(url).json()

    json_data = requests.get(url).json()

    json_status = json_data["info"]["statuscode"]
    
    f = open('index.html','w')

    message = """<html style="height: 100%;">
	<style 
		   lang="en" type="text/css" id="night-mode-pro-style">html {background-color: #FFFFFF !important;} body {background-color: #FFFFFF;}
	</style>
	<link type="text/css" rel="stylesheet" id="night-mode-pro-link">

	<head>
  <meta charset="utf-8">
  <title>Map</title>
  	</head>
	
	<body style="margin: 0px; background: #0e0e0e; height: 100%">
		<img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 100%);transition: background-color 300ms;" 
			 src="https://www.mapquestapi.com/staticmap/v5/map?key=F8zn5GJu5M8QijBZJyE8l906IrADG7pB&amp;start=""" + orig + """|flag-start&amp;end=""" + dest + """|flag-end&amp;scalebar=true|bottom&amp;size=1920,1080@2x&amp;banner=From+""" + orig + """+To+""" + dest + """|sm-rigth-562C22-EEDFD8" width="1920" height="1080">
	</body>
</html>"""

    f.write(message)
    f.close()
        
    if json_status == 0:
        #print("API Status: " + str(json_status))
        print (url)
        print("Trip      : " + (orig) + " to " + (dest))
        print("Duration  : " + (json_data["route"]["formattedTime"]))
        print("Kilometers: " + str("{:.1f}".format((json_data["route"]["distance"])*1.609)))
        print("Fuel Used : " + str("{:.1f}".format((json_data["route"]["fuelUsed"])*3.785)))
        print("=========================================================================")
        
     
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + ") " + "km"))
            print("=====================================================================")
    else:
        print("Запрос не удался. Попробуйте снова")


