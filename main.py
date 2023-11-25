##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas

email = "oskar.lab16@gmail.com"
password = "zfdfqxxfjfcdvtta"

data = pandas.read_csv('birthdays.csv')
new_data = data.to_dict(orient="records")

current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day

for item in new_data:
    if item["month"] == current_month and item["day"] == current_day:
        absolute_name = item["name"]
        absolute_email = item["email"]

        file_number = random.randint(1, 3)
        file_path = f"letter_templates/letter_{file_number}.txt"
        with open(file_path) as file:
            contents = file.read()
            named_letter = contents.replace("[NAME]", absolute_name, 1)
            print(named_letter)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=absolute_email, msg=f"Subject: Happy Birthday!\n\n{named_letter}")