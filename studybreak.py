import webbrowser #this is abstraction
import time


# make my program wait 

total_breaks = 5
break_count = 0

print("This program started on "+time.ctime()) # bring in the current time function
while(break_count < total_breaks):
	time.sleep(10)
	webbrowser.open("https://www.netflix.com") 
	break_count = break_count + 1
#add a loop to this code so it prompts the user to take 5 breaks