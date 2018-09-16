import sys
import textfsm
from tabulate import tabulate

template_file = sys.argv[1]
output_file = sys.argv[2]

with open(template_file) as template, open(output_file) as output:
    re_table = textfsm.TextFSM(template)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(result)
    print(tabulate(result, headers=header))
