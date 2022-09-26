from cgi import test
import StockScraper   # The code to test
import unittest   # The test framework
import pandas as pd

class Test_SearchColumn(unittest.TestCase):

    data = [['Andy', 7, 'A'],['Elizabeth', 0, 'E' ],
            ['cArry', 19, 'C' ],['Draven', 11, 'D'],['Ben', 2, 'E']]
    
    dataframe = pd.DataFrame(data, columns = ['Name', '_politicianId', 'party'])
    
    
    
    def test_searchColumnName1(self):

        #Test that searchColumn can actually search and find names and
        #and return their politician ID
        self.assertEqual(StockScraper.StockScraper.searchColumn(
            Test_SearchColumn.dataframe,'Name','Andy'),[7] )
    
    def test_searchColumnName2(self):    
        #Test that searchColumn can return a full list of politicians that apply
        self.assertEqual(StockScraper.StockScraper.searchColumn(
            Test_SearchColumn.dataframe,'Name','a'),[7, 0, 19, 11] )
        
    def test_searchColumnName3(self):     
        #Test that searchColumn can find names in different locations within the dataframe    
        self.assertEqual(StockScraper.StockScraper.searchColumn(
            Test_SearchColumn.dataframe,'Name','Draven'),[11] )
        
    def test_searchColumnName4(self):       
        #Test that searchColumn properly handles values that are not within the list
        self.assertRaises(ValueError, StockScraper.StockScraper.searchColumn,
            Test_SearchColumn.dataframe, 'Name', "David")
    
    
    
    def test_searchColumnNameCapitols1(self):
        
        #Test that searchColumn can handle lowercase
        self.assertEqual(StockScraper.StockScraper.searchColumn(
            Test_SearchColumn.dataframe, 'Name','andy'),[7])

    def test_searchColumnNameCapitols2(self):    
        #Test that searchColumn can handle random capitols mid word
        self.assertEqual(StockScraper.StockScraper.searchColumn(
            Test_SearchColumn.dataframe, 'Name', 'carRy'),[19])
        
        
        
    def test_searchColumnOtherCategorySearch(self):
        
        #Test that searchColumn works with other categories. This also handles multiple outputs found.
        self.assertEqual(StockScraper.StockScraper.searchColumn(
            Test_SearchColumn.dataframe, 'party', 'E'), [0,2])
    
    
    
    def test_searchColumnReturnDataFrame(self):
        
        answerData = [['Andy',7,'A']]
        answerDf = pd.DataFrame(answerData, columns = ['Name', '_politicianId','party'])
        
        #Test that search column returnDataFrame has the desired effect when true
        self.assertEqual(pd.testing.assert_frame_equal(StockScraper.StockScraper.searchColumn(
            Test_SearchColumn.dataframe, 'party', 'A', True)[0],answerDf),None)
        
        
if __name__ == '__main__':

    unittest.main()

    