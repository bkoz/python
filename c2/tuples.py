#
#
#
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = []
p_number = []
for name, number in pokemon.items():
    p_names.append(name)
    p_number.append(number)
print('p_names =', p_names)
print('p_number =', p_number)

#
#
#

track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}
track_events = []
for event in track_medal_counts.items():
    track_events.append(event[0])
print('track_events =', track_events)
