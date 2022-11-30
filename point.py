"""File holding class and it's features"""
from os import getenv
from dotenv import load_dotenv
import requests
load_dotenv()


class Point:
    """Class holding point's data and it's functions"""
    def __init__(self, name: str):
        self.pointName = name.replace(" ", "%20")
        self.API = getenv("API")
        url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={self.pointName}&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key={self.API}"
        response = requests.request("GET", url)
        json = response.json()
        self.latitude = self.getLatitude(json)
        self.lengthtitude = self.getLengthtitude(json)
        self.coords = [self.latitude, self.lengthtitude]
        self.detailedLocation = self.getLocation(json)

    def getLocation(self, json):
        return json["candidates"][0]["formatted_address"]

    def getLatitude(self, json):
        return json["candidates"][0]["geometry"]["location"]["lat"]

    def getLengthtitude(self, json):
        return json["candidates"][0]["geometry"]["location"]["lng"]

    def distanceToX(self, destination):
        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={self.pointName}&destinations={destination}&units=metric&key={self.API}"
        response = requests.request("GET", url)
        json = response.json()
        return json["rows"][0]["elements"][0]["distance"]["value"]

    def timeToX(self, destination):
        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={self.pointName}&destinations={destination}&units=metric&key={self.API}"
        response = requests.request("GET", url)
        json = response.json()
        return json["rows"][0]["elements"][0]["duration"]["value"]
    