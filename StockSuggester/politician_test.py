from tokenize import Name
from Politician import Politician
import unittest
import pandas as pd

class Test_Politician(unittest.TestCase):
    
    data = [['Andy', 7, 'A', 'Alabama', 'House'],
            ['Elizabeth', 0, 'E', 'Florida' , 'Senate'],
            ['cArry', 19, 'C', 'California' , 'Senate'],
            ['Draven', 11, 'D', 'Delaware', 'House'],
            ['Ben', 2, 'E', 'Maine', 'Senate']]
    
    testDataframe = pd.DataFrame(
        data, columns = ['Name', '_politicianId', 'party', 'state', 'chamber'])

    andyDf = testDataframe.iloc[[0]]
    
    elizaDf = testDataframe.iloc[[0]]
    
    carryDf = testDataframe.iloc[[0]]
    
    dravDf = testDataframe.iloc[[0]]
    
    benDf = testDataframe.iloc[[0]]
        
    Andy = Politician(andyDf)

    Elizabeth = Politician(elizaDf)
    
    Carry = Politician(carryDf)
    
    Draven = Politician(dravDf)
    
    Ben = Politician(benDf)
            
    def test_unloadDataframe(self):
        
        correctDf = pd.DataFrame([['Andy', 7, 'A', 'Alabama', 'House']],columns = ['Name', '_politicianId', 'party', 'state', 'chamber']) #test we are grabbing the correct dataframe
        self.assertEqual(pd.testing.assert_frame_equal(self.Andy.dataframe, correctDf),None)
        
        self.assertEqual(self.Andy.Name, 'Andy' )
        
        self.assertEqual(self.Andy._politicianId, 7)
        
        
if __name__ == "__main__":
    
    data = [['Andy', 7, 'A', 'Alabama', 'House'],
            ['Elizabeth', 0, 'E', 'Florida' , 'Senate'],
            ['cArry', 19, 'C', 'California' , 'Senate'],
            ['Draven', 11, 'D', 'Delaware', 'House'],
            ['Ben', 2, 'E', 'Maine', 'Senate']]
    
    testDataframe = pd.DataFrame(
        data, columns = ['Name', '_politicianId', 'party', 'state', 'chamber'])
    
    #unittest.main()      
    Andy = Politician(testDataframe.iloc[[0]])
    #print(Andy.dataframe.values[0])
    #print(Andy.dataframe.columns.tolist())
    
    # for column, value in zip(Andy.dataframe.columns.tolist(), Andy.dataframe.values[0]):
    #     exec(column + " = value")
    # print("\n\n\n\n\n\n\n\n")
    # print("Thinks it's not a variable, but it is: ",_politicianId)