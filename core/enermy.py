from math import atan2, sin, cos

import pygame as pg



class Enermy :
	def __init__ (self) :
		self.pos = [125, 100]


	def update (self, dt) :
		pass


	def render (self, frame, player) :
		pg.draw.circle(frame, (255, 0, 0), self.pos, 3)

		pg.draw.rect(frame, (0, 0, 255), (50, 90, 20, 20))

		deg = atan2(self.pos[1] - player.pos[1], self.pos[0] - player.pos[0])

		color = (255, 255, 255)
		distance = 0
		for i in range(round(100/6)) :
			distance += 6
			for collider in [(50, 90, 20, 20)] :
				if pg.Rect(((self.pos[0]-3)-(cos(deg) * distance), (self.pos[1]-3) - (sin(deg) * distance), 6, 6)).colliderect(collider) :
					color = (0, 255, 0)
					break

			if color == (0, 255, 0) : break

			if pg.Rect(((self.pos[0]-3)-(cos(deg) * distance), (self.pos[1]-3) - (sin(deg) * distance), 6, 6)).colliderect((player.pos[0]-3, player.pos[1]-3, 6, 6)) :
				color = (255, 0, 0)
				break
				

		pg.draw.line(frame, color, self.pos,
			[self.pos[0] - (cos(deg) * distance),
			 self.pos[1] - (sin(deg) * distance)], 1)
		