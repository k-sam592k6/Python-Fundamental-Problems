def speed(sdis,stime):
    return sdis / stime

def distance(dspeed,dtime):
    return dspeed * dtime

def time(tdis, tspeed):
    return tdis / tspeed

print("What do you want to calculate: ")
print("1.Speed")
print("2. Distance")
print("3. Time")

choice = int(input("Enter Choice: "))
if choice == 1:
    time_to_speed = float(input("Enter Time(hours): "))
    distance_to_speed = float(input("Enter Distance(km): "))
    print(f"Speed: {speed(distance_to_speed, time_to_speed):.2f}")
elif choice == 2:
    speed_to_distance = float(input("Enter Speed(km/hr): "))
    time_to_distance = float(input("Enter Time(hr): "))
    print(f"Distance: {distance(speed_to_distance, time_to_distance):.2f}")
elif choice == 3:
    
    distance_to_time = float(input("Enter distance(km): "))
    speed_to_time = float(input("Enter Speed(km/hr): "))
    print(f"Time: {time(distance_to_time, speed_to_time):.2f}")
    
else:
    print("Wrong choice")
