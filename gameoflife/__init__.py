class GameOfLife:

    def __init__(self, seed):
        self._state = set(seed)

    @property
    def state(self):
        return self._state

    def tick(self):
        pass

    def die(self, cell):
        self._state.remove(cell)

    def live(self, cell):
        self._state.add(cell)

    def is_alive(self, cell):
        return cell in self._state

    def get_neighbors_count(self, cell):
        cell_x, cell_y = cell
        neighbors = [self.is_alive((cell_x + x, cell_y + y))
                     for x, y in
                     zip((-1, 1, 1, 1, 0, 0, 1, -1),
                         (-1, 1, -1, 1, -1, 1, 0, 0))]
        return sum(neighbors)

    def __str__(self):
        pass
