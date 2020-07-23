hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
print("Finish Time:",((hour+(mins+dura)//60)%24),":",(mins+dura)%60)