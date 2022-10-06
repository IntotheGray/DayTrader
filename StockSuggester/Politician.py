import StockScraper
import pandas as pd

class Politician:
    """ An object containing all the data of the politician dataframe passed through."""
    
    def __init__(self, dataframe): 
        "Initiating the Politician and populating attributes"
        
        self.dataframe = dataframe
        
        variableNames = self.dataframe.columns.tolist() #These two variables are to prevent having  
        valuesList = self.dataframe.values[0]           #to access dataframe every loop of for below
        
        for columns, values in zip(variableNames, valuesList):
            
            setattr(self, columns, values)
            
            
            
    def changeAttr(self, attr, value):
        """Changes an attribute's value, if an attribute is not found it will raise an Attribute error"""
        
        try:                                #Don't really need the try/except block here, consider removing when optimizing
            if not(hasattr(self, attr)): 
                raise AttributeError
            
        except AttributeError:
            raise
        
        else:
            setattr(self, attr, value)
            
            
            
    def removeAttr(self, attr):
        """Removes an attribute from Politician Object"""
        
        if(hasattr(self, attr)):
            
            delattr(self, attr)
    
    
    
    def hasAttr(self, attr):
        """Boolean method that determines if the attribute already exists"""
        
        return hasattr(self, attr)
    
    
    
    def addAttr(self, attr, value):
        "Adds the attribute value pair to objects attributes"
        
        if not (hasattr(self, attr)):
            
            setattr(self, attr, value)
            
        else:
            
            pass
        
                        

if __name__ == "__main__":
    data = [['Andy', 7, 'A', 'Alabama', 'House'],
            ['Elizabeth', 0, 'E', 'Florida' , 'Senate'],
            ['cArry', 19, 'C', 'California' , 'Senate'],
            ['Draven', 11, 'D', 'Delaware', 'House'],
            ['Ben', 2, 'E', 'Maine', 'Senate']]
    
    testDataframe = pd.DataFrame(
        data, columns = ['Name', '_politicianId', 'party', 'state', 'chamber'])
    
    Andy = Politician(testDataframe.iloc[[0]])
    
    print(Andy.changeAttr("Not a real attribute"))