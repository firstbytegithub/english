#!/usr/bin/python

import os
import sys
import commands

simple_question=["Am ", "Is ", "Are ", "Was ", "Were ", "Do ", "Does ", "Did ", "Can ", "Could", "May ", "Might ", "Will ", "Would ", "Shall ", "Should ", "Has ", "Have ", "Had "]

special_question=["what ", "which ", "who ", "whose ", "whom ", "when ", "where ", "why ", "how "]

others=["as well as", "as long as"]

f_input=sys.argv[1]

print f_input

for key in simple_question:
    f_out = key.strip() + "_" + f_input
    cmd = "cat " + f_input + " | grep \'" + key + "\' > " + f_out
    print cmd
    (status, output)  = commands.getstatusoutput(cmd)

for key in special_question:
    f_out = key.strip() + "_" + f_input
    cmd = "cat " + f_input + " | grep -i \'" + key + "\' > " + f_out
    print cmd
    (status, output)  = commands.getstatusoutput(cmd)

for key in others:
    f_out = key.strip().replace(' ', '_') + "_" + f_input
    cmd = "cat " + f_input + " | grep -i \'" + key + "\' > " + f_out
    print cmd
    (status, output)  = commands.getstatusoutput(cmd)

