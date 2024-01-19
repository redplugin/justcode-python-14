friends = [
    {
        "name": "Ulan",
        "age": 23,
        "first_meet_year": 2010
    }, {
        "name": "Gulzat",
        "age": 21,
        "first_meet_year": 2022
    }, {
        "name": "Amir",
        "age": 25,
        "first_meet_year": 2018
    }

]
# 'name', 'location',
# 'day_ago', 'month_ago' or 'year_ago'
meetings = [
    {
        'name': 'Ulan',
        'location': 'Medeu',
        'month_ago': 2
    }, {
        'name': 'Gulzat',
        'location': 'Mega',
        'day_ago': 5
    }, {
        'name': 'Ulan',
        'location': 'Mega',
        'day_ago': 2
    }, {
        'name': 'Amir',
        'location': 'mesto1',
        'year_ago': 2
    }

]

# 1
# current_year = 2023
# for friend in friends:
#     if current_year - friend['first_meet_year'] >= 2:
#         print(friend)


#2
# for meeting in meetings:
#     if meeting.get('year_ago') != None and meeting.get('year_ago') > 1:
#         print(meeting)


#5
cnt = {}
for meeting in meetings:
    location = meeting.get('location')
    if cnt.get(location):
        cnt[location] = cnt[location] + 1
    else:
        cnt[location] = 1

print(cnt)