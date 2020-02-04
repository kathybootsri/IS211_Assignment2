# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:52:18 2020

@author: kbootsri
"""

def main():
    import argparse
    import sys
 
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv", type=str)
    args = parser.parse_args()
    if (args.input == None and args.length == None):
        sys.exit()    

        
if __name__ == "__main__":
    
    """PART II: DOWNLOAD DATA FUNCTION"""
        
    def downloadData(url):
        import urllib.request
        import pandas as pd
        from io import StringIO
        
        global df
        
        response = urllib.request.urlopen(url)
        html = response.read()
        
        s=str(html,'utf-8')
        
        data = StringIO(s) 
        
        df=pd.read_csv(data)
    
    """PART III: FUNCTION TO PROCESS DATA"""
    
    def processData(df):   
        
        downloadData(url)
        
        import logging
        global dict 
        
        LOG_FILENAME = 'errors.log'
        logging.basicConfig(filename=LOG_FILENAME, level=logging.ERROR)
        
        dict = {}
        for ind in df.index: 
            import datetime
            
            try:
                i = df['id'][ind]
                n = df['name'][ind]
                b = df['birthday'][ind]
                converted_date = datetime.datetime.strptime(b, '%d/%m/%Y').strftime("%x")
    #            d = datetime.date.converted_date
                dict.update({i: (n, converted_date)})
            except Exception as e: 
                i = df['id'][ind]
                row = df.index[i]
                
                logging.error("Error processing line # {} for ID# {}: Exception Detail: {}".format(row, i, e), exc_info=True)
                pass
            
        print(dict)
    
    """PART IV: RETRIEVE ID ATTRIBUTES AND FORMAT AS PRINT VALUE"""
    
    def displayPerson(id):
        import sys
        
        processData(df)
        if id <= 0:
            sys.exit()
        else:
            try:
                print("Person #{} is {} with a birthday of {}".format(id, dict[id][0], dict[id][1]))
            except KeyError:
                print("No user found with that id")
                pass
    

"""TEST FUNCTIONS"""

url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'

downloadData(url)
processData(df)
displayPerson(3)