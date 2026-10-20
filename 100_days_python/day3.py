"""
1. Module imports
2. built-in-functions
3. DateTime
4. Control & looping statements
5. conditional operators
"""
import day2 as d2
import math as m
from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo


def min_max_numbers(*numbers: int) -> tuple[int,int]:
    print("Length=",len(numbers))
    return min(numbers),max(numbers)


def sum_(*numbers:int) -> int:
    return sum(numbers)

def _convert_str_to_int(*numbers: str) -> tuple[int,...]:
    return tuple(int(float(number)) for number in numbers)


def datetime_operations(date_: str) -> str:
    print("Current Date=",datetime.now())
    print("Current Date=",date.today())
    print("formatting=",datetime.now().strftime("%d-%m-%Y"))
    print("converting str to datetime=",datetime.strptime(date_,"%Y-%m-%d"))
    print("ISO Date format=",datetime.now().isoformat())
    ist_time = datetime.now(ZoneInfo("Asia/Kolkata"))
    est_time = ist_time.astimezone(ZoneInfo("America/New_York"))
    print("converting Timezone",est_time.isoformat())
    return 'success'

def conditional_ops(num: int) -> None:
    val = "number is not zero" if num !=0 else "number is zero"
    print("result=",val)



if __name__ == "__main__":
    numbers = _convert_str_to_int(*input("Enter the numbers ").split())
    print("min-max=",min_max_numbers(*numbers))
    print("sum=",sum_(*numbers))
    print("sorted=",sorted(numbers))
    print("sorted reverse=",sorted(numbers,reverse=True))
    print(m.sqrt(numbers[0]))
    datetime_operations("2026-10-19")
    conditional_ops(0)
    conditional_ops(1)





