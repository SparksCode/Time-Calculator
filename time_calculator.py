def flip_merediem(merediem):
  if merediem == 'PM':
    merediem = 'AM' 
  else:
    merediem = 'PM'
  return merediem

def add_time(start, duration, day=False):
  #No Change
  if duration == '0:00':
    return start

  days = 0
  duration_hour = duration.partition(":")[0]
  duration_minutes = duration.partition(":")[2]
  merediem = start.split()[1]
  new_hour = 0
  new_minutes = 0
  start_hour = start.split()[0].partition(":")[0]
  start_minutes = start.split()[0].partition(":")[2]
  day_map={
    'Monday': 0, 
    'Tuesday': 1, 
    'Wednesday': 2, 
    'Thursday': 3, 
    'Friday': 4, 
    'Saturday': 5, 
    'Sunday': 6
  }

  #Find Minutes 
  try:
    new_minutes += int(start_minutes) + int(duration_minutes)
  except:
    return "Minutes Error"

  if (new_minutes > 60):
    new_hour += 1
    new_minutes -= 60

  #Find Days
  try:
    days = (new_hour + int(duration_hour)) // 24
    if int(duration_hour) % 24 > 12:
      days = days
  except:
    return "Days Error"

  #Find Hours
  try:
    combined_hour = (new_hour + int(start_hour) + int(duration_hour))
    if combined_hour != 12:
      new_hour =  combined_hour % 12
      if new_hour == 0:
        new_hour = 12
    else:
      new_hour = combined_hour
    if combined_hour >= 12 and (combined_hour // 12) % 2 > 0:
      merediem = flip_merediem(merediem)
      if merediem == 'AM':
        days += 1
  except:
    return "Hours Error"

  #Find Day
  if day != False:
    try:
      day = list(day_map.keys())[list(day_map.values()).index((day_map[day.lower().capitalize()] + days) % 7)]
    except:
      return "Day Error"

  #Build new_time and return
  new_time = f"{str(new_hour)}:{str(new_minutes).zfill(2)} {merediem}"
  if day != False:
    new_time += f", {day}"
  if days == 1:
    new_time += " (next day)"
  elif days > 1:
    new_time += f" ({str(days)} days later)"

  return new_time