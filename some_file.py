from pydantic import field_validator, BaseModel
from datetime import date


my_date = date(year=2003, month=4, day=19)

today = date.today()

age = today.year - my_date.year - ((today.month, today.day) < (my_date.month, my_date.day))

print(age)


