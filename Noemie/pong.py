import pygame
 
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
 
font20 = pygame.font.Font('freesansbold.ttf', 20)

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
FPS = 30

# Player class
class Striker:
	
	# Take the initial position,
	# dimensions, speed and color of the object
	def __init__(self, posx, posy, width, height, speed, color):
		self.posx = posx
		self.posy = posy
		self.width = width
		self.height = height
		self.speed = speed
		self.color = color
		# Rect that is used to control the
		# position and collision of the object
		self.geekRect = pygame.Rect(posx, posy, width, height)
		# Object that is blit on the screen
		self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

	# Used to display the object on the screen
	def display(self):
		self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

	# Used to update the state of the object
	# yFac represents the direction of the striker movement
	# if yFac == -1 ==> The object is moving upwards
	# if yFac == 1 ==> The object is moving downwards
	# if yFac == 0 ==> The object is not moving
	def update(self, yFac):
		self.posy = self.posy + self.speed*yFac

		# Restricting the striker to be below
		# the top surface of the screen
		if self.posy <= 0:
			self.posy = 0
		# Restricting the striker to be above
		# the bottom surface of the screen
		elif self.posy + self.height >= HEIGHT:
			self.posy = HEIGHT-self.height

		# Updating the rect with the new values
		self.geekRect = (self.posx, self.posy, self.width, self.height)

	# Used to render the score on to the screen
	# First, create a text object using the font.render() method
	# Then, get the rect of that text using the get_rect() method
	# Finally blit the text on to the screen
	def displayScore(self, text, score, x, y, color):
		text = font20.render(text+str(score), True, color)
		textRect = text.get_rect()
		textRect.center = (x, y)

		screen.blit(text, textRect)

	def getRect(self):
		return self.geekRect


# Player class
class StrikerCPU:
	
	# Take the initial position,
	# dimensions, speed and color of the object
	def __init__(self, posx, posy, width, height, speed, color):
		self.posx = posx
		self.posy = posy
		self.width = width
		self.height = height
		self.speed = speed
		self.color = color
		# Rect that is used to control the
		# position and collision of the object
		self.geekRect = pygame.Rect(posx, posy, width, height)
		# Object that is blit on the screen
		self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

	# Used to display the object on the screen
	def display(self):
		self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

	# Used to update the state of the object
	# yFac represents the direction of the striker movement
	# if yFac == -1 ==> The object is moving upwards
	# if yFac == 1 ==> The object is moving downwards
	# if yFac == 0 ==> The object is not moving
	def update(self, yFa,ball,tick):
		self.posy = self.posy + self.speed*yFa

		# Restricting the striker to be below
		# the top surface of the screen
		if self.posy <= 0:
			self.posy = 0
		# Restricting the striker to be above
		# the bottom surface of the screen
		elif self.posy + self.height >= HEIGHT:
			self.posy = HEIGHT-self.height

		# Updating the rect with the new values
		self.geekRect = (self.posx, ball.posy-(50*tick/10), self.width, self.height)

	# Used to render the score on to the screen
	# First, create a text object using the font.render() method
	# Then, get the rect of that text using the get_rect() method
	# Finally blit the text on to the screen
	def displayScore(self, text, score, x, y, color):
		text = font20.render(text+str(score), True, color)
		textRect = text.get_rect()
		textRect.center = (x, y)

		screen.blit(text, textRect)

	def getRect(self):
		return self.geekRect


# Ball class
class Ball:
	def __init__(self, posx, posy, radius, speed, color):
		self.posx = posx
		self.posy = posy
		self.radius = radius
		self.speed = speed+5
		self.color = color
		self.xFac = 1
		self.yFac = -1
		self.ball = pygame.draw.circle(
			screen, self.color, (self.posx, self.posy), self.radius)
		self.firstTime = 1

	def display(self):
		self.ball = pygame.draw.circle(
			screen, self.color, (self.posx, self.posy), self.radius)

	def update(self):
		self.posx += self.speed*self.xFac
		self.posy += self.speed*self.yFac

		# If the ball hits the top or bottom surfaces,
		# then the sign of yFac is changed and it
		# results in a reflection
		if self.posy <= 0 or self.posy >= HEIGHT:
			self.yFac *= -1

		# If the ball touches the left wall for the first time,
		# The firstTime is set to 0 and we return 1
		# indicating that Geek2 has scored
		# firstTime is set to 0 so that the condition is
		# met only once and we can avoid giving multiple
		# points to the player
		if self.posx <= 0 and self.firstTime:
			self.firstTime = 0
			return 1
		elif self.posx >= WIDTH and self.firstTime:
			self.firstTime = 0
			return -1
		else:
			return 0

	# Used to reset the position of the ball
	# to the center of the screen
	def reset(self):
		self.posx = WIDTH//2
		self.posy = HEIGHT//2
		self.xFac *= -1
		self.firstTime = 1

	# Used to reflect the ball along the X-axis
	def hit(self):
		self.xFac *= -1

	def getRect(self):
		return self.ball

# Game Manager
def main():
    running = True

    # Defining the objects
    geek1 = Striker(20, 0, 10, 100, 10, GREEN)
    geek2 = StrikerCPU(WIDTH-30, 0, 10, 100, 10, RED)
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)

    listOfGeeks = [geek1, geek2]

    # Initial parameters of the players
    geek1Score, geek2Score = 0, 0
    geek1YFac, geek2YFac = 0, 0
    while running:
        screen.fill(BLACK)
        COUNT=0
    # Event handling
        if geek1Score<3 and geek2Score<3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        geek1YFac = -1
                    if event.key == pygame.K_s:
                        geek1YFac = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        geek1YFac = 0

            # Collision detection
            for geek in listOfGeeks:
                if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                        ball.hit()

            # Updating the objects
            geek1.update(geek1YFac)
            geek2.update(geek2YFac,ball,COUNT%30)
            point = ball.update()

            # -1 -> Geek_1 has scored
            # +1 -> Geek_2 has scored
            # 0 -> None of them scored
            if point == -1:
                geek1Score += 1
            elif point == 1:
                geek2Score += 1

            if point: # Someone has scored a point and the
            # ball is out of bounds. So, we reset it's position
                ball.reset()

            # Displaying the objects on the screen
            geek1.display()
            geek2.display()
            ball.display()

            # Displaying the scores of the players
            geek1.displayScore("Player : ", geek1Score, 100, 20, WHITE)
            geek2.displayScore("Enemy : ", geek2Score, WIDTH-100, 20, WHITE)
			
        elif geek1Score>=3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            text = font20.render('You won!',GREEN,BLACK)
            textRect = text.get_rect()
            textRect.center = (WIDTH//2, HEIGHT//2)
            screen.fill(GREEN)
            screen.blit(text, textRect)

        elif geek2Score>=3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            text = font20.render('You lost!',RED,BLACK)
            textRect = text.get_rect()
            textRect.center = (WIDTH//2, HEIGHT//2)
            screen.fill(RED)
            screen.blit(text, textRect)
			

        pygame.display.update()
        COUNT +=1
        # Adjusting the frame rate
        clock.tick(FPS)
	
if __name__=="__main__":
	main()
	pygame.quit
