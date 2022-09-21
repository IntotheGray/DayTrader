import StockScraper    # The code to test
import unittest   # The test framework

class Test_DetailedInfo(unittest.TestCase):
    
    def test_grabPolitician(self): #Test is returning Politician A dataframe from Politcian A arg
        self.assertEqual(
            StockScraper.StockScraper.detailedInfo("F000462"), )   
        
        