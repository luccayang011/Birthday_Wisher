import pandas as pd
import datetime as dt
import random
import smtplib

my_email = 'myemail@gmail.com'
password = 'password'

birthdays = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
month = now.month
day = now.day
#today_tuple = (now.month, now.day)
#birthdays_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}

for index, row in birthdays.iterrows():
    if month == row.month and day == row.day:
        with open(f'letter_templates/letter_{random.randint(1, 3)}.txt', 'r') as letter_template:
            letter = letter_template.read()
            letter = letter.replace('[NAME]', row["name"])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=row["email"],
                                    msg=f"Subject: Happy Birthday! \n\n"
                                        f"{letter}")




