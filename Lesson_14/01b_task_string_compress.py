# Given: s = 'aabcccccaaaBBFFyyyyyyyyyy0000000aaa'
# Write generator that will output chunks of grouped characters -> 'aa' ,'b', 'ccccc' , 'aaa'

from itertools import groupby


def chunks_genarator(target_str):
    yield from [''.join(list(group)) for _, group in groupby(target_str)]


s1 = 'aabcccccaaaBBFFyyyyyyyyyy0000000aaa'
for chunk in chunks_genarator(s1):
    print(chunk)
