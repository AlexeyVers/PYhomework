calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    string_text = (len(string), string.upper(), string.lower())
    return string_text


def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    string = string.lower()
    result = string in list_to_search
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
