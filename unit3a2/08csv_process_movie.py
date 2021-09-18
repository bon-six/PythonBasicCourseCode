
import csv
import itertools
import matplotlib.pyplot
import pathlib

data_index = {'Title' : -99,
              'Year': -99,
              'Gross Earnings':-99,
              'IMDB Score':-99}



file_path = pathlib.Path('D:/Edu/program_resource/dataset')
file_name = file_path/'movies-1.csv'
file_name2 = file_path/'movies-2.csv'
file_name3 = file_path/'movies-3.csv'

file_names = [file_name, file_name2, file_name3]

filtered_data = []

with open(file_names[0],'r',encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    title_list = next(reader)
    i = 0
    for item in title_list:
        if item in data_index.keys():
            data_index[item]=i
        i+=1

for file_name in file_names:
    with open(file_name,'r',encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader) # skip the hearder row.
        for row in reader:
            filtered_data.append([row[data_index['Title']],
                                  row[data_index['Year']],
                                  row[data_index['Gross Earnings']],
                                  row[data_index['IMDB Score']] ])

''' #testing code, to output captured data, can open file to validate
with open('test.csv','w',encoding='utf-8-sig') as file:
    for item in filtered_data:
        file.write('"{0:s}","{1:s}","{2:s}","{3:s}",\n'.format(item[0],item[1],item[2],item[3]))
    file.close()
input()
'''
''' #testing code, to output captured data, can open file to validate
with open('test.csv','w',encoding='utf-8-sig',newline='') as file:
    writer = csv.writer(file)
    for item in filtered_data:
        writer.writerow(item)
    file.close()
input()
'''
''' #testing code, to check if earning data any suspicious value.
for item in filtered_data:
    if item[2]!='' and int(item[2])<10:
        print (item[0])
input()
'''

def sort_earnings(val):
    return int(val[2]) if val[2] != '' else 0
'''
def copy_data(*args):
    if len(args) == 1: # make a shallow copy and return it
        return (args[0].copy())
    elif len(args) == 2:  # do a shallow copy between 2 lists
        for i in range(len(args[1])):
            args[0][i] = args[1][i]
        return
def bubble_sort(to_sort_list,compare_func,copy_func):
    for i in range(len(to_sort_list)-1):
        change_flag=0
        for j in range(i,len(to_sort_list)):
            if compare_func(to_sort_list[j]) > compare_func(to_sort_list[j-1]):
                change_flag=1
                to_sort_list[j],to_sort_list[j-1]=to_sort_list[j-1],to_sort_list[j]
        if change_flag==0:
            break
#this is self made bubble soring algorithsm.
#bubble_sort(filtered_data,sort_earnings)
'''
#this is the python list sorting algorithsm. much faster than bublle sorting
filtered_data.sort(key=sort_earnings,reverse=True)
''' #testing code, to check first 10 itmes and last 10 items after sorting.
for item in itertools.islice(filtered_data,0,10):
    print(item)
for item in itertools.islice(reversed(filtered_data),0,10):
    print(item)
'''
#found duplicate name of movies. change one to a different name.
for item in filtered_data:
    if item[0] == 'The Avengers\xa0':
        item[0]=item[0].replace('\xa0', ' ***')
        break


#top 10 selling movies to show on bar graph
movies=[]
sales=[]
for item in itertools.islice(filtered_data,0,10):
    if len(item[0])>21:
        tmp_name = item[0][:21]+'.'*3
    else:
        tmp_name = item[0]
    movies.append(tmp_name)
    sales.append(int(item[2]))
'''#test code, to show content
print(movies)
print(sales)
'''
fig = matplotlib.pyplot.figure()
ax = fig.add_axes([0.1,0.4,0.8,0.5])
ax.bar(movies,sales,width=0.2)
ax.set_title('Top 10 Sales Movies')
ax.set_xlabel('movies')
ax.set_ylabel('Earnings')
for label in ax.get_xmajorticklabels():
    label.set_rotation(45)
    label.set_ha("right")
matplotlib.pyplot.show()

def sort_years(val):
    return int(val[1]) if val[1] != '' else 0
filtered_data.sort(key=sort_years)
''' #testing code, to check first 10 itmes and last 10 items after sorting.
for item in itertools.islice(filtered_data,0,10):
    print(item)
for item in itertools.islice(reversed(filtered_data),0,10):
    print(item)
'''

#show yearly total movie sales trending graph
years = []
year_sales = []
iter_data = iter(filtered_data)
for item in iter_data:
    if item[1] == '':
        continue
    if years == [] or int(item[1]) != years[-1]:
        if item[2] != '':
            years.append(int(item[1]))
            year_sales.append(int(item[2]))
    else:
        if item[2] != '':
            year_sales[-1]+=int(item[2])
''' #test code, to have a look at the values
for item in itertools.islice(years,0,10):
    print(item)
for item in itertools.islice(year_sales,0,10):
    print(item)
for item in itertools.islice(reversed(years),0,10):
    print(item)
for item in itertools.islice(reversed(year_sales),0,10):
    print(item)
'''
fig = matplotlib.pyplot.figure()
ax = fig.add_axes([0.1,0.2,0.8,0.7])
ax.plot(years,year_sales)
ax.set_title('Yearly movie sales')
matplotlib.pyplot.show()


#show review score histogram graph
scores = []
iter_data = iter(filtered_data)
for item in iter_data:
    if item[3] == '':
        continue
    scores.append(float(item[3]))
bins=[i for i in range(0,11)]
fig = matplotlib.pyplot.figure()
ax = fig.add_axes([0.1,0.2,0.8,0.7])
ax.hist(scores,bins)
ax.set_title('IMDB score distribution')
matplotlib.pyplot.show()
