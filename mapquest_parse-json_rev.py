import urllib.parse
import requests
from tabulate import tabulate

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "lEd9LltiGqUxDujaS93GodmohinwfxdR"
while True:
    orig = input('\033[35m' + "Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input('\033[35m' + "Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print ('\033[34m'+"URL ", (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print('\033[32m'+"API Status: " + str(json_status) + " = A successful route call.\n")
        print('\033[37m'+"=============================================")
        print("\033[1;35m Directions from " +'\033[35m' + (orig) + " to " +'\033[35m' + (dest))
        print("\033[1;33m Trip Duration:   " + '\033[37m'+ (json_data["route"]["formattedTime"]))
        print("\033[1;33m Kilometers:      " + '\033[37m'+ str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        #print miles measurement to versus with kilometer
        print("\033[1;33m Miles:           " + '\033[37m' + str("{:.2f}".format((json_data["route"]["distance"]))))        
        print("\033[1;33m Fuel Used (Ltr): " + '\033[37m'+ str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print('\033[37m'"=============================================")
        #add road instruction title
        print('\033[36m'+"Road Instructions from "+'\033[35m'+ (orig) + "\033[36m to " +'\033[35m'+ (dest) + "\n")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print('\033[37m'+(each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)" + " (" + str("{:.2f}".format((each["distance"])) + " mi)")))
        print('\033[37m'+"=============================================\n")
    elif json_status == 402:
        print('\033[37m'+"**********************************************")
        print('\033[31m'"Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print('\033[37m'+"**********************************************\n")
    elif json_status == 611:
        print('\033[37m'+"**********************************************")
        print('\033[31m'"Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print('\033[37m'+"**********************************************\n")
    else:
        print('\033[37m'+"************************************************************************")
        print('\033[37m'+"For Status Code: " + str(json_status) + "; Refer to:")
        print('\033[37m'+"https://developer.mapquest.com/documentation/directions-api/status-codes")
        print('\033[37m'+"************************************************************************\n")

    #for the table summary
    km=str("{:.2f}".format((json_data["route"]["distance"])*1.61))
    mi=str("{:.2f}".format((json_data["route"]["distance"])))
    fuel=str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78))

    print('\033[1;33m'+"=============================================")
    print('\033[1;33m'+"SUMMARY")
    #display table
    col_names = ["Distance(km)", "Distance(mi)", "Fuel Used"]
    print(tabulate([["Distance(km)", km], ["Distance(mi)", mi], ["Fuel Used(Ltr)", fuel]], floatfmt=".2f", tablefmt="fancy_grid"))
    print("=============================================\n")