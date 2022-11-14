#Activity Crawler API
#Build large library of activities from open-data/publicly available information
#take as input a search string consisting of:
#activity name
#location information like city & state

#data return will return as JSON object

#list of fields as MOPO GOld Standard Doc
#WILL NOT HAVE:
#start/end datetime
#WILL HAVE(may not be reliable):
#Opening hours
#phone number

#generate googles map link for venue
#Use AI to parse out operating hours/phone number
import webbrowser as browser
from urllib import response
import urllib.request, json, pprint, requests

def activity_crawler_api():
    

    activity = {}

    #given url https://nominatim.openstreetmap.org/details.php?osmtype=W&osmid=407063554&class=tourism&addressdetails=1&hierarchy=0&group_hierarchy=1&format=json
    #if not given url use osmid string with conjunction of base url without any parameters, this returns same page/json
    with urllib.request.urlopen("https://nominatim.openstreetmap.org/details.php?osmtype=W&osmid=407063554&class=tourism&addressdetails=1&hierarchy=0&group_hierarchy=1&format=json") as url:
        
        #loads it to dictionary called data
        data = json.load(url)

        #converted into class object, but ONLY for reading purposes and use data dictionary
        #use https://docs.python.org/3/library/pprint.html for pprint object manipulation
        #readable_dictionary = pprint.pprint(data, indent=5)
        #print(readable_dictionary)

        #constructing fields: activity name, street number, street address, city, state, zip , lat, long
        activity['osm_id'] = data['osm_id']#OpenStreetMap (OSM) is a digital map database location id
        activity['osm_type'] = data['osm_type']
        activity['type'] = data['type']
        activity['street'] = data['addresstags']['street']
        activity['category'] = data['category']
        activity['location_name'] = data['address'][0]['localname']
        activity['city'] = data['addresstags']['city']
        activity['country'] = data['addresstags']['country']
        activity['district'] = data['addresstags']['district']
        activity['house_number'] = data['addresstags']['housenumber']
        activity['zipcode'] = data['addresstags']['postcode']
        activity['state'] = data['addresstags']['state']
        activity['street'] = data['addresstags']['street']
        activity['longtitude_coordinate'] = data['centroid']['coordinates'][0]
        activity['latitude_coordinate'] = data['centroid']['coordinates'][1]
        activity['wikidata_id'] = data['extratags']['wikidata']
        activity['wikipedia_searchstring'] = data['calculated_wikipedia'].removeprefix('en:')


        wiki_base_url = "https://www.wikidata.org/wiki/"
        #crawling wikidata url
        activity['wikidata_url'] = wiki_base_url + str(activity['wikidata_id'])
        browser.open_new_tab(activity['wikidata_url']) #opens finished url to new tab
    #print(activity.items())
activity_crawler_api()
