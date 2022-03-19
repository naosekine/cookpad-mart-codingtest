from cgitb import strong
import sys
import requests

url = "https://ob6la3c120.execute-api.ap-northeast-1.amazonaws.com/Prod/battle/"
args = sys.argv[1:]

def is_strong_first_monster(first_monster, second_monster):
    payload = s = '{}+{}'.format(first_monster, second_monster)
    r = requests.get(url+payload)
    
    if r.json()["winner"] == first_monster:
        return True
    else:
        return False
        
def quick_sort(arr):
    weak_arr = []
    strong_arr = []
    if len(arr) <= 1:
        return arr

    base = arr[0]
    for monster in arr[1:]:
        if is_strong_first_monster(base, monster):
            weak_arr.append(monster)
        else:
            strong_arr.append(monster)
    weak_arr = quick_sort(weak_arr)
    strong_arr = quick_sort(strong_arr)
    return weak_arr + [base] + strong_arr

if __name__ == '__main__':
    print(quick_sort(args))