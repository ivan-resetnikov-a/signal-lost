import pygame as pg



class Player :
	def __init__ (self) :
		self.pos = [0, 0]
		self.vel = [0, 0]
		self.speed = 0.2

		self.level = 0


	def update (self, dt) :
		keys = pg.key.get_pressed()

		if keys[pg.K_w] : self.vel[1] -= self.speed * dt
		if keys[pg.K_s] : self.vel[1] += self.speed * dt
		if keys[pg.K_a] : self.vel[0] -= self.speed * dt
		if keys[pg.K_d] : self.vel[0] += self.speed * dt

		self.pos[0] += self.vel[0]
		self.pos[1] += self.vel[1]

		self.vel[0] *= 0.8
		self.vel[1] *= 0.8


	def render (self, frame) :
		pg.draw.circle(frame, (255, 255, 255), self.pos, 3)