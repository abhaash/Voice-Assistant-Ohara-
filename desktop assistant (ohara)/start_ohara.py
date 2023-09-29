from input_ohara import take_input
from process_ohara import process
from output_ohara import output

while(True):
    i=take_input()
    o=process(i)
    output(o)