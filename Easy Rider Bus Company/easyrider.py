import json
import re
import sys


json_str = input()
str_ = json.loads(json_str)
errors_count = 0
bus_id_err = 0
stop_id_err = 0
stop_name_err = 0
next_stop_err = 0
stop_type_err = 0
a_time_err = 0
bus_id = []
dicts = []
start_stops = []
finish_stops = []
transfer_stops = set()
for i in range(len(str_)):
    if not isinstance(str_[i]['stop_name'], str) or len(str_[i]['stop_name']) < 1 or \
            re.match(r'([A-Z]\w+ )+(Road|Avenue|Boulevard|Street)$', str_[i]['stop_name']) is None:
        errors_count += 1
        stop_name_err += 1
    if str_[i]['stop_type'] == '':
        pass
    else:

        if not isinstance(str_[i]['stop_type'], str) or re.match(r'^[SOF]$', str_[i]['stop_type']) is None:
            errors_count += 1
            stop_type_err += 1

    if not isinstance(str_[i]['a_time'], str) or len(str_[i]['a_time']) < 5 or\
            re.match(r'([01]\d:[0-5]\d)$|(2[0-3]:[0-5]\d)$', str_[i]['a_time']) is None:
        errors_count += 1
        a_time_err += 1
if errors_count > 0:
    print('Type and required field validation: {}'.format(errors_count))
    print('stop_name: {}'.format(stop_name_err))
    print('stop_type: {}'.format(stop_type_err))
    print('a_time: {}'.format(a_time_err))

for i in enumerate(str_):

    if i[1]['bus_id'] not in bus_id:
        bus_id.append(i[1]['bus_id'])
for j in enumerate(bus_id):
    stops_amount = 0
    stops_name = []
    start_stop = False
    finish_stop = False
    for i in enumerate(str_):
        if i[1]['bus_id'] == j[1]:
            if i[1]['stop_name'] not in stops_name:
                if i[1]['stop_type'] == 'S':
                    start_stop = True
                    start_stops.append(i[1]['stop_name'])
                elif i[1]['stop_type'] == 'F':
                    finish_stop = True
                    finish_stops.append(i[1]['stop_name'])
                stops_name.append(i[1]['stop_name'])
                stops_amount += 1

    if not start_stop & finish_stop:
        print('There is no start or end stop for the line: {}'.format(j[1]))
        sys.exit()
    dicts.append({'bus_id': j[1], 'stops': stops_name})

# print('Line names and number of stops:')

# for i in enumerate(dicts):
#     print('bus_id: {} stop_names: {}'.format(i[1]['bus_id'], i[1]['stops']))

# comb = list(itertools.combinations(dicts, 2))
#
# for i in enumerate(comb):
#     transfer_stops |= set(i[1][0]['stops']) & set(i[1][1]['stops'])
# start_set = set(start_stops)
# finish_set = set(finish_stops)
# print('Start stops: {}'.format(len(start_set)), sorted(list(start_set)))
# print('Transfer stops: {}'.format(len(transfer_stops)), sorted(list(transfer_stops)))
# print('Finish stops: {}'.format(len(finish_set)), sorted(list(finish_set)))

# print('Arrival time test:')
# arrival_test_errors = 0
# temp_next_stop = ''
# for j in bus_id:
#     for i in enumerate(str_):
#         if i[1]['bus_id'] == j:
#             if i[1]['stop_id'] == temp_next_stop:
#                 if i[1]['bus_id'] == prev_bus_id:
#
#                     if i[1]['a_time'] <= temps_curr_time:
#                         print('bus_id line {}: wrong time on station {}'.format(i[1]['bus_id'], i[1]['stop_name']))
#                         arrival_test_errors += 1
#                         break
#             temp_next_stop = i[1]['next_stop']
#             temps_curr_time = i[1]['a_time']
#             prev_bus_id = i[1]['bus_id']
#
#
# if arrival_test_errors == 0:
#     print('OK')


print('On demand stops test:')
on_demand_stops = []
for i in enumerate(str_):
    if i[1]['stop_type'] == 'O':
        on_demand_stops.append(i[1]['stop_name'])
for j in on_demand_stops:
    stops_count = 0
    for i in enumerate(str_):
        if i[1]['stop_name'] == j:
            stops_count += 1
            if i[1]['stop_type'] in ['S', 'F']:
                try:
                    on_demand_stops.remove(j)
                except ValueError:
                    pass

    if stops_count < 2:
        try:
            on_demand_stops.remove(j)
        except ValueError:
            pass

if len(on_demand_stops) > 0:
    print('Wrong stop type: {}'.format(sorted(on_demand_stops)))
else:
    print('OK')




