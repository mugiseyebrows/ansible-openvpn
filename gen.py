import enum
import os
import re

"""
This script generates echo / cat command sequence from client.j2 to inline certs and keys in ovpn file
"""

base = os.path.dirname(__file__)

src = os.path.join(base, "client.j2")
with open(src) as f:
    lines = f.readlines()

for i,line in enumerate(lines):
    m = re.match("ca\\s+", line)
    if m:
        lines[i] = "<ca>\\ncat(pki/ca.crt)\\n</ca>\\n"
        continue
    m = re.match("key\\s+", line)
    if m:
        lines[i] = "<key>\\ncat(pki/private/{{ item }}.key)\\n</key>\\n"
        continue
    m = re.match("tls-auth\\s+.*\\s+(0|1)", line)
    if m:
        lines[i] = "<tls-auth>\\ncat(pki/ta.key)\\n</tls-auth>\\nkey-direction {}".format(m.group(1))
        continue
    m = re.match("cert.*", line)
    if m:
        lines[i] = "<cert>\\ncat(pki/issued/{{ item }}.crt)\\n</cert>\\n"
        continue


text = "\\n".join(lines).replace("\n","\\n")

res = []

while True:
    m = re.search("cat\\(([^)]+)\\)", text)
    if m:
        s = m.span(0)
        e = text[:s[0]]
        res.append('echo "{}"'.format(e))
        s = m.span(1)
        c = text[s[0]:s[1]]
        res.append("cat " + c)
        s = m.span(0)
        text = text[s[1]:]
        #print(res)
        #print(text)
    else:
        e = text
        res.append('echo "{}"'.format(e))
        break

lines = res
for i, line in enumerate(lines):
    if i == 0:
        lines[i] = lines[i] + " > {{ item }}.ovpn"
    else:
        lines[i] = lines[i] + " >> {{ item }}.ovpn"

dst = os.path.join(base, "exp.tmp")
with open(dst, "w") as f:
    f.write("\n".join(lines))

#print(res)

#text = text.replace("\n","\\n")
