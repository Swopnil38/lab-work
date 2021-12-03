'''
You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
run to university. You jog the first mile at 7mph; then run the next two at15mph; before
jogging the last at 7mph again. Will this be quicker or slower than the bus?
'''
distance = 4
bus_speed = 25/60    #converted mph to mpm(miles per minute)
wait_time = 2
stops = 10
waiting = wait_time * stops
bus_time = bus_speed * distance
bus_totaltime = bus_time + waiting

speed1 = 7/60       #converted mph to mpm(miles per minute)
speed2 = 15/60
time_7mpm = speed1*2
time_15mpm = speed2*2
jog_totaltime = time_7mpm + time_15mpm

if bus_totaltime>jog_totaltime:
    print(f"Bus will be Faster than Jogging.")
elif bus_totaltime<jog_totaltime:
    print(f"Jogging will be Faster than Travelling by Bus.")
else:
    print(f"Both Jogging and Travelling by Bus take same time.")


