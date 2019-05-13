import pandas as pd

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

file1='C:/Users/vwake/Downloads/share/googleplaystore.csv'
file2 = 'C:/Users/vwake/Downloads/share/bid_requests.csv'
file3 ='C:/Users/vwake/Downloads/share/us-500.csv'


app = pd.read_csv(file1)
bidReq = pd.read_csv(file2)
user = pd.read_csv(file3)
#can add code to remove/drop columns

app_data = pd.DataFrame(app)
print(app_data)
bid_data=pd.DataFrame(bidReq)

#filtered_df= df[df.Price > df1.Price.values]

for i in range(len(bid_data.Price)):
    df2=app_data.loc[((app_data['Price']) * 1000 >= bid_data.Price.values[i]) &
                     ((app_data['Age_group'] == bid_data.Target_group.values[i]) | (app_data['Age_group'] == 'Everyone') )]
    #print(df2)
    df2.to_csv('merge.csv')


'''
for i in range(len(bid_data.Price)):
    for j in range(len(df2.Price)):
        name = (bid_data.Target_Segment.values[i]).upper()

        print("NAME",name)
        #print(df2['Category'])
        category=df2.Category.values[j].lower()
        print(category)
        genre= df2.Genres.values[j].lower()
        print(genre)
        filter_genre= df2.loc[(category.str.contains(name))| (genre.str.contains(name))]
'''
col=[]
col=(df2.columns.values)
print(col)
final = pd.DataFrame(columns=col)
for i in range(len(bid_data.Price)):
    name = (bid_data.Target_Segment.values[i])

    print("NAME",name)
    #print(df2['Category'])
    filter_genre= df2.loc[(df2['Genres'].str.contains(name, na=False, case=False))|(df2['Category'].str.contains(name, na=False, case=False))]
    #print(f'col names in filter genre {filter_genre.shape}')
    final = final.append(filter_genre,ignore_index=True)
    #print("FINALLLLLLLL",final.shape)
    #print("FINAL FILE DATAFRAME",final)


final.drop_duplicates(keep='first',inplace=True)
#final.to_csv('Final_condition.csv')


for i in range(len(final.Age_group)):
    age= final.Age_group.values[i]
    age_filter= final.loc[(final['Age_group'].str.contains(age,case=False))]
    age_filter.to_csv('agefilterd.csv')
    #print(Age_filter)

df = pd.read_csv('agefilterd.csv')

sample_data_table = FF.create_table(df.head())
py.iplot(sample_data_table, filename='age-filterd-table')