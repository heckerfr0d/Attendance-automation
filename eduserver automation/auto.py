#!/usr/bin/python3
###### this code is written by Abhinav -p (@_ai_factory) and ported to mechanize by Hadif Hameed ######
### abhinavhariharan2001@gmail.com ###

import http.cookiejar as cookielib
import mechanize
import os
import timetable as tb
import datetime
import time

# timetable information to be supplied in timetable.py file

# personal information to be filled-----------!!

class_login = [("username1", "password1"), ("username2", "password2")]

# --------------------------------------------!!

# main timetable data
arr = tb.timetable

# globals
curr_time = 0   		# variable for accessing the current time
day_indx = 0			# index of the day monday has index 0
length_of_day = 0		# the total sessions on the day
non_working_day = False
prev_slot = "none"

# the code tries to put the attendance for some attempts if it fails at its first attempt
# this can happen if the link is unavailable or the slot is changed.
# each attempt is done after a 10second delay inorder to wait for the link

max_attempts = 10  # maximum number of attempts till completion

rotate_animation = 0
rot_anim = '|'


def put_attendance(sub_id, sub_code):
    global max_attempts, class_login
    attendance_marked = False
    attempts = 0
    for username, password in class_login:
        while(attendance_marked == False and attempts < max_attempts):
            browser = mechanize.Browser()
            cookiejar = cookielib.LWPCookieJar()
            browser.set_cookiejar(cookiejar)
            browser.set_handle_equiv(True)
            browser.set_handle_gzip(True)
            browser.set_handle_redirect(True)
            browser.set_handle_referer(True)
            browser.set_handle_robots(False)
            browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
            browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

            try:
                browser.open("https://eduserver.nitc.ac.in/login/index.php")
                browser.select_form(action="https://eduserver.nitc.ac.in/login/index.php")
                browser.form.set_all_readonly(False)
                browser.form['username'] = username
                browser.form['password'] = password
                browser.submit()

                browser.open(sub_code)
                browser.follow_link(text="Submit attendance")

                time.sleep(2)

                browser.select_form(action="https://eduserver.nitc.ac.in/mod/attendance/attendance.php")
                browser.form.set_all_readonly(False)
                browser.form.find_control(name="status").get(nr=0).selected = True

                time.sleep(1)
                browser.submit(id="id_submitbutton")
                time.sleep(1)
                attendance_marked = True
            except:
                print("trying again..")
                time.sleep(10)
                attempts += 1
                print(f"---> attempt : {attempts} <---")

            browser.close()
        if(attempts >= max_attempts):
            print(f"link unavailable after {max_attempts} attempts.. skipping")
            attendance_marked = True


def rotate_animation_init():

    global rotate_animation, rot_anim

    rot_anim = '|'
    if(rotate_animation > 50):
        rot_anim = '/'

    if(rotate_animation > 100):
        rot_anim = '-'
    if(rotate_animation > 150):
        rot_anim = "\\"
    if(rotate_animation > 200):
        rot_anim = '|'
        rotate_animation = 0
    rotate_animation += 3


def init_day():
    global curr_time, day_indx, length_of_day, non_working_day, rot_anim

    x = datetime.datetime.now()
    curr_time = [int(x.hour), int(x.minute)]

    day = x.strftime("%A").lower()
    os.system("cls")

    rotate_animation_init()

    print("________ automation status : running "+rot_anim+"  ________\n")
    print(f'current time | {curr_time[0]} : {curr_time[1]} : {x.second}')
    print("day          | "+day)

    if(day in tb.days):
        non_working_day = False
        day_indx = tb.days.index(day)
        length_of_day = len(arr[day_indx])
    else:
        non_working_day = True


def event_driver():
    global prev_slot
    while True:
        init_day()  # initialise the current day

        if(non_working_day):  # check if the day is a working day or not
            continue

        for i in range(1, length_of_day):

            block = arr[day_indx][i]

            hours_curr = curr_time[0]
            min_curr = curr_time[1]

            if(block[0][0] == hours_curr and block[0][1] == min_curr):
                attendance_to = block[1]
                print("\ntimetable slot found ...")
                print(f'current active slot  | {attendance_to}\n')
                print("=========================================")
                curr_slot = attendance_to
                if(curr_slot == prev_slot):
                    continue

                if(attendance_to not in tb.active_classes):
                    continue

                id_path = tb.course_web_url[attendance_to]

                put_attendance(attendance_to, id_path)

                prev_slot = curr_slot


# // main

event_driver()


# sleep peacefully
# :) :) :) *-* :( :( :(
