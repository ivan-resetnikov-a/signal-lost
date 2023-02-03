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
		self.player.update(self.timeMult, self.colliders)

		[enermy.update(self.timeMult) for enermy in self.enermies]


	def render (self) :
		self.frame.fill((0, 0, 0))
		################
		[enermy.render(self.frame, self.player, self.colliders) for enermy in self.enermies]

		[obj.render(self.frame) for obj in self.objects]

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


	def loadLevel (self) :
		print(f'=== LOADING LEVEL "{self.player.level}" ===')
		content = core.loadFromJSON(f'data/signal_lost/world/{self.player.level}.json')
		print('[Y] Reading from file')

		self.colliders, self.objects = [], []

		try : rot = obj['rot']
		except : rot = 0
		[self.objects.append(core.Object(obj['name'], obj['pos'], rot)) for obj in content['objects']]
		print('[Y] Loading objects')

		# load colliders
		[self.colliders.append(tuple(collider)) for collider in content['colliders']]


	def onStart (self) :
		self.player = core.Player()

		self.enermies = [core.Enermy()]

		self.loadLevel()



Game().run()