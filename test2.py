#new file 
import re
telephone="123434"
if re.compile(r'\d+',telephone):
    print("it is match")