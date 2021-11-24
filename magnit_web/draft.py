import re

s = "[[merit|merited]] and [[eat|eaten]] and [[go]]"
p = "\[\[[a-zA-Z]*?[|]*([a-zA-Z]*)\]\]"

print(re.sub(p, r'\1', s))
