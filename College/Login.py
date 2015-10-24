username = str(input("Enter your username: "))
while username == "":
	username = str(input("Re-enter your username: "))

password = str(input("Enter your password: "))
while password == "":
	password = str(input("Re-enter you password: "))

users = {
	"M.Dawson": "secret",
	"S.Meier": "civilization",
	"S.Miyamoto": "mariobros",
	"W.Wright": "thesims",
	"guest": "guest"
}

security = {
	"M.Dawson": 5,
	"S.Meier": 3,
	"S.Miyamoto": 3,
	"W.Wright": 3,
	"guest": 1
}

if username in users and password == users[username]:
	print("Welcome {0}, you have been assigned level {1} security".format(username, security[username]))
else:
	print("Sorry, but you name is not on the list, so you can't come in!")