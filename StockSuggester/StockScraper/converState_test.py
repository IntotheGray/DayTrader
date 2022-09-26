import StockScraper   # The code to test
import unittest   # The test framework

class Test_ConvertState(unittest.TestCase):
    
    def test_convertState(self):
        
        self.assertEqual(
            StockScraper.StockScraper.convertState('floRida'), 'FL')
        
        self.assertEqual(
            StockScraper.StockScraper.convertState('fl'), 'Florida')
        
        self.assertRaises(
            ValueError, StockScraper.StockScraper.convertState, 'Not A State')    