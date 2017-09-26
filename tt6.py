#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2015 delcasso <delcasso@delcasso-ephys>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import time
from constants import Color, Event
import utils

# Variables Setup By User
arduino_port = '/dev/ttyACM9'
box = '6'
data_folder = "/home/snc-team/Dropbox (MIT)/SNc-Team/Behavior/Data/"

user = '@gmail.com'
pwd = ''
recipient = user
subject = "box" + box + " done"
body = subject

###################################################################

print "\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "\t\t~ Behavioral Data Acquisition Software v1.0 ~"
print "\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print ""

# ---------------------
#   Setup Experiment  |
# ---------------------

ser = utils.setup_serial(arduino_port)  # Creation of serial connection with Arduino
fo = utils.open_file(data_folder, box)  # Creation of the output filename and opening of the file
utils.establish_connection(ser)         # Establish connection with Arduino

time.sleep(0.2)


# ----------------------
#   Begin Experiment!  |
# ----------------------

nTrials = 0
nRewards = 0
nLights = 0
nLicks = 0
nInterrupts = 0

running = True
while running:
    if ser.inWaiting() > 0:
        # print "ser.inWaiting = " +str(ser.inWaiting())
        out = ser.readline()
        fo.write(out)
        out.replace('\n', '')
        c = out.split("\t")
        value = c[2]
        value = value[:-1]
        # print c[0] + "-" + c[1] + "-" + c[2]

        ms = int(c[0])

        h, ms = ms / 3600000, ms % 3600000
        m, ms = ms / 60000, ms % 60000
        s = ms / 1000
        ms = ms % 1000

        current_time_str = str(h) + ":" + str(m) + ":" + str(s) + ":" + str(ms)
        event = c[1]

        if event == Event.TONE1_ON:
            nTrials += 1
            print Color.WARNING + "\t" + current_time_str + "\tTONE_1 ON    trial #" + str(nTrials) + Color.END

        if event == Event.TONE2_ON:
            nTrials += 1
            print Color.WARNING + "\t" + current_time_str + "\tTONE_2 ON    trial #" + str(nTrials) + Color.END

        if event == Event.TONE3_ON:
            nTrials += 1
            print Color.WARNING + "\t" + current_time_str + "\tTONE_3 ON    trial #" + str(nTrials) + Color.END

        if event == Event.TONE1_OFF:
            print Color.WARNING + "\t" + current_time_str + "\tTONE_1 OFF    trial #" + str(nTrials) + Color.END

        if event == Event.TONE2_OFF:
            print Color.WARNING + "\t" + current_time_str + "\tTONE_2 OFF    trial #" + str(nTrials) + Color.END

        if event == Event.TONE3_OFF:
            print Color.WARNING + "\t" + current_time_str + "\tTONE_3 OFF    trial #" + str(nTrials) + Color.END

        if event == Event.LICK:
            nLicks += 1
            print Color.OK_GREEN + "\t" + current_time_str + "\tLICK #" + str(nLicks) + Color.END

        if event == Event.NLICK_DURING_DECISION:  # END OF DECISION
            nLicks += 1
            print Color.HEADER + "\t" + current_time_str + "\tDEC. val=" + value + Color.END

        if event == "103":  # INTERRUPT
            nInterrupts += 1
            print Color.HEADER + "\t" + current_time_str + "\tinterrupt #" + value + Color.END

        if event == Event.SOLENOID_ON:
            nRewards += 1
            print Color.OK_BLUE + "\t" + current_time_str + "\tREWARD #" + str(nRewards) + Color.END

        if event == Event.LED_PWM:
            nLights += 1
            print Color.FAIL + "\t" + current_time_str + "\tLIGHT #" + str(nLights) + " " + str(int(value)) + " PWM" + \
                Color.END

        if event == Event.EXPERIMENT_STOP:
            running = False
            print "Experiment Stopped By Arduino"

        time.sleep(0.01)

    else:
        time.sleep(0.1)


ser.close()
fo.close()
utils.send_email(user, pwd, recipient, subject, body)
