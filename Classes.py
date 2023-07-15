def get_font(a):
	pass

class Button():
	def __init__(self, image, pos, font,text_input = "", base_color = "#FFFFFF", hovering_color = "Black"):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

class Var():
	def __init__(self):
		self.displaylist = [] 			# List of the answers that the user has entered into the screen
		self.lastscreen = 0 			# Index of the lastscreen before the view screen to go back properly
		self.score = 0 					# Keeping track of the score of the user
		self.current = 1				# Current number in the quiz
		self.i = 0 						# Index for displaying premises
		self.j = 1 						# Number of lines in the screen (to be compared to ansnum to know when to go to the next quiz number)
		self.answernumlist = []			# Amount of answers in the current quiz item
		self.premisenumlist = []		# Amount of premises in the current quiz item
		self.anscheck = 1				# Index of the final answer of the current quiz item
		self.anum = 0					# Number to be displayed before the answer