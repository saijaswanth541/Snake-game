from collections import namedtuple

Body = namedtuple('Body', ['head', 'size', 'colour'])

class GetTupleFunctions:
    """
    Tuple func.
    """
    def __init__(self, tup):
        """Get tuple attributes.

        Parameters:
        ------------------------------------------
        namedTuple
        """
        self.tup = tup

    def get_coordinates(self):
        """return head
        """
        return self.tup.head

    def get_size(self):
        """return size
        """
        return self.tup.size

    def get_colour(self):
        """return colour
        """
        return self.tup.colour



class Snake:
    """
    Snake Class using named tuple.
    """
    def __init__(self, head, size, colour):
        """Init__.

        Parameters:
        ------------------------------------------
        colour
        head
        size
        """
        self.body_length = 1
        self.size = size
        self.colour = colour
        self.bodyparts = []
        self.head = head
        body = Body(head, size, colour)
        self.bodyparts.append(body)

    def previous_head(self):
        """store previous head into self.head
        """
        self.head = (self.bodyparts[0].head[0], self.bodyparts[0].head[1])

    def move_left(self):
        """Move left
        """
        self.previous_head()
        for i in range(len(self.bodyparts)-1, -1, -1):
            if i == 0:
                self.bodyparts[0] = self.bodyparts[0]._replace(head=(self.head[0] - self.size[0], self.head[1]))
            else:
                self.bodyparts[i] = self.bodyparts[i]._replace(head=self.bodyparts[i-1].head)


    def move_right(self):
        """Move right
        """
        self.previous_head()
        for i in range(len(self.bodyparts)-1, -1, -1):
            if i == 0:
                self.bodyparts[0] = self.bodyparts[0]._replace(head=(self.head[0] + self.size[0], self.head[1]))
            else:
                self.bodyparts[i] = self.bodyparts[i]._replace(head=self.bodyparts[i-1].head)


    def move_up(self):
        """Move up
        """
        self.previous_head()
        for i in range(len(self.bodyparts)-1, -1, -1):
            if i == 0:
                self.bodyparts[0] = self.bodyparts[0]._replace(head=(self.head[0], self.head[1] - self.size[1]))
            else:
                self.bodyparts[i] = self.bodyparts[i]._replace(head=self.bodyparts[i-1].head)


    def move_down(self):
        """Move down
        """
        self.previous_head()
        # replace every next body to its next
        for i in range(len(self.bodyparts)-1, -1, -1):
            if i == 0:
                self.bodyparts[0] = self.bodyparts[0]._replace(head=(self.head[0], self.head[1] + self.size[1]))
            else:
                self.bodyparts[i] = self.bodyparts[i]._replace(head=self.bodyparts[i-1].head)


    def grow(self):
        """Grow function.
        """
        body = Body(self.bodyparts[-1].head, self.size, self.colour)
        self.bodyparts.append(body)
        self.body_length += 1

    def inside_bounds(self, top_left_point, down_right_point):
        """Inside bounds function.

        Parameters:
            top_left_point
            down_right_point
        """
        left_x_body = self.bodyparts[0].head[0]
        right_x_body = self.bodyparts[0].head[0] + self.size[0]
        top_y_body = self.bodyparts[0].head[1]
        down_y_body = self.bodyparts[0].head[1] + self.size[1]
        if top_left_point[0] <= left_x_body <= down_right_point[0] and top_left_point[1] <= top_y_body <= down_right_point[1]:
            if top_left_point[0] <= left_x_body <= down_right_point[0] and top_left_point[1] <= down_y_body <= down_right_point[1]:
                if top_left_point[0] <= right_x_body <= down_right_point[0] and top_left_point[1] <= top_y_body <= down_right_point[1]:
                    if top_left_point[0] <= right_x_body <= down_right_point[0] and top_left_point[1] <= down_y_body <= down_right_point[1]:
                        return True
        return False

    def check_collision_with_fruit(self, top_left_point, down_right_point):
        """Check collision with fruit.

        Parameters:
            top_left_point
            down_right_point
        """
        body = self.bodyparts[0]
        if body.head[0] == top_left_point[0] and body.head[1] == top_left_point[1]:
            return True
        return False


    def check_collision_with_self(self):
        """Check collision with self.
        """

        for blockindex in range(1, len(self.bodyparts)):
            if self.bodyparts[0].head == self.bodyparts[blockindex].head and self.bodyparts[0].size == self.bodyparts[blockindex].size:
                return True
        return False

    def check_head_coincide(self, headnew):
        """check head coincide
        """
        if headnew == self.bodyparts[0].head:
            return True
        return False

    def check_point_inside(self, top_left_point, down_right_point, block):
        """check point inside
        """
        if (top_left_point[0] < block.head[0] < down_right_point[0] and top_left_point[1] < block.head[1] < down_right_point[1]) or (top_left_point[0] < block.head[0] + self.size[0] < down_right_point[0] and top_left_point[1] < block.head[1] < down_right_point[1]):
            return True
        if top_left_point[0] < block.head[0] < down_right_point[0] and top_left_point[1] < block.head[1] + self.size[1] < down_right_point[1]:
            return True
        if top_left_point[0] < block.head[0] + self.size[0] < down_right_point[0] and top_left_point[1] < block.head[1] + self.size[1] < down_right_point[1]:
            return True
        return False

    def check_collision(self, top_left_point, down_right_point):
        """Check collision.

        Parameters:
            top_left
            bottom_right
        """
        for block in self.bodyparts:
            if self.check_point_inside(top_left_point, down_right_point, block):
                return True
        if self.check_head_coincide(top_left_point):
            return True
        return False


    def __iter__(self):
        """iterator
        """
        self.iteratorlimit = 0
        return self

    def __next__(self):
        """next of iter
        """
        if self.iteratorlimit < self.body_length:
            self.iteratorlimit += 1
            index = self.iteratorlimit
            return GetTupleFunctions(self.bodyparts[index - 1])
        raise StopIteration
