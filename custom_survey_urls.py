import pandas as pd
import re

df = pd.read_csv('contacts_2.csv')

x = df.Company.str.replace('-| |\'|\.|\&|,|', 
                           '').str.lower().to_dict()

y = df['Last Name'].str.lower().to_dict()

z = df['Email Address'].to_dict()

df['collectors2'] = df.Collectors.replace(regex=r'\[or_value\]', value=x)

df.collectors2 = df.collectors2.replace(regex=r'\[ln_value\]', value=y)

df.collectors2 = df.collectors2.replace(regex=r'\[em_value\]', value=z)

df.to_csv('contacts_final2.csv')
