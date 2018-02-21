import pandas as pd
import main_module

columns = ('name','age')
contact_df = pd.DataFrame(contact_list,columns=columns)
sorted_df = contact_df.sort_values(by=['age'])
del sorted_df['age']
print (sorted_df.values)
