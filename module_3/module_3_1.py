calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    len_str = len(string)
    up_str = string.upper()
    tup_str = (len_str, up_str)
    return tup_str


def is_contains(string, list_to_search):
    count_calls()
    return
