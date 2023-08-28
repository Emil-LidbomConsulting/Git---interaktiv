
#import module
import pandas as pd


mandatory, results = pd.read_csv((r"Git---interaktiv\1 - Python\Obligatorisk\ObligatoriskaMediaKurser.csv"), names= 
                       ["Course_code","Course_name", "Points"], sep=";"), pd.read_csv((r"Git---interaktiv\1 - Python\Obligatorisk\Studieresultat.csv"), sep=";", names= [i for i in range(17)])
                    
#print(mandatory.Course_code)
print(results)