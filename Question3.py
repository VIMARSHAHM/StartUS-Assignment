# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 19:37:07 2020

@author: VIMARSHA H M
"""


#Question 3
#How do I use the standard console tools to find ten IP addresses 
#from which there were most requests?

#Run the following commmand-


#awk '{ print $1}' access.log.2016-05-08 | sort | uniq -c | sort -nr | head -n 10


# =============================================================================
# In the command above:
# 
# awk – prints the access.log.2016-05-08 file.
# sort – helps to sort lines in a access.log.2016-05-08 file, the -n option compares lines based on the numerical value of strings and -r option reverses the outcome of the comparisons.
# uniq – helps to report repeated lines and the -c option helps to prefix lines according to the number of occurrences.
# =============================================================================

#Top 10 tools are-
#Wireshark, Nmap, iPerf3, Cisco Packet Tracer, Putty, Netstat, Angry IP Scanner,
# PingPlotter, cURL, PRTG WiFi Monitor
