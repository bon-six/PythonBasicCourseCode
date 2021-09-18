import random


queue = []

finished = []

total_guest = 0
current_time_min = 0
second = 0


def sort_time(e):
    return e[2]    # to sort according to arrive seconds (time)


while len(finished)<100:

    # generate event and add to end of queue
    # every minute comes randomly 0~5 guests. time guest comes also random.
    if second == 0:
        guest_number = random.randint(0,5)
        arrives=[]
        for i in range(guest_number):
            arrive_seconds = random.randint(0,59) # a random time of guest arrives
            total_guest+=1
            arrives.append([total_guest,current_time_min,arrive_seconds,-1,0])

        arrives.sort(key=sort_time)
        queue.extend(arrives)

    # take event from queue head and do process
    while queue:
        event = queue.pop(0)
        if event[3] == -1: # for new guest check how long time to serve.
            serving_time = random.randint(15,25)
            if current_time_min == event[1] and second < event[2]:
                second = event[2]
            if second + serving_time <= 59:
                second += serving_time
                event[3] = current_time_min
                event[4] = second
                finished.append(event)
            else: #put it back for next minute to serve
                event[3] = current_time_min
                event[4] = serving_time + second - 60
                queue.insert(0,event)
                current_time_min +=1
                second = 0
                break
        else: # for last minutes guest
            serving_time = event[4]
            second += serving_time
            event[3] = current_time_min
            event[4] = second
            finished.append(event)
    else:
        current_time_min +=1
        second = 0

# process the data
for item in finished:
    print(item)
        
