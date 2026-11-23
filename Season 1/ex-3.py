from zmq.backend import second

second = int(input("Enter second:"))
minute = int(input("Enter minute:"))
hour = int(input("Enter hour:"))

minute += hour*60
second += minute*60
print(second)