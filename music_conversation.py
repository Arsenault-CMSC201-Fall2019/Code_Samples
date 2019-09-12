def main():
	is_hot = input("Hi! Is it hot out?").lower()
	if is_hot.lower() == "yes":
		is_raining = input("Is it wet out there?")
		if is_raining == "yes":
			print("Better bring an umbrella")
		else:
			bearness = input("Is there a large bear at your door?")
			if bearness == "yes":
				print("play dead, because that totally always works")
		really = input ("like, is it super hot?")
		if really ==  "super":
			print ("play dead; you’ll be cooler")
		else:
			print("wear something that’s cool and comfortable")
	else: 
		music = input ("What is your favorite musical genre?")
		if music == "jazz" or music == "jazz funk" or music == "jazz fusion" or music == "swing":
			print("How about a fedora (but also wear a suit or you’ll make the wrong impression)")
		elif music == "polka metal fusion":
			print("Let’s get lunch together, and talk about your life decision")
		else:
			print ("Oh, tell me more about ”, music, “ and I will nod.")

main()
