def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
    global cur_hedons, cur_health

    global cur_time, over_bound
    global last_activity, last_activity_duration, prev_health, prev_hedons
    global cur_star, cur_star_activity, offer_times
    global is_tired, stored_dur, stored_health, stored_hedons
    
    global last_finished
    global bored_with_stars
    
    cur_time, cur_hedons, cur_health = 0, 0, 0
    over_bound = False
    
    is_tired = False
    stored_dur, stored_health, stored_hedons = 0, 0, 0
    cur_star = False
    cur_star_activity = ""
    offer_times = []
    
    bored_with_stars = False
    
    last_activity = ""
    last_activity_duration, prev_health, prev_hedons = 0, 0, 0
    
    last_finished = -1000
    

def perform_activity(activity, duration):
    global cur_time, cur_hedons, cur_health, cur_star, cur_star_activity, last_activity, over_bound, stored_dur, stored_health, stored_hedons, prev_health, prev_hedons, last_activity_duration
    if(duration > 0):
        # last_activity_duration is swapped with previous duration before stored_dur updates
        last_activity_duration, stored_dur = stored_dur, last_activity_duration
        stored_dur = duration
        # still is prev cur_health and cur_hedons because it will in the following if operations.
        stored_health = cur_health
        prev_health, stored_health = stored_health, prev_health
        stored_hedons = cur_hedons
        prev_hedons, stored_hedons = stored_hedons, prev_hedons
        cur_time += duration
        check_tiredness()
        star_can_be_taken(activity) # checks for offer_star changing cur_star

        if(activity == "running"):
            # check_tiredness() runs before last activity is updated
            # print(str(last_activity_duration) + "LOOK")
            if(last_activity == "running"):
                if(over_bound == False):
                    if(duration + last_activity_duration <= 180):
                        cur_health += 3 * duration
                    #20, 170
                    else:
                        over_bound = True
                        cur_health += 3 * (180 - last_activity_duration) + duration + last_activity_duration - 180
                else:
                    cur_health += duration
            else:
                over_bound = False
                if(duration <= 180):
                    cur_health += 3 * duration
                else:
                    cur_health += 3 * 180 + duration - 180
            last_activity = "running"
            if(is_tired == True):
                cur_hedons += -2 * duration
                # check's cur_star and adds hedons accordingly
                give_star_hedons(duration)
            elif(is_tired == False): 
                if(duration <= 10):
                    cur_hedons += (2 * duration)
                else:
                    cur_hedons += (2 * 10) + (-2 * (duration - 10))
                give_star_hedons(duration)
        elif(activity == "textbooks"):
            last_activity = "textbooks"
            cur_health += 2 * duration
            if(is_tired == True):
                # print(str(cur_hedons) + "LOOK")
                cur_hedons += -2 * duration
                give_star_hedons(duration)
            elif(is_tired == False): 
                if(duration <= 20):
                    cur_hedons += (1 * duration)
                else:
                    cur_hedons += (1 * 20) + (-1 * (duration - 20))
                give_star_hedons(duration)
        elif(activity == "resting"):
            last_activity = "resting"
        else:
            pass
        # Reset cur_star every time since it can only be activated once\
        cur_star = False
        cur_star_activity = ""
    else:
        pass

def undo_activity():
    global cur_time, cur_hedons, cur_health, last_activity_duration, prev_health, prev_hedons
    cur_time -= last_activity_duration
    cur_health = prev_health
    cur_hedons = prev_hedons

def get_cur_hedons():
    global cur_hedons
    return cur_hedons
    
def get_cur_health():
    global cur_health
    return cur_health
    
def star_can_be_taken(activity):
    global cur_star, cur_star_activity
    if(cur_star_activity == activity):
        cur_star = True
    else:
        cur_star = False

def offer_star(activity):
    global cur_star_activity, cur_time, bored_with_stars, offer_times
    cur_star_activity = activity

    offer_times.append(cur_time)
    num_time = len(offer_times)
    if(bored_with_stars == False):
        if((num_time) > 2):
            print(offer_times)
            if((offer_times[num_time - 1] - offer_times[num_time - 3]) < 120):
                bored_with_stars = True
            else: 
                bored_with_stars = False
    

def give_star_hedons(duration):
    global cur_hedons, cur_star, cur_star_activity, bored_with_stars
    if ((cur_star == True) and (bored_with_stars == False)):
        if(duration >= 10):
            cur_hedons += 3 * 10
        else:
            cur_hedons += 3 * (duration % 10)
        
def most_fun_activity_minute():
    # Need to test perform_acitivity on a clone
    global cur_star_activity
    if(cur_star_activity == ""):
        activities = ["running", "textbooks", "resting"]
    else:
        if(cur_star_activity == "running"):
            activities = ["running", "textbooks", "resting"]
        elif(cur_star_activity == "textbooks"):
            activities = ["textbooks", "running", "resting"]

    max_hedons = -100000
    index = 0
    for i in range(len(activities)):
        perform_activity(activities[i], 1)
        current = get_cur_hedons()
        undo_activity()
        if(current > max_hedons):
            max_hedons = current
            index = i
    return activities[index]

def check_tiredness():
    global last_activity, last_activity_duration, is_tired
    if(last_activity  == "running" or last_activity == "textbooks"):
        is_tired = True
    elif(last_activity == "resting"):
        if(last_activity_duration < 120):
            is_tired = True
        else:
            is_tired = False
        
if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)    
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)  
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10

