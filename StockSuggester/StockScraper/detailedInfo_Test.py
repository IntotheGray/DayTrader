import StockScraper   # The code to test
import unittest   # The test framework
import pandas as pd

class Test_DetailedInfo(unittest.TestCase):
    
    data = [["iniRemove","1a","1remove","2a","3a","4a","5a","6a","7a","8a","9a","10a" #everything with "remove" represents data the detailedInfo method from StockScraper should exclude
             ,"11a","12a","13a","14a","15a","16a","17a","18a","19a","20a"],["iniRemove","1b","1remove", "2b","3b","4b","5b","6b","7b","8b","9b","10b"
             ,"11b","12b","13b","14b","15b","16b","17b","18b","19b","20b","2remove"]]
    
    dataframe = pd.DataFrame(data, columns = ["removeIni", "_politicianId","remove1","txDate","txType","chamber","price","size","sizeRangeHigh","sizeRangeLow","value", "filingId","filingURL",
                                              "reportingGap", "asset.assetType", "issuer.country", "issuer.issuerName", "politician._stateId","politician.chamber",
                                              "politician.dob", "politician.lastName","politician.party","remove2"])
    
    def test_grabPolitician(self): #Test is returning Politician "1a" dataframe from Politcian "1a" arg
        
        expectedData = [["1a","2a","3a","4a","5a","6a","7a","8a","9a","10a"
             ,"11a","12a","13a","14a","15a","16a","17a","18a","19a","20a"]]
        
        expectedDataFrame = pd.DataFrame(expectedData, columns = ["_politicianId","txDate","txType","chamber","price","size","sizeRangeHigh","sizeRangeLow","value", "filingId","filingURL",
                                              "reportingGap", "asset.assetType", "issuer.country", "issuer.issuerName", "politician._stateId","politician.chamber",
                                              "politician.dob", "politician.lastName","politician.party"])
        
        self.assertEqual(pd.testing.assert_frame_equal(StockScraper.detailedInfo("1a"), expectedDataFrame), None)
        