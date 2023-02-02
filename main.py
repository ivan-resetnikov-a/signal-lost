import pygame as pg

import core



class Game :
	def __init__ (self) :
		# config
		self.size, self.rez = (1000, 800), (250, 200)
		self.title = 'Signal Lost'
		
		self.timeMult = 1
		self.fps = 60

		# window
		self.window = pg.display.set_mode(self.size)
		self.frame  = pg.Surface(self.rez)
		self.clock  = pg.time.Clock()
		pg.display.set_caption(self.title)


	def update (self) :
		self.player.update(self.timeMult)

		[enermy.update(self.timeMult) for enermy in self.enermies]


	def render (self) :
		self.frame.fill((0, 0, 0))
		################
		[enermy.render(self.frame, self.player) for enermy in self.enermies]

		self.player.render(self.frame)
		################
		self.window.blit(pg.transform.scale(self.frame, self.size), (0, 0))
		self.clock.tick(self.fps)
		pg.display.flip()


	def run (self) :
		self.onStart()

		self.running = 1
		while self.running :
			for event in pg.event.get() :
				if event.type == pg.QUIT :
					self.running = 0

			self.update()
			self.render()


	def onStart (self) :
		self.player = core.Player()

		self.enermies = [core.Enermy()]



Game().run()