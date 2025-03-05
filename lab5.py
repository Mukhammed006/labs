#Ex1 
import re
txt="The rabbit swiftly hopped across the grassy field."
pattern="ab*"

result=re.findall(pattern, txt)
print(result)

#Ex2
import re
txt="She decided to abbborate her notebook with glitter and stickers"
result=re.findall("ab{2,3}",txt)
print(result)

#Ex3
import re

txt="The variable name must_use_underscores in_python."

result=re.findall(r"[a-z]+(?:_[a-z]+)+", txt)
print(result)

#Ex4
import re
txt="My PP2 teacher is mister Saduakas"
results=re.finditer(r"[A-Z]+[a-z]+", txt)
print(result)

for result in results:
    print(result)

#Ex5 
import re
txt="She put the kebab on the grill."
result=re.findall(r"\b\w*a\w*b\b", txt)
print(result)

#Ex6
import re
txt="KBTU is the best university, and historical building."
pattern=r"[ ,.]"
replace=":"
result=re.sub(pattern, replace, txt)
print(result)

#Ex7
import re

def convert(txt):
    words=re.split(r'_', txt)
    camel=words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel
snake="hello_world_example"
camel=convert(snake)
print(camel)

#Ex8
import re
txt="AtyrauILoveYou MissYou"
result=re.sub(r"(?=[A-Z])", " ", txt).strip()
print(result)

#Ex9
import re

txt="WeLoveKazakhstan"

result=re.sub(r"(?<!^)(?=[A-Z])", " ", txt)
print(result)

#Ex10
import re
def convert(txt):
    snake=re.sub(r'(?<!^)(?=[A-Z])', '_', txt)
    return snake

txt="CamelCaseText"
print(convert(txt))