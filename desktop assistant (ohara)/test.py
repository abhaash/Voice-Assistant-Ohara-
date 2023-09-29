from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H Hours, %M Minutes") 
print(current_time)