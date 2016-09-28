from ics import Calendar, Event

c = Calendar()
e = Event()
e.name = "My cool event"
e.begin = '20160927 09:00'
#e.end = 20160927 09:00'
c.events.append(e)

print c.events
print e.begin.humanize()

with open('my.ics', 'w') as f:
	f.writelines(c)

