"""
Design Snake Game


Design a Snake game that is played on a device with screen size height x width. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0, 0) with a length of 1 unit.

You are given an array food where food[i] = (ri, ci) is the row and column position of a piece of food that the snake can eat. When a snake eats a piece of food, its length and the game's score both increase by 1.

Each piece of food appears one by one on the screen, meaning the second piece of food will not appear until the snake eats the first piece of food.

When a piece of food appears on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

The game is over if the snake goes out of bounds (hits a wall) or if its head occupies a space that its body occupies after moving (i.e. a snake of length 4 cannot run into itself).

Implement the SnakeGame class:

SnakeGame(int width, int height, int[][] food) Initializes the object with a screen of size height x width and the positions of the food.
int move(String direction) Returns the score of the game after applying one direction move by the snake. If the game is over, return -1.


thoughts

1. width and height is the screens
2. food is the quantity 
    1. increase score
    2. increase snakes length
3. if the length goes beyond width and height failed
4. define direction map in the class

game ends
1. snakes goes beyond boundary
2. if it hits one of the boundaries
3. if snake bites itself

should we store its tail and head positions ?


"""


from collections import deque


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque([(0, 0)])
        self.snake_set = {(0,0): 1}
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.directions = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
        

    def move(self, direction: str) -> int:
        x, y = self.snake[0]
        dx, dy = self.directions[direction]

        new_x, new_y = x+dx, y+dy
        if 0 <= new_x < self.height and 0<=new_y < self.width:
            
            # Checking if the snake bites itself.
            bites_itself = (new_x, new_y) in self.snake_set and (new_x, new_y) != self.snake[-1]
            if bites_itself:
                return -1
            
            next_food_item = self.food[self.food_index] if self.food_index < len(self.food) else None

            # If there's an available food item and it is on the cell occupied by the snake after the move, eat it
            if self.food_index < len(self.food) and tuple(next_food_item) == (new_x, new_y):
                self.food_index += 1
            else:
                # not eating food: delete tail
                tail = self.snake.pop()
                del self.snake_set[tail]
            # A new head always gets added
            self.snake.appendleft((new_x, new_y))
            # Also add the head to the set
            self.snake_set[(new_x, new_y)] = 1
            return len(self.snake) - 1
                
        return -1

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)