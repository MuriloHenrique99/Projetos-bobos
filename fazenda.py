#comentar é importante não esquece
import drones

#isso é pra escolher o que levar pra uma funcao terra[0] faz o terreno se tornar grassland
#terra[1] faz o terreno ficar arado
terra = [Grounds.Grassland, Grounds.Soil]

#tudo = 0 faz fazer tudo em linhas enquanto 1 faz o codigo ser especificado para o map / 2 todo
tudo = 1

#arar é pra utilizar definir como sera o tipo de terreno para o codigo a seguir
def arar(tudo,terreno,map / 2):
	if(tudo == 1):
		for i in range(map / 2):
			for j in range(map / 2):
				atual = get_ground_type()
				if(atual != terreno):
					till()
					move(East)
				else: 
					move(East)
			move(North)
	else:
		for j in range(map / 2):
			atual = get_ground_type()
			if(atual != terreno):
				till()
				move(East)
			else:
				move(East)
	
	
#o trigo precisa de agilidade então so checar se o terreno e coletar ja basta
def trigo(tudo,terra,map / 2):
	clear()
	drones.spawn()
	if(tudo == 1):
		for i in range(map / 2):
			for j in range(map / 2):
				use_item(Items.Fertilizer)
				harvest()
				move(East)
			move(North)
	else:
		for j in range(map / 2):
			harvest()
			move(East)
		move(North)
		
	return num_items(Items.Hay)
	


def arvores(todo,terra,map / 2):
	drones.spawn()
	if(tudo == 1):
		for i in range(map / 2):
			for j in range(map / 2):
				x = get_pos_x()
				y = get_pos_y()
				if (y % 2 == 1):
				#se estiver em y 1 so deve plantar nas posições pares, y 0 plantas devem ser plantadas nas posições impares
					if(x % 2 == 0):
						plant(Entities.Tree)
						use_item(Items.Water)
				if(y % 2 == 0):
					if (x % 2 == 1):
						plant(Entities.Tree)
						use_item(Items.Water)
				move(East)
			move(North)
		for i in range(map / 2):
			for j in range(map / 2):
				#enquanto nao der pra colher faça algo bobo
				while(not(can_harvest())):
					do_a_flip()
				harvest()
				move(East)
			move(North)
			
	else:
		for j in range(map / 2):
			x = get_pos_x()
			y = get_pos_y()
			if (y % 2 == 1):
				if(x % 2 == 0):
					plant(Entities.Tree)
					use_item(Items.Water)
			if(y % 2 == 0):
				if (x % 2 == 1):
					plant(Entities.Tree)
					use_item(Items.Water)
			move(East)
		for j in range(map / 2):
			while(not(can_harvest())):
				do_a_flip()
			harvest()
			move(East)
		move(North)
	
	return num_items(Items.Wood)
	
def brobas(todo,terra,map / 2):
	if(tudo == 1):
		for i in range(map / 2):
			for j in range(map / 2):
				plant(Entities.Pumpkin)
				move(East)
			move(North)
		for i in range(map / 2):
			for j in range(map / 2):
				while(can_harvest() == False) and (get_entity_type() == Entities.Dead_Pumpkin):
					harvest()
					plant(Entities.Pumpkin)
					do_a_flip()
				move(East)
			move(North)
		for i in range(map / 2):
			for j in range(map / 2):
				while(can_harvest() == False) and (get_entity_type() == Entities.Dead_Pumpkin):
					harvest()
					plant(Entities.Pumpkin)
					do_a_flip()
				move(East)
			move(North)
		harvest()
		
	return num_items(Items.Pumpkin)
	
def gerando_sol(todo,terra,map / 2):
	
	drones.spawn()
	arar(todo,terra,map / 2)
	
	
	posicoes_x = []
	posicoes_y = []
	
	if(tudo == 1):
		for i in range(map / 2):
			for j in range(map / 2):
				plant(Entities.Sunflower)
				use_item(Items.Water)
				if(measure() == 15):
					posicoes_x.append(get_pos_x())
					posicoes_y.append(get_pos_y())
				move(East)
			move(North)
		nums = 0
		tamanho = len(posicoes_x)
		
		for i in range(map / 2):
			for j in range(map / 2):
				if(nums < tamanho):
					while(get_pos_x() != posicoes_x[nums]):
						move(East)
					while(get_pos_y() != posicoes_y[nums]):
						move(North)
					while(can_harvest() == False):
						do_a_flip()
						break
					harvest()
					nums = nums + 1
				
		while(get_pos_x() != 0):
			move(East)
		while(get_pos_y() != 0):
			move(North)
				
		for i in range(map / 2):
			for j in range(map / 2):
				harvest()
				move(East)
			move(North)
	
