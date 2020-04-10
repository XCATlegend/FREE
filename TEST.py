# -*- coding: utf-8 -*-
'''
©EDITOR XCAT PROJECT 2019 
'''
from important import *
print("💜💛💚💙")
print (""" 
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ ➣LOVE YOU
┃➣Siriyakorn Chopkankit
┃ ➣3 Month
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
import os
print("💜💛💚💙")
parser = argparse.ArgumentParser(description='© 2018SelfBot ProtectV2.2')
parser.add_argument('-t', '--token', type=str, metavar='', required=False, help='Token | Example : Exxxx')
parser.add_argument('-e', '--email', type=str, default='', metavar='', required=False, help='Email Address | Example : example@xxx.xx')
parser.add_argument('-p', '--passwd', type=str, default='', metavar='', required=False, help='Password | Example : xxxx')
parser.add_argument('-a', '--appName', type=str, default='', metavar='', required=False, choices=list(ApplicationType._NAMES_TO_VALUES), help='Application Type | Example : CHROMEOS')
parser.add_argument('-s', '--systemname', type=str, default='', metavar='', required=False, help='System Name | Example : Chrome_OS')
parser.add_argument('-c', '--channelid', type=str, default='', metavar='', required=False, help='Channel ID | Example : 1341209950')
parser.add_argument('-T', '--traceback', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Using Traceback | Use : True/False')
parser.add_argument('-S', '--showqr', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Show QR | Use : True/False')
args = parser.parse_args()
#LOVE ZONE#
start_runtime = datetime.now()
bas = LINE()
Mymid = basprofile.mid
creator = ["u9f701b2a76a5acfada5ebbcecdaef92b"]
owner = ["u9f701b2a76a5acfada5ebbcecdaef92b"]
admin = ["u9f701b2a76a5acfada5ebbcecdaef92b"]
staff = ["u9f701b2a76a5acfada5ebbcecdaef92b"]
GOD = [Mymid]
#$
Ariff = creator + admin + owner + staff + Bots
programStart = time.time()
oepoll = OEPoll(line)
#$#$#
    elif text.lower().startswith("/exec\n") or "exec" in msg.text:
                    try:
                        code = msg.text.replace("/exec\n", "")
                        exec(code)
                    except Exception as error:
                        line.sendMessage(to, "Error : {}".format(error))
    elif msg.text.lower().startswith('/exec '):
                    delcmd = msg.text.split(" ")
                    getx = msg.text.replace(delcmd[0] + " ","")
                    data = data="{}".format(getx)
                    sendTemplate(to, data)    