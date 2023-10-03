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

	def dice_roll(self, type:int, quanty):
		
		roll_list = []
		sums = 0
		for time in range(quanty):
			num = randint(1, type)
			roll_list.append(num)
			sums += num
		return {"rolls": roll_list, "sum": sums}

	def set_class(self, arg_class):
		match arg_class:
			case "mage":
				self.char_class = "Mage"
				#self.spells.append(spell['star_rain'])
				#self.spells.append(spell['fire_ball'])
				#self.inventory.append(item['base_sword'])