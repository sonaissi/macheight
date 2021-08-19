import sys, json, urllib.request
url="https://mach-eight.uc.r.appspot.com"

if len(sys.argv) < 2:
    print("No Argument Submitted! Please try again (ex: python app.py 150)")
    exit(0)

sum=int(sys.argv[1])


response = urllib.request.urlopen(url)
data = json.loads(response.read())

#dump dict into a list
players=data['values']

#sort the list
def Sort(list):
    list.sort(key = lambda x: x['h_in'])
    return list

sorted_players=Sort(players)
length = len(sorted_players)

#declare two indices to iterate the sorted list
left=0
right=length-1

#list of positive results
results = []
list_to_append = []


while left<right:
    if (int(sorted_players[left]['h_in']) + int(sorted_players[right]['h_in']) == sum):   
        list_to_append = [left,right]
        results.append(list_to_append)
        right=right-1
    elif (int(sorted_players[left]['h_in']) + int(sorted_players[right]['h_in']) < sum):
        left = left+1
    else:
        right = right-1

#length of results list
res_length = len(results)

if (res_length == 0):
    print("No Matches found")
else:
    space= ' '
    for i in range(res_length):
        print("-"+space+sorted_players[(results[i][0])]['first_name']+space+sorted_players[(results[i][0])]['last_name']+7*space+sorted_players[(results[i][1])]['first_name']+space+sorted_players[(results[i][1])]['last_name'])
