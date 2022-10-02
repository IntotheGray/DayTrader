from re import S
import StockScraper # The code to test
import unittest   # The test framework
import pandas as pd
import os
os.chdir('c:/Users/Owner/Documents/GitHub/DayTrader/StockSuggester')

class Test_GetIds(unittest.TestCase):
#    data = [['Andy', 7, 'A', 'Alabama', 'House'],
#            ['Elizabeth', 0, 'E', 'Florida' , 'Senate'],
#            ['cArry', 19, 'C', 'California' , 'Senate'],
#            ['Draven', 11, 'D', 'Delaware', 'House'],
#            ['Ben', 2, 'E', 'Maine', 'Senate']]
    
#    dataframe = pd.DataFrame(
#        data, columns = ['Name', '_politicianId', 'party', 'state', 'chamber']) 
    def test_getIdsGeneral(self):
        
        self.assertEqual(StockScraper.StockScraper.getIds(testData = True)[0],"F000462" )
        
        
        
    def test_getIdsLength(self):
        
        self.assertEqual(len(StockScraper.StockScraper.getIds(testData = True)), 217)
        
        
        
    def test_getIdsName(self):
        
        self.assertEqual(
            len(StockScraper.StockScraper.getIds(name = "ben", testData = True)), 6)
        
        
        
    def test_getIdsTerminalName(self):
        
        self.assertEqual(
            len(StockScraper.StockScraper.getIds(name = "jeff", testData = True)), 4)
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(name = "jeff", testData = True)[0], "C001053")
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(name = "jeff",testData = True)[-1], "F000449")
        

        
    def test_getIdsParty(self):
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(party = "democrat",testData = True)[0], "F000462")
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(party = "democrat",testData = True)[-1], "L000557")
        
        
        
    def test_getIdsState(self):
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(state = "ut",testData = True)[0], "C001114")
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(state = "Utah",testData = True)[0], "C001114")
                
        self.assertEqual(
            StockScraper.StockScraper.getIds(state = "utah",testData = True)[0], "C001114")
                  
                  
                  
    def test_getIdsChamber(self):
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(chamber = "house",testData = True)[0], "F000462")
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(chamber = "house",testData = True)[-1], "F000449")
    
    
    
    def test_getIdsGender(self):
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(gender = 'female',testData = True)[0], 'F000462')
        
        self.assertEqual(
            StockScraper.StockScraper.getIds(gender = 'female',testData = True)[-1], 'B001284')        
    
    def test_getIdsMultipleArgs(self):
        self.assertEqual(
        StockScraper.StockScraper.getIds(
            name = 'x', party = 'republican', state = 'tn', 
            gender = 'male', chamber = 'senate' ,testData = True)[0], 'A000360')
        
        #self.assertEqual()
        
        
        
if __name__ == '__main__':
    #os.chdir('c:/Users/Owner/Documents/GitHub/DayTrader/StockSuggester')
    print(os.getcwd())
    unittest.main()