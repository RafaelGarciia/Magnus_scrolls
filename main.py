import Lib.token_lib as tok


while True:
	comand_line = input("> ").lower()
	
	if " " in comand_line:
		comand_line = comand_line.split(" ")
		comand = comand_line.pop(0)
		argument = comand_line
	else:
		comand = [comand_line]
		argument = []

	match comand:
		case "roll":	print(tok.dice_roll(argument))