from turtle import Turtle

class Wall():
    def __init__(self):
            self.bricks =[]
            self.positions= {
               'red': [(250,280), (200,280), (150,280), (100,280), (50,280), (0,280), (-50,280), (-100,280), (-150,280), (-200,280), (-250,280),
                        (250,270), (200,270), (150,270), (100,270), (50,270), (0,270), (-50,270), (-100,270), (-150,270), (-200,270), (-250,270)
               ],
               'orange': [(250,255), (200,255), (150,255), (100,255), (50,255), (0,255), (-50,255), (-100,255), (-150,255), (-200,255), (-250,255),
                        (250,245), (200,245), (150,245), (100,245), (50,245), (0,245), (-50,245), (-100,245), (-150,245), (-200,245), (-250,245)
               ],
                'yellow': [(250,230), (200,230), (150,230), (100,230), (50,230), (0,230), (-50,230), (-100,230), (-150,230), (-200,230), (-250,230),
                        (250,220), (200,220), (150,220), (100,220), (50,220), (0,220), (-50,220), (-100,220), (-150,220), (-200,220), (-250,220)
               ],
               'green': [(250,205), (200,205), (150,205), (100,205), (50,205), (0,205), (-50,205), (-100,205), (-150,205), (-200,205), (-250,205),
                        (250,195), (200,195), (150,195), (100,195), (50,195), (0,195), (-50,195), (-100,195), (-150,195), (-200,195), (-250,195)
               ]
            }
            
    def build(self):
        for color in self.positions:
            for position in self.positions[color]:
                segments_positions = [(position[0]-20, position[1]), (position[0]-15, position[1]), (position[0]-10, position[1]), (position[0]-5, position[1]), (position[0], position[1]), (position[0]+5, position[1]), (position[0]+10, position[1]), (position[0]+15, position[1]), (position[0]+20, position[1])]
                # (position[0]-2.5, position[1]), (position[0]+2.5, position[1]), (position[0]+7.5, position[1])
                self.add_segments(segments_positions, color)

    def add_segments(self, segments_positions, color):
        list_of_segments = []
        for position in segments_positions:
            t1 = self.add_segment(position, color)
            list_of_segments.append(t1)
        self.bricks.append(list_of_segments)


    def add_segment(self, position, color):
        t = Turtle(shape="square")
        t.penup()
        t.shapesize(stretch_len=0.21, stretch_wid=0.33)
        t.color(color)
        t.speed("fastest")
        t.goto(position)
        return t
    
    def disapear(self, brick):
        for segment in brick:
            segment.goto((500,500))


