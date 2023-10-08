# stored = 1
# current = 2

# def get_last():
#     global last_activity_duration
#     return last_activity_duration

# def memory():
#     global last_activity_duration
#     global stored_dur
#     stored_dur = last_activity_duration

# def undo():
#     global last_activity_duration, stored_dur
#     last_activity_duration, stored_dur = stored_dur, last_activity_duration

# if __name__ == "__main__":
#     global last_activity_duration
#     last_activity_duration = 1
#     print(get_last())
#     memory()
#     last_activity_duration += 1
#     print(get_last())
#     undo()
#     print(get_last())

# test = [1,2,3,4,5,4,3,6,7,5,6,1,]
# max_hedons = test[0]
# for acts in test:
#     current = acts
#     if(current > max_hedons):
#         max_hedons = current

# print(max_hedons)
a,b,c=2,3,4

a,b,c=b,c,5

print(a,b,c)