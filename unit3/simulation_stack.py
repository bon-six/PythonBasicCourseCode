import random


stack = []
finished = []

total_files = 0
current_day = 0
time = 0
processing_event = 0

def sort_time(e):
    return e[2]    # to sort according to arrive time

while len(finished)<100:
    # generate event and add to top of stack
    # every day comes randomly 2~10 files wair for process.
    if time == 0:
        arrives=[]
        files = random.randint(2,10)
        for i in range(files):
            arrive_time = random.randint(0,11) # a random time of file arrives
            total_files+=1
            arrives.append([total_files,current_day,arrive_time,-1,0])
        arrives.sort(key=sort_time)
    
    while arrives:
        item = arrives.pop(0)
        if item[2] <= time:
            stack.append(item)
        else:
            arrives.insert(0,item)
            break

    # take event from stack top and do process
    if time < 11:
        time += 1
    else:
        current_day+=1
        time = 0

    if processing_event:
        process_time = processing_event[4]
    else:
        if stack:
            processing_event = stack.pop(-1)
            process_time = random.randint(1,3)

    if processing_event:
        process_time -= 1
        if process_time ==0:
            processing_event[3] = current_day
            processing_event[4] = time
            finished.append(processing_event)
            processing_event=0
        else:
            processing_event[3] = current_day
            processing_event[4] = process_time
    
            
# process the data
for item in finished:
    print(item)
