#This file is for the purpose of scrubbing the internet for recent stock trades by public figures and importing them as text files
from ast import Try
from lib2to3.pytree import convert
from re import S
import sys
import os
from sqlite3 import DateFromTicks
from sre_compile import isstring
import requests #Sends HTTP requests to a website's server, which will return a response containing my needed data
from bs4 import BeautifulSoup #Parser that extracts data from HTML 
import pandas as pd
#from StockSuggester import *

class StockScraper():
    """ A class that will scrape the internet for the investment patterns of political figure
    """
    
    def interfaceWeb (url):
        pass
    
    
        
    def prepareTradeHistory(politicianId): 
        
        responseJson = []

        url = "https://bff.capitoltrades.com/trades"   
                 
        if (isinstance(politicianId, list)): #when given a list of politicians, the method should handle it by
                                             #putting all trades from all listed
            politicianId = [*set(politicianId)]
            for politician in politicianId: #For each politician Id in the list it will try to iterate
                                        #through all of the pages of stock information, stopping if we
                                        #try to go to a page that does not exist
                
                try:    
                    
                    for page in range(1, 10):

                        querystring = {"page":f"{page}","pageSize":"100","politician":f"{politician}"}

                        headers = {
                            "authority": "bff.capitoltrades.com",
                            "accept": "*/*",
                            "accept-language": "en-US,en;q=0.9,fr;q=0.8",
                            "content-type": "application/json",
                            "origin": "https://www.capitoltrades.com",
                            "referer": "https://www.capitoltrades.com/",
                            "sec-ch-ua": "^\^Google"
                            }

                        response = requests.request("GET", url, headers=headers, params=querystring)

                        data = response.json()
                        
                        for p in data["data"]:
                            
                            responseJson.append(p)
            
                except:
                    
                    pass
            
        else:
            
            try:
                for page in range(1, 10):

                    querystring = {"page":f"{page}","pageSize":"100","politician":f"{politicianId}"}

                    headers = {
                        "authority": "bff.capitoltrades.com",
                        "accept": "*/*",
                        "accept-language": "en-US,en;q=0.9,fr;q=0.8",
                        "content-type": "application/json",
                        "origin": "https://www.capitoltrades.com",
                        "referer": "https://www.capitoltrades.com/",
                        "sec-ch-ua": "^\^Google"
                        }

                    response = requests.request("GET", url, headers=headers, params=querystring)

                    data = response.json()
                    
                    for p in data["data"]:
                        
                        responseJson.append(p)
            
            except IndexError:
                
                print(f"index error at page: {page}")
                pass
        
        getIdDataFrame = pd.json_normalize(responseJson) #puts the information in a format that is easily sorted in excel
        
        getIdDataFrame.to_csv("./TradesExtended.csv") #Takes the information of all traders gathered and puts them in a csv file along with some other data                
        
        return getIdDataFrame
        
        

    def prepareIds():
        """A method that will prepare a dataframe of all the politicians and their information"""
        
        responseJson = [] #initialize the array that will eventually hold all the gathered information
        
        for page in range(1,6): #Iterate through pages
            payload = ""        

            headers = {
            'authority': "bff.capitoltrades.com",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9,fr;q=0.8",
            'content-type': "application/json",
            'origin': "https://www.capitoltrades.com",
            'referer': "https://www.capitoltrades.com/",
            'sec-ch-ua': "^\^Google"
            }
            
            getIdResponse = requests.request("GET", f"https://bff.capitoltrades.com/politicians?page={page}&pageSize=50&metric=dateLastTraded&metric=countTrades&metric=countIssuers&metric=volume")
            #Go to capitol trades and request the data on each public figure there through their api
            
            data = getIdResponse.json() #get the json of the server's response
            
            
            for p in data["data"]:      #iterate through all the data available in this and adds it to the "responseJson" array
                responseJson.append(p)
                
            getIdDataFrame = pd.json_normalize(responseJson) #puts the information in a format that is easily sorted in excel
        
            getIdDataFrame.to_csv("TraderIDs.csv") #Takes the information of all traders gathered and puts them in a csv file along with some other data
            
        return getIdDataFrame
    
    

    def getIds( name = None, party = None, state = None, chamber = None, gender = None, testData = None):
        """A method that will grab the IDs of all the politicians with criteria matching passed arguments. If no arguments are passed, it will return the IDs of all politicians
        """
        
        #os.chdir('c:/Users/Owner/Documents/GitHub/DayTrader/StockSuggester')
        print(os.getcwd())
        if (testData != None):

            getIdDataFrame = pd.read_csv("Test_TraderIDs.csv")
            
        else:
            getIdDataFrame = StockScraper.prepareIds()
        
        #Handle the keyword arguments passed
        if (name != None): #if an argument has been passed for politician name
            
            getIdDataFrame = StockScraper.searchColumn(
                getIdDataFrame, "fullName",name, True)[0]
            
            
        if (party != None): #if an argument has been passed for politician party
            
            getIdDataFrame = StockScraper.searchColumn(
                getIdDataFrame, "party", party, True)[0]
            
        if (state != None): #if an argument has been passed for state
            
            if (len(state) > 2 ):
                
                state = StockScraper.convertState(state).lower()
                
            else:
                state = state.lower()
                
            getIdDataFrame = StockScraper.searchColumn(
                getIdDataFrame, "_stateId", state, True)[0]
           
        if (chamber != None): #if an argument has been passed for chamber
            
            getIdDataFrame = StockScraper.searchColumn(
                getIdDataFrame, "chamber", chamber, True)[0]
        
        if (gender != None):
            
            getIdDataFrame = StockScraper.searchColumn(
                getIdDataFrame, 'gender', gender, True)[0]
        
        politicianIds = (getIdDataFrame["_politicianId"]) #Grab the column that has the IDs of specific politicians
        
        return politicianIds.to_list()
    
 
 
    def searchColumn(dataframe,column, value, returnDataFrame = False): 
        """This method will take the given dataframe and a column and return a list containing the IDs of the relevant parties.
        Setting the returnDataFrame boolean to true will have this method return an entire row for politicians rather than just the ID
        """
        
        politicianIds = []
            
        for index in range (0,len(dataframe[column])): #searching through every row of given column
            
            if (value.lower() in dataframe[column].iloc[index].lower()): #if that row contains the given value
                
                if (returnDataFrame == True): #if dataframe return was marked
                    
                    if (len(politicianIds) <= 0):
                        
                        index2 = index + 1 #the purpose of this is for grabbing a single index of dataframe
                        
                        politicianIds.append(dataframe[index : index2]) #First index for list so we can use dataframe append in future loops
                        
                    else:    
                        
                        index2 = index + 1
                        
                        politicianIds[0] = pd.concat([politicianIds[0],dataframe[index : index2]], ignore_index= True) #add the entire row to the dataframe within politicianIds array
                        
                else:
                    politicianIds.append(dataframe["_politicianId"].iloc[index]) #If returnDataFrame is false, however, add just the politician ID to the array
        
        if len(politicianIds) <=0:
            
            raise ValueError(f"{value} is not in database")
        
        return politicianIds 
    
    
    
    def convertState(state):
        
        stateFull = True
        
        us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

        if (len(state) <= 2):
            
            abbrev_to_us_state = dict(
                map(reversed, us_state_to_abbrev.items()))
            
            stateFull = False
        
        try:
            
            if stateFull:
                
                returnState = us_state_to_abbrev.get(state.capitalize())
                
            if not(stateFull):
                
                returnState = abbrev_to_us_state.get(state.upper())
                
            if returnState == None:
                
                raise ValueError(
                    f"{state} is not a state or a valid state abbreviation.")
            
        except:
            
                 raise ValueError(
                    f"{state} is not a state or a valid state abbreviation.")           

        return returnState



    def detailedInfo(id):
        """ When giving IDs as a string or list of strings will go to their more detailed pages
        and gather the information there. Only send out information wanted in the politician object"""

        tradeDataframe = StockScraper.prepareTradeHistory(id) #prepareTradeHistory handles both strings and lists
        
        tradeDataframe = tradeDataframe.drop(columns = ["_txId","_assetId","_issuerId","pubDate", "txTypeExtended","hasCapitalGains",
                                       "owner", "committees", "labels", "asset.instrument", 
                                       "issuer._stateId", "issuer.c2iq", "politician.nickname"])
        
        tradeDataframe.to_csv("./Trades.csv")
        
        return tradeDataframe
    
    
    def politicianPopulate(dataframe):
        pass


if __name__ == "__main__":
    print("\n\n\n")
    #StockScraper.interfaceWeb("https://www.smartinsider.com/politicians/")
    #StockScraper.interfaceWeb("https://www.capitoltrades.com/politicians/")
    #StockScraper.interfaceCT()
    os.chdir('c:/Users/Owner/Documents/GitHub/DayTrader/StockSuggester')
    print(StockScraper.detailedInfo("F000462"))



