##################### Extra Hard Starting Project ######################
import smtplib
import random
import pandas
import datetime as dt


def birthday_wish():
    MY_GMAIL = "kondalwadesanjana@gmail.com"
    PASSWORD = "755S@njana"
    # 1. Update the birthdays.csv
    # done

    # 2. Check if today matches a birthday in the birthdays.csv
    today = (dt.datetime.now().month, dt.datetime.now().day)
    # print(today)
    birthday_data = pandas.read_csv("birthdays.csv")
    bday_dict = {
        (birthday_data["month"], birthday_data["day"]): birthday_data
                 for (index, birthday_data) in birthday_data.iterrows()
                 }

    # 3. If step 2 is true, pick a random letter from letter templates and replace
    # the [NAME] with the person's actual name from birthdays.csv
    number = random.randint(1, 3)
    if today in bday_dict:
        birthday_person = bday_dict[today]
        letter = f"letter_templates/letter_{number}.txt"
        with open(letter) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])


    # 4. Sending the letter generated to that person's email address.

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_GMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_GMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject: HAPPY BIRTHDAY\n\n{contents}"
            )

birthday_wish()

