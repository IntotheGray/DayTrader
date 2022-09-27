from re import S
import StockScraper    # The code to test
import unittest   # The test framework
import pandas as pd

class Test_GetIds(unittest.TestCase):
#    data = [['Andy', 7, 'A', 'Alabama', 'House'],
#            ['Elizabeth', 0, 'E', 'Florida' , 'Senate'],
#            ['cArry', 19, 'C', 'California' , 'Senate'],
#            ['Draven', 11, 'D', 'Delaware', 'House'],
#            ['Ben', 2, 'E', 'Maine', 'Senate']]
    
#    dataframe = pd.DataFrame(
#        data, columns = ['Name', '_politicianId', 'party', 'state', 'chamber']) 
    def test_getIdsGeneral(self):
        
        self.assertEqual(StockScraper.StockScraper.getIds()[0],"G000563" )
        
        
        
    def test_getIdsLength(self):
        
        self.assertEqual(len(StockScraper.StockScraper.getIds()), 217)
        
        
        
    def test_getIdsName(self):
        
        self.assertEqual(
            len(StockScraper.StockScraper.getIds(name = "ben")), 6)
        
        
        
    def test_getIdsTerminalName(self):
        
        self.assertEqual(
            len(StockScraper.StockScraper.getIds(name = "jeff")), 4)
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(name = "jeff")[0], "C001053")
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(name = "jeff")[-1], "F000449")
        

        
    def test_getIdsParty(self):
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(party = "democrat")[0], "M001135")
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(party = "democrat")[-1], "L000557")
        
        
        
    def test_getIdsState(self):
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(party = "ut")[0], "C001114")
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(party = "Utah")[0], "C001114")
                
        self.assertEqual(
            StockScraper.StockScraper.getIds(party = "utah")[0], "C001114")
                  
                  
                  
    def test_getIdsChamber(self):
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(chamber = "house")[0], "G000563")
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(chamber = "house")[-1], "F000449")
    
    
    
    def test_getIdsGender(self):
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(gender = 'female')[0], 'M001135')
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(gender = 'female')[-1], 'B001284')        
    
    def test_getIdsMultipleArgs(self):
        self.assertEqual(
        StockScraper.StockScraper.getIds(
            name = 'x', party = 'republican', state = 'tn', 
            gender = 'male', chamber = 'senate' ))
        
        #self.assertEqual()
        
        
        
if __name__ == '__main__':
    unittest.main()