
# Attendance-automation

A python script for nitc eduserver attendance automation.
This is a fork of the original repo by Abhinav -p (@_ai_factory) which I ported from Selenium to Mechanize for a headless script that can work on EC2 instances.

## External libraries used

1. Mechanize

## Mechanize installation

```pip3 install mechanize``` or
```pip install mechanize``` depending on your python setup.

## Running the script

```python3 auto.py``` or
```python auto.py``` or, on Linux,
```./auto.py```

## Script details

1. timetable.py

    Contains timetable data and links.

    Timetable format: [[hour, minute], "subject_name"]

    Order of slots doesn't matter.

    Give slot time as the time when the link for attendance becomes active in eduserver.

2. auto.py

    Main script file.

    Provide user details here.

    Modify the script here.

## Important parameters in auto.py

1. class_login : Eduserver login details of multiple users in the format [("username1", "password1"), ("username2", "password2")]

2. max_attempts : Max number of retries

## About this script

This code is written by Abhinav -p and forked by Hadif Hameed. It is still under development so proceed at your own risk.

licensed under [![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/AI-Factor-y/Attendance-automation/blob/main/LICENSE)

Any contribution to this code will be helpful so please feel free to commit