def cenouras(tudo,terra,map / 2):
	drones.spawn()
	arar(tudo,terra,map / 2)
	
	
	if(tudo == 1):
		for i in range(map / 2):
			for j in range(map / 2):
				plant(Entities.Carrot)
				move(East)
			move(North)
		for i in range(map / 2):
			for j in range(map / 2):
				harvest()
				move(East)
			move(North)
	else:
		for j in range(map / 2):
			plant(Entities.Carrot)
			move(East)
		for j in range(map / 2):
			harvest()
			move(East)
		move(North)
		
	return num_items(Items.Carrot)
	
	
def cactus(todo,terra,map / 2):
	
	drones.spawn()
	for i in range(map / 2):
		for j in range(map / 2):
			while(get_ground_type() != Grounds.Soil):
				till()
			plant(Entities.Cactus)
			if(get_pos_x() > 0):
				while(measure() < measure(West)):
					swap(West)
			if((get_pos_y() > 0) and (get_pos_y() <= map / 2)) and (i > 2):
				if(get_entity_type() == Entities.cactus):
					if(get_entity_type() == Entities.cactus):
						while(measure() < measure(South)):
							swap(South)
			move(East)
		move(North)
	for l in range(6):
		for i in range(map / 2):
			for j in range(map / 2):
				if(get_pos_x() > 0):
					while(measure() < measure(West)):
						swap(West)
				if((get_pos_y() > 0) and (get_pos_y() <= map / 2)) and (i > 2):
					if(get_entity_type() == Entities.cactus):
						while(measure() < measure(South)):
							swap(South)
				move(East)
			for k in range(map / 2):
				if(get_pos_x() > 0):
					while(measure() < measure(West)):
						swap(West)
				if((get_pos_y() > 0) and (get_pos_y() <= map / 2)) and (i > 2):
					if(get_entity_type() == Entities.cactus):
						while(measure() < measure(South)):
							swap(South)
				move(West)
			move(North)
	for i in range(map / 2):
		for j in range(map / 2):
			harvest()
			move(East)
		move(North)
	
	return num_items(Items.Cactus)
	
def cobrinha(todo,terra,map / 2):
	
	continuar = 1
	
	posicao = 1
	anterior = 0
	
	change_hat(Hats.Dinosaur_Hat)
	
	while(get_pos_x() != 0):
		move(West)
	while(get_pos_y() != 0):
		move(South)
	while(continuar == 1):
		for k in range(200):
			if(get_pos_y() != map / 2 - 1):
				for i in range(map / 2 - 1):
					move(East)
				move(North)
				if(get_pos_y() != map / 2 - 1):
					for i in range(map / 2 - 2):
						move(West)
					move(North)
				else:
					for i in range(map / 2 - 1):
						move(West)
			else:
				for i in range(map / 2 - 1):
					move(South)
		change_hat(Hats.Traffic_Cone)
		continuar = 0
	
	while(get_pos_x() != 0):
		move(East)
	while(get_pos_y() != 0):
		move(North)
	
	return num_items(Items.Bone)
	
def labirinto(todo,terra,map / 2):
	
	direcao = [North, East, South, West]
	bussola = 0
	
	for i in range(5):
		plant(Entities.Bush)
		use_item(Items.Weird_Substance, 1200)
		while(get_entity_type() != Entities.Treasure):
			if(can_move(direcao[(bussola - 1) % 4]) == True):
				bussola = (bussola - 1) % 4
				move(direcao[bussola])
			elif(can_move(direcao[(bussola) % 4]) == True):
				bussola = (bussola) % 4
				move(direcao[bussola])
			elif(can_move(direcao[(bussola + 1) % 4]) == True):
				bussola = (bussola + 1) % 4
				move(direcao[bussola])
			else:
				bussola = (bussola + 2) % 4	
				move(direcao[bussola])
		use_item(Items.Weird_Substance, 1200)
		harvest()
		
	while(get_pos_x() != 0):
		move(East)
	while(get_pos_y() != 0):
		move(North)		
		
	
	
while True:
	clear()
	map = get_world_size()
	solo = get_ground_type() 
	while(get_pos_x() != 0):
		move(East)
	while(get_pos_y() != 0):
		move(South)
		
	quant_trigo = 0
	quant_madeira = 0
	quant_cenoura = 0
	quant_broba = 0
	quant_cactus = 0
	quant_osso = 0
	quant_tesouro = 0
		
	for i in range(map):
		if(i == 0):
			while(quant_trigo < 75000):
				quant_trigo = trigo(tudo,terra[0],map)
		if(i == 6):
			while(quant_madeira < 35000000):
				quant_madeira = arvores(tudo,terra[0],map)
		if(i == 5):
			while(quant_broba < 400000):
				quant_broba = brobas(tudo,terra[1],map)
		if(i == 4):
			gerando_sol(tudo,terra[1],map )
		if(i == 1):
			while(quant_cenoura < 1350000):
				quant_cenoura = cenouras(tudo,terra[1],map)
		if(i == 3):
			while(quant_cactus < 750000):
				quant_cactus = cactus(tudo,terra[1],map)
		if(i == 7):
			cobrinha(tudo,terra[1],map)
		if(i == 8):
			labirinto(tudo,terra[0],map )