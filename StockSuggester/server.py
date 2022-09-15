from flask import Flask,request
import StockScraper as ss

app = Flask(__name__)

@app.post('/')
def hello_worldPlus():
    
    data = request.get_json()
    
    data_name = data['name']
    
    peopleWithXInThereNameSuckDick = ss.StockScraper.getIds(name = data_name)

    return f"The names are: /n {peopleWithXInThereNameSuckDick}"

@app.post('/ids')
def hello_worldMinus():
    
    data = request.get_json()
    
    data_name = data['name']
    
    peopleWithXInThereNameSuckDick = ss.StockScraper.getIds(name = data_name)

    return f"The Politcian IDs are: {peopleWithXInThereNameSuckDick}"