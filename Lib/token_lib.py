from random import randint


def creat_spell(damage:int, type_damage:str):
	return {
		'damage'		: int(damage),
		'type_damage'	: str(type_damage)
	}

def creat_item(damage:int, type_damage:str):
	return {
		'damage'		: int(damage),
		'type_damage'	: str(type_damage)
	}

def dice_roll(roll:str | list[int, int]) -> list[int] | bool:
	if "d" in roll:
		roll = roll.split('d')
	if type(roll) != type(["list"]):
		print(f"argument is not a list\n{roll}")
		return False
	many_times = roll[0]
	dice_type  = roll[1]
	
	roll_list = []
	for time in range(many_times):
		num = randint(1, dice_type)
		roll_list.append(num)
	return roll_list

class sheet_token():
	def __init__(self) -> None:
		self.char_name	= ""
		self.char_class	= ""
		self.char_job	= ""

		self.attributes = {
			'strength'		: 0,
			'dexterity'		: 0,
			'constitution'	: 0,
			'intelligence'	: 0,
			'wisdom'		: 0,
			'charisma'		: 0,
		}
		self.modifiers = {
			'stre_mod'		: 0,
			'dext_mod'		: 0,
			'cons_mod'		: 0,
			'inte_mod'		: 0,
			'wisd_mod'		: 0,
			'char_mod'		: 0,
		}
		self.inventory	= []
		self.spells		= []
		self.skills		= []

	def set_class(self, arg_class):
		match arg_class:
			case "mage":
				self.char_class = "Mage"
				#self.spells.append(spell['star_rain'])
				#self.spells.append(spell['fire_ball'])
				#self.inventory.append(item['base_sword'])