import json

print("login with username : ")

user_name = input()

print("ready to chat!\n")
msg = input()

exit_sign = 0

while exit_sign == 0:

	msg_dict = {"message":msg, "user":user_name, "type":"text message"}
	print(msg_dict["user"] + " : " + msg_dict["message"])
	msg = input()
	if msg == "/exit":
		break
	print(json.dumps(msg_dict, indent=4))

