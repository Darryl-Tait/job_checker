from datetime import timedelta
from art import logo
from replit import clear
# t1 = timedelta(hours=4, minutes=53)
# t2 = timedelta(hours=12, minutes=41)
# t3 = timedelta(hours=13, minutes=7)
# t4 = timedelta(hours=21, minutes=0)

# arrival = t2 - t1
# lunch = (t3 - t2 - timedelta(hours=1))
# departure = t4 - t3

# print(arrival, lunch, departure)


def job_length():
    """Determines the job length"""
    return finish_time - start_time


def check_pnb(start_time, finish_time):
    """Checks the start and finish times and checks when you should be getting a break"""
    if job_length() >= timedelta(hours=6, minutes=1) and job_length() <= timedelta(hours=9):
        pnb_1 = start_time + timedelta(hours=3)
        pnb_2 = start_time + timedelta(hours=5)
        pnb_3 = start_time + timedelta(hours=2)
        pnb_4 = start_time + timedelta(hours=7)
        print(f"Job length {job_length()} - 30min PNB between {pnb_1} and {pnb_2}\nOr 2 * 30min between {pnb_3} and {pnb_4}.")
    elif job_length() >= timedelta(hours=9, minutes=1):
        pnb_1 = start_time + timedelta(hours=3)
        pnb_2 = start_time + timedelta(hours=5)
        pnb_3 = start_time + timedelta(hours=3)
        pnb_4 = start_time + timedelta(hours=7)
        print(f"Job length {job_length()} - 40mins PNB between {pnb_1} and {pnb_2}\nOr 2 * 40min between {pnb_3} and {pnb_4}.")
    elif job_length() < timedelta(hours=6, minutes=1):
        print(f"Job length {job_length()} - PNB 20min break")


print(logo)

start_time = timedelta(hours=int(input("Please input the start hour: ")), minutes=int(input("please input the start minutes: ")))
clear()
print(logo)
finish_time = timedelta(hours=int(input("Please input the finish hour: ")), minutes=int(input("please input the finish minutes: ")))
clear()
print(logo)
check_pnb(start_time, finish_time)

