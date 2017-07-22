def main():
	daily_growth = float(input("Daily percent gain"))*.01 +1
	time = int(input("number of days"))
	x = 1
	for i in range(time):
		x *= daily_growth
		if i % 10 == 0:
			print(x)
	print("Final return after"+str(time)+" days is",x)

main()
