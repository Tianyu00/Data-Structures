# python3

from collections import namedtuple
import re

# didn't use
Bracket = namedtuple("Bracket", ["char", "position"])

# didn't use
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

# didn't use
def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            pass


def main():
    text = input()
    #text=re.search(r"[(){}[\]]+",text)
    #text = re.sub( r'[^(){}[\]]', '', text)
    #print(text)
    stack = []
    loc = []
    for i, char in enumerate(text):
        if char in ["(","[","{"]:
            stack.append(char)
            loc.append(i)
        else:
            if char in [')',']','}']:
                try:
                    stack_last = stack.pop()
                except:
                    print(i+1)
                    return 
                if (char == "]" and stack_last != "[") or \
                    (char == ')' and stack_last != '(') or \
                    (char == '}' and stack_last != '{'):
                    print(i+1)
                    return 
                else:
                    loc.pop()
    print('Success' if len(stack) == 0 else (loc.pop()+1))


if __name__ == "__main__":
    main()
