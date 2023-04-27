# date_time.py
from datetime import datetime

date_string = "26 Apr 2023 05:23 PM UTC"
input_format = "%d %b %Y %I:%M %p %Z"
output_format = "%Y-%m-%dT%H:%M:%S"

date_obj = datetime.strptime(date_string, input_format)
formatted_date = date_obj.strftime(output_format)

print(formatted_date)
