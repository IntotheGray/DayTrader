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
    
    Andy2 = Andy

    Elizabeth = Politician(elizaDf)
    
    Carry = Politician(carryDf)
    
    Draven = Politician(dravDf)
    
    Ben = Politician(benDf)
            
    def test_unloadDataframe(self):
        
        correctDf = pd.DataFrame([['Andy', 7, 'A', 'Alabama', 'House']],columns = ['Name', '_politicianId', 'party', 'state', 'chamber']) #test we are grabbing the correct dataframe
        
        self.assertEqual(pd.testing.assert_frame_equal(self.Andy.dataframe, correctDf),None) #tests the dataframes are equal
        
        self.assertEqual(self.Andy.Name, 'Andy' ) #tests the attributes are properly set
        
        self.assertEqual(self.Andy._politicianId, 7)
        
        self.assertEqual(self.Andy.party,'A')
        
        self.assertEqual(self.Andy.state,"Alabama")
        
        self.assertEqual(self.Andy.chamber, 'House')
        
        
    def test_changeAttr(self):
        
        self.assertRaises(AttributeError,
            self.Andy2.changeAttr, ("Not an attribute"), ("Shouldn't be value"))
        
        self.Andy2.changeAttr("Name", "Amdy")
        
        self.assertEqual(self.Andy2.Name, "Amdy")
    
    
    
    def test_hasAttr(self):
    
        self.assertEqual(self.Andy.hasAttr("Name"), True)
        
        self.assertEqual(self.Andy.hasAttr("Not an attribute"), False)
    
    
    def test_removeAttr(self):
        
        self.assertEqual(self.Andy2.hasAttr("Name"), True)
        
        self.Andy2.removeAttr("Name")
        
        self.assertEqual(self.Andy2.hasAttr("Name"), False)
        
        
        
    def test_addAttr(self):
        
        self.assertEqual(self.Andy2.hasAttr("Height"), False)
        
        self.Andy2.addAttr("Height", "165")
        
        self.assertEqual(self.Andy2.hasAttr("Height"), True)
    
    
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