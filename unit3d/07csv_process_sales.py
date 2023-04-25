
import csv
import itertools
import matplotlib.pyplot
import datetime
import pathlib

file_path = pathlib.Path('D:/Edu/program_resource/dataset/SalesJan2009.csv')

input_data = []

with file_path.open('r') as file:
    reader = csv.reader(file)
    title_list = next(reader)
    for row in reader:
        input_data.append(row)

# to test the basic information of the data from csv file

print('row number :', len(input_data))
print('column number :', len(title_list))
for col in range(len(title_list)):
    print(title_list[col],end='\t')
print()
for row in range(10):   # first 10 rows of data
    for col in range(len(title_list)):
        print(input_data[row][col],end='\t')
    print()
for col in range(len(title_list)):
    print(type(input_data[0][col]),end='\t')
print()
input('check the 10 row of data then hit enter')


def sort_price(row):
    return int(row[2]) if row[2]!='' else 0
input_data.sort(key=sort_price,reverse=True)
for i in range(len(input_data)):
    print(input_data[i][2])
input('check the sort result accordint to transaction price in reverse order then hit enter')  # check the sort result

#top 10 transactions to show on bar graph
names=[]
sales=[]
for item in itertools.islice(input_data,0,10):
    names.append(item[4])
    sales.append(int(item[2]))

fig, ax = matplotlib.pyplot.subplots()
ax.set_position([0.15,0.3,0.8,0.6])
#fig = matplotlib.pyplot.figure()
#ax = fig.add_axes([0.15,0.3,0.8,0.6])
ax.bar(names,sales,width=0.2)
ax.set_title('Top 10 Sales')
ax.set_xlabel('Person')
ax.set_ylabel('Price')
for label in ax.get_xticklabels():
    label.set_rotation(45)
    label.set_ha('right')
matplotlib.pyplot.show()

file_name = 'output.csv'
with open(file_name,'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(title_list)
    for row in range(10):
        writer.writerow(input_data[row])
input('check the output.csv file if contain title row and 10 row data record then hit enter')
# check the output file of 10 records.


def sort_date(row):
    return datetime.datetime.strptime(row[0], '%m/%d/%Y %H:%M') if row[0] != '' else 0
input_data.sort(key=sort_date)

for i in range(len(input_data)):
    print(input_data[i][0])
input('the the date sorted result then hit enter')  # check the sort result

#show daily sales trending graph
days = []
daily_sales = []
iter_data = iter(input_data)
for item in iter_data:
    if item[0] == '':
        continue
    else:
        date = datetime.datetime.strptime(item[0], '%m/%d/%Y %H:%M').date()
    if days == [] or date != days[-1]:
        if item[2] != '':
            days.append(date)
            daily_sales.append(int(item[2]))
    else:
        if item[2] != '':
            daily_sales[-1]+=int(item[2])

fig, ax = matplotlib.pyplot.subplots()
ax.set_position([0.1,0.2,0.85,0.7])
#fig = matplotlib.pyplot.figure()
#ax = fig.add_axes([0.1,0.2,0.85,0.7])
ax.plot(days,daily_sales)
ax.set_title('Daily sales')
for label in ax.get_xticklabels():
    label.set_rotation(45)
    label.set_ha('right')
matplotlib.pyplot.show()


