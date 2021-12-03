# Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?
N = int(input("Enter minute: "))
hour = N//60
minute = N%60
print(f"The time is {hour} : {minute}")