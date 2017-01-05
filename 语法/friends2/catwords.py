#!/usr/bin/python

import os
import sys
import commands

simple_question=["Am ", "Is ", "Are ", "Was ", "Were ", "Do ", "Does ", "Did ", "Can ", "Could", "May ", "Might ", "Will ", "Would ", "Shall ", "Should ", "Has ", "Have ", "Had "]

special_question=["What ", "Which ", "Who ", "Whose ", "Whom ", "When ", "Where ", "Why ", "How "]

others=["as well as", "as long as"]

daici1=["I ", "You ", "He ", "She ", "It ", "We ", "They "]

daici2=["I'm ", "You're ", "It's ", "He's ", "She's ", "We're ", "They're "]

daici3=["My ", "Your ", "His ", "Her ", "Its ", "Their ", "Our "]

daici4=["This ", "That ", "These ", "Those "]

daici5=["This's ", "That's "]

daici6=["Some ", "Any ", "No ", "Every ", "All ", "Each ", "Few ", "A few ", "Little ", "A little ", "Many ", "Much ", "Both ", "Neither ", "None ", "Either ", "Other ", "Others ", "Another ", "One ", "The "]

daici7=["Something ", "Somebody ", "Someone ", "Anything ", "Anybody ", "Anyone ", "Nothing ", "Nobody ", "Everything ", "Everybody ", "Everyone "]

mix=["Let ", "Let's ", "To "]

f_input=sys.argv[1]

print f_input

for key in simple_question:
    f_out = key.strip() + "_" + f_input
    cmd = "cat " + f_input + " | grep \'^" + key + "\' > " + f_out
    print cmd
    (status, output)  = commands.getstatusoutput(cmd)

for key in special_question:
    f_out = key.strip() + "_" + f_input
    cmd = "cat " + f_input + " | grep \'^" + key + "\' > " + f_out
    print cmd
    (status, output)  = commands.getstatusoutput(cmd)

for key in others:
    f_out = key.strip().replace(' ', '_') + "_" + f_input
    cmd = "cat " + f_input + " | grep -i \'" + key + "\' > " + f_out
    print cmd
    (status, output)  = commands.getstatusoutput(cmd)

for key in daici1:
    f_out = key.strip().replace(' ', '_').replace('\'', "_") + "_" + f_input
    cmd = "cat " + f_input + " | grep \'^" + key + "\' | sort > " + f_out
    print cmd
    (status, output)  = commands.getstatusoutput(cmd)
    
for key in daici2:
    f_out = key.strip().replace(' ', '_').replace('\'', "_") + "_" + f_input
    cmd = "cat " + f_input + " | grep \"^" + key + "\" | sort > " + f_out
    print cmd
    (status, output)  = commands.getstatusoutput(cmd)
    
for key in daici3:
    f_out = key.strip().replace(' ', '_').replace('\'', "_") + "_" + f_input
    cmd = "cat " + f_input + " | grep \'^" + key + "\' | sort > " + f_out
    print cmd
    (status, output)  = commands.getstatusoutput(cmd)
    
for key in daici4:
    f_out = key.strip().replace(' ', '_').replace('\'', "_") + "_" + f_input
    cmd = "cat " + f_input + " | grep \'^" + key + "\' | sort > " + f_out
    print cmd
    (status, output)  = commands.getstatusoutput(cmd)
    
for key in daici5:
    f_out = key.strip().replace(' ', '_').replace('\'', "_") + "_" + f_input
    cmd = "cat " + f_input + " | grep \"^" + key + "\" | sort > " + f_out
    print cmd
    (status, output)  = commands.getstatusoutput(cmd)
    
for key in daici6:
    f_out = key.strip().replace(' ', '_').replace('\'', "_") + "_" + f_input
    cmd = "cat " + f_input + " | grep \'^" + key + "\' | sort > " + f_out
    print cmd
    (status, output)  = commands.getstatusoutput(cmd)
    
for key in daici7:
    f_out = key.strip().replace(' ', '_').replace('\'', "_") + "_" + f_input
    cmd = "cat " + f_input + " | grep \'^" + key + "\' | sort > " + f_out
    print cmd
    (status, output)  = commands.getstatusoutput(cmd)

for key in mix:
    f_out = key.strip().replace(' ', '_').replace('\'', "_") + "_" + f_input
    cmd = "cat " + f_input + " | grep \"^" + key + "\" | sort > " + f_out
    print cmd
    (status, output)  = commands.getstatusoutput(cmd)
    
