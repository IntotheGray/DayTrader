import StockScraper
import pandas as pd

class Politician:
    """ An object containing all the data of the politician dataframe passed through."""
    
    def __init__(self, dataframe):
        
        self.dataframe = dataframe
        
        variableNames = self.dataframe.columns.tolist()
        
        valuesList = self.dataframe.values[0]
        
        for columns, values in zip(variableNames, valuesList):
            
            #print("Column Added:\t", columns, "\tValue Added:\t", values)
            setattr(self, columns, values)
            

                    

if __name__ == "__main__":
    data = [['Andy', 7, 'A', 'Alabama', 'House'],
            ['Elizabeth', 0, 'E', 'Florida' , 'Senate'],
            ['cArry', 19, 'C', 'California' , 'Senate'],
            ['Draven', 11, 'D', 'Delaware', 'House'],
            ['Ben', 2, 'E', 'Maine', 'Senate']]
    
    testDataframe = pd.DataFrame(
        data, columns = ['Name', '_politicianId', 'party', 'state', 'chamber'])
    
    Andy = Politician(testDataframe.iloc[[0]])