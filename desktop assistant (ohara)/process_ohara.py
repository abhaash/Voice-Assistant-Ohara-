from output_ohara import output
from time_ohara import get_time

def process(query):
    if "what is the time" in query:
        return ("Time is "+ get_time())
    else:
        return "Nothing to return"