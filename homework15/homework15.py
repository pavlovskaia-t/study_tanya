class Romb:
    def __init__(self,side_a, angle_a, angle_b):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = angle_b

    def __setattr__(self, key, value):
        if key == 'side_a':
            if value < 0:
                print('ERROR')
            super().__setattr__(key,value)

        elif key == 'angle_a':
            if value > 0:
                super().__setattr__('angle_a', value)
                super().__setattr__('angle_b', 180 - value)

        elif key == 'angle_b':
            if value > 0:
                super().__setattr__('angle_b', value)
                super().__setattr__('angle_a', 180 - value)
        else:
            super().__setattr__(key, value)

romb = Romb(10, 0, 9)
print(romb.side_a)   # 10
print(romb.angle_a)  # 60
print(romb.angle_b)  # 120

