import requests

fact_list = []
def cats_fact(num):
    while num == 0:
        num -= 1
        request = requests.get('https://catfact.ninja/fact').json()['fact']
        print(request)
        if request not in fact_list:
            fact_list.append(request)

cats_fact(5)


print(fact_list)
