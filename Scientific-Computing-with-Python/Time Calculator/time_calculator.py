
def add_time(start, duration, starting_day = None):

  day_of_the_week = {'sunday':1, 'monday':2 , 'tuesday':3, 'wednesday':4, 'thursday':5, 'friday':6, 'saturday':7}
  AMPM = {'AM':1,'PM':-1}

  start = start.replace(" ","")
  semicolon_location = start.find(":")
  AMPM_location = start.find("M")
  start_hour = int(start[0:semicolon_location])
  start_minute = int(start[(semicolon_location+1):(AMPM_location-1)])
  start_AMPM = start[(AMPM_location-1):]

  duration_time = duration.split(':')
  duration_day = 0
  duration_time = list(map(int,duration_time))
  duration_hour = duration_time[0]
  duration_minute = duration_time[1]

  if start_AMPM == 'AM':
    pass
  elif start_AMPM == 'PM':
    start_hour += 12

  new_time_hour = start_hour + duration_hour
  new_time_minute = start_minute + duration_minute
  
  if new_time_minute >= 60:
    new_time_minute -= 60
    new_time_hour+=1

  new_time_hour_formatted = new_time_hour % 24 

  if new_time_hour_formatted > 12: 
    new_AMPM = 'PM'
    new_time_hour_formatted -= 12
  elif new_time_hour_formatted == 12:
    new_AMPM = 'PM'
  elif new_time_hour_formatted == 0:
    new_time_hour_formatted = 12
    new_AMPM = 'AM'
  else: 
    new_AMPM = 'AM'
    
  days_elapsed = int(new_time_hour/24)
  new_day = ""
  
  if starting_day != None:
    starting_day = day_of_the_week.get(starting_day.lower())
    new_day = starting_day + days_elapsed
    if new_day > 7:
      new_day = new_day%7
    else:
      new_day = new_day
    for day, value in day_of_the_week.items():
      if value == new_day:
        new_day = ', ' + day.capitalize()

  if days_elapsed == 0:
    new_time = '{:}:{:0>2} {}{}'.format(new_time_hour_formatted,new_time_minute,new_AMPM,new_day)
  elif days_elapsed == 1:
    new_time = '{:}:{:0>2} {}{} (next day)'.format(new_time_hour_formatted,new_time_minute,new_AMPM,new_day)
  elif days_elapsed > 1:
    new_time = '{:}:{:0>2} {}{} ({} days later)'.format(new_time_hour_formatted,new_time_minute,new_AMPM,new_day,days_elapsed)

   
  
  return new_time