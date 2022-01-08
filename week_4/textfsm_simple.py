import textfsm

template_file = "show_ip_int_brief.template"
template = open(template_file)

with open("show_ip_int_brief.txt") as f:
    raw_text_data = f.read()

import ipdb
ipdb.set_trace()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)

template.close()
