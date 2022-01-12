# Python program to test internet speed
import speedtest
st = speedtest.Speedtest()
option = int(input('''What speed do you want to test:
1) Download Speed
2) Upload Speed
3) Ping
Your Choice: '''))
