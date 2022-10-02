from StockScraper import StockScraper   # The code to test
import unittest   # The test framework
import pandas as pd

class Test_DetailedInfo(unittest.TestCase):
    
    data = [["iniRemove","1a","1remove","2remove","3remove","2a","3a","4a","5remove",'6remove','7remove',"5a","6a","7a","8a","9a","10a","11a" #everything with "remove" represents data the detailedInfo method from StockScraper should exclude
             ,"12a","13a","14a","8remove","9remove","15a","16a","10remove","11remove","12remove","17a","18a","19a","20a","21a","22a","23a","24a","25a", "26a" ,"13remove"],
            ["iniRemove","1b","1remove","2remove","3remove","2b","3b","4b","5remove",'6remove','7remove',"5b","6b","7b","8b","9b","10b","11b" #everything with "remove" represents data the detailedInfo method from StockScraper should exclude
             ,"12b","13b","14b","8remove","9remove","15b","16b","10remove","11remove","12remove","17b","18b","19b","20b","21b","22b","23b","24b","25b", "26b" ,"13remove"]]
    
    dataframe = pd.DataFrame(data, columns = ["_txId", "_politicianId","_assetId",'_issuerId',"pubDate","filingDate","txDate","txType","txTypeExtended","hasCapitalGains","owner",
                                              "chamber","price","size","sizeRangeHigh","sizeRangeLow","value", "filingId","filingURL",
                                              "reportingGap","comment","committees" ,"labels","asset.assetType", "asset.assetTicker","asset.instrument","issuer._stateId","issuer.c2iq",
                                              "issuer.country", "issuer.issuerName", "issue.issuerTicker","issuer.sector","politician._stateId","politician.chamber",
                                              "politician.dob","politician.firstName", "politician.gender", "politician.lastName","politician.nickname"])
    
    
#tradeDataframe = tradeDataframe.drop(columns = ["_txId","_assetId","_issuerId","pubDate", "txTypeExtended","hasCapitalGains",
#                                       "owner", "committees", "labels", "asset.instrument", 
#                                       "issuer._stateId", "issuer.c2iq", "politician.nickname"])
    
    
    
    # def test_grabPolitician(self): #Test is returning Politician "1a" dataframe from Politcian "1a" arg
        
    #     expectedData = [["1a","2a","3a","4a","5a","6a","7a","8a","9a","10a"
    #          ,"11a","12a","13a","14a","15a","16a","17a","18a","19a","20a"]]
        
    #     expectedDataFrame = pd.DataFrame(expectedData, columns = ["_politicianId","txDate","txType","chamber","price","size","sizeRangeHigh","sizeRangeLow","value", "filingId","filingURL",
    #                                           "reportingGap", "asset.assetType", "issuer.country", "issuer.issuerName", "politician._stateId","politician.chamber",
    #                                           "politician.dob", "politician.lastName","politician.party"])
        
    #     self.assertEqual(pd.testing.assert_frame_equal(StockScraper.detailedInfo("1a"), expectedDataFrame), None)
        
        #does not work as a method because we are using the id to query website. revise