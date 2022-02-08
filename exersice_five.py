# return the frequency of a in the substring

def repeated_string(string: str, num: int):
    count_a = string.count("a")
    div_len = count_a * (num // len(string))
    remains = num % len(string)
    remeains_str = string[:remains].count("a")
    # print('ss', string[:remains].count("a"))
    # print('sa', string[:remains])
    return div_len + remeains_str


s = input('Enter a string to repeat:')
n = int(input('Enter the number of characters to consider:').strip())

result = repeated_string(s, n)
print(result)
