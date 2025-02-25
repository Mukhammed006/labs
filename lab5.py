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
txt="My PP2 teacher is miss Akbota"
result=re.finditer(r"[A-Z]+[a-z]+", txt)
print(result)