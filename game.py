#importing modules
import pygame
import sys
import random
import time
from pygame import mixer
from pygame.locals import *

#initializing pygame
pygame.init()

#cursor
pygame.mouse.set_cursor(*pygame.cursors.tri_left)

#resolution of the screen
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#caption and icon
pygame.display.set_caption("Stone Paper Scissor")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#user
stone_user=pygame.image.load("stone_user.png")
paper_user=pygame.image.load("paper_user.png")
scissor_user=pygame.image.load("scissor_user.png")
reset_user=pygame.image.load("reset_user.png")
user_pos=[172,344]
player_score=0
user_list=["Stone","Paper","Scissor"]

#comp
stone_comp=pygame.image.load("stone_comp.png")
paper_comp=pygame.image.load("paper_comp.png")
scissor_comp=pygame.image.load("scissor_comp.png")
reset_comp=pygame.image.load("reset_comp.png")
comp_pos=[172,0]
comp_score=0
comp_list=["Stone","Paper","Scissor"]

#buttons
stone_button=pygame.image.load("stone_button.jpg")
paper_button=pygame.image.load("paper_button.jpg")
scissor_button=pygame.image.load("scissor_button.jpg")

#background image
background = pygame.image.load("background.jpg")
screen.blit(background,(0,0))
screen.blit(reset_user,(user_pos[0],user_pos[1]))
screen.blit(reset_comp,(comp_pos[0],comp_pos[1]))

mixer.music.load("background.mp3")
mixer.music.play(-1)

font1=pygame.font.Font("font1.ttf",35, bold=False, italic=True)
font2=pygame.font.Font("font2.otf",23, bold=True, italic=False)
font3=pygame.font.Font("font3.ttf",25, bold=True, italic=True)

game_over=False
winner=0
clock=pygame.time.Clock()

while(1):
	if(game_over==False):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			if event.type==pygame.MOUSEBUTTONDOWN:
				comp_choice=random.choice(comp_list)
				click=pygame.mouse.get_pos()
				x=click[0]
				y=click[1]
				if (x>=443 and x<=525 and y>=417 and y<=457):
					screen.blit(background,(0,0))
					button_sound=mixer.Sound("button.wav")
					button_sound.play()
					user_choice=user_list[0]
					screen.blit(stone_user,(user_pos[0],user_pos[1]))
					label=font3.render("Computer chose", 1, (153, 204, 255))
					screen.blit(label,(410,46))
					label=font3.render(comp_choice, 1, (153, 204, 255))
					screen.blit(label,(453,70))
					if(comp_choice==user_choice):
						if(comp_choice==comp_list[0]):
							screen.blit(stone_comp,(comp_pos[0],comp_pos[1]))
						if(comp_choice==comp_list[1]):
							screen.blit(paper_comp,(comp_pos[0],comp_pos[1]))
						if(comp_choice==comp_list[2]):
							screen.blit(scissor_comp,(comp_pos[0],comp_pos[1]))
					elif(comp_choice==comp_list[1]):
						screen.blit(paper_comp,(comp_pos[0],comp_pos[1]))
						comp_score+=1
					elif(comp_choice==comp_list[2]):
						screen.blit(scissor_comp,(comp_pos[0],comp_pos[1]))
						player_score+=1
				elif (x>=443 and x<=525 and y>=467 and y<=507):
					screen.blit(background,(0,0))
					button_sound=mixer.Sound("button.wav")
					button_sound.play()
					user_choice=user_list[1]
					screen.blit(paper_user,(user_pos[0],user_pos[1]))
					label=font3.render("Computer chose", 1, (153, 204, 255))
					screen.blit(label,(410,46))
					label=font3.render(comp_choice, 1, (153, 204, 255))
					screen.blit(label,(453,70))
					if(comp_choice==user_choice):
						if(comp_choice==comp_list[0]):
							screen.blit(stone_comp,(comp_pos[0],comp_pos[1]))
						if(comp_choice==comp_list[1]):
							screen.blit(paper_comp,(comp_pos[0],comp_pos[1]))
						if(comp_choice==comp_list[2]):
							screen.blit(scissor_comp,(comp_pos[0],comp_pos[1]))
					elif(comp_choice==comp_list[0]):
						screen.blit(stone_comp,(comp_pos[0],comp_pos[1]))
						player_score+=1
					elif(comp_choice==comp_list[2]):
						screen.blit(scissor_comp,(comp_pos[0],comp_pos[1]))
						comp_score+=1
				elif (x>=443 and x<=525 and y>=517 and y<=557):
					screen.blit(background,(0,0))
					button_sound=mixer.Sound("button.wav")
					button_sound.play()
					user_choice=user_list[2]
					screen.blit(scissor_user,(user_pos[0],user_pos[1]))
					label=font3.render("Computer chose", 1, (153, 204, 255))
					screen.blit(label,(410,46))
					label=font3.render(comp_choice, 1, (153, 204, 255))
					screen.blit(label,(453,70))
					if(comp_choice==user_choice):
						if(comp_choice==comp_list[0]):
							screen.blit(stone_comp,(comp_pos[0],comp_pos[1]))
						if(comp_choice==comp_list[1]):
							screen.blit(paper_comp,(comp_pos[0],comp_pos[1]))
						if(comp_choice==comp_list[2]):
							screen.blit(scissor_comp,(comp_pos[0],comp_pos[1]))
					elif(comp_choice==comp_list[0]):
						screen.blit(stone_comp,(comp_pos[0],comp_pos[1]))
						comp_score+=1
					elif(comp_choice==comp_list[1]):
						screen.blit(paper_comp,(comp_pos[0],comp_pos[1]))
						player_score+=1
			screen.blit(stone_button,(443,417))
			label=font3.render("Stone", 1, (255, 204, 0))
			screen.blit(label,(454,425))
			screen.blit(paper_button,(443,467))
			label=font3.render("Paper", 1, (255, 102, 102))
			screen.blit(label,(454,475))
			screen.blit(scissor_button,(443,517))
			label=font3.render("Scissor", 1, (153, 153, 255))
			screen.blit(label,(448,525))
			text="Your Score: "+str(player_score)
			label=font2.render(text, 1, (255, 204, 0))
			screen.blit(label,(10,550))
			text="Computer Score: "+str(comp_score)
			label=font2.render(text, 1, (255, 204, 0))
			screen.blit(label,(10,10))
			clock.tick(60)
			pygame.display.update()
		if(player_score==5):
			explosion=mixer.Sound("gameover.wav")
			mixer.music.stop()
			explosion.play()
			winner="user"
			game_over=True
		if(comp_score==5):
			explosion=mixer.Sound("gameover.wav")
			mixer.music.stop()
			explosion.play()
			winner="computer"
			game_over=True
		pygame.display.update()
	elif (game_over==True):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		if(winner=="user"):
			label=font1.render("Congratulations! You Won!", 1, (204, 255, 51))
			screen.blit(label,(130,280))
		elif(winner=="computer"):
			label=font1.render("Computer Won! Better Luck Next Time!", 1, (204, 255, 51))
			screen.blit(label,(20,280))
		pygame.display.update()
pygame.quit()