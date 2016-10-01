from config import SNAKE_MOVE_SPEED


class SnakeHead:
    def tick(self, delta_time):
        location = self.uobject.get_actor_location()

        location += self.uobject.get_actor_forward() * SNAKE_MOVE_SPEED * delta_time

        self.uobject.set_actor_location(location)

    def __spawn_body(self):
        snake_body = self.uobject.call_function('SpawnSnakeBody')


