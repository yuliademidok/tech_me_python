import re


text = "Guest it he tears aware as. Make my no cold of need. He been past in by my hard. Warmly thrown oh he common  #future. Otherwise concealed favourite frankness on be at dashwoods defective at. Sympathize interested  #sImplicity at do projecting increasing terminated. As edward settle limits at  in."

pattern = re.compile(r"#\w+")

for i in pattern.findall(text):
    print(i.lower())

print(pattern.findall(text.lower()))
