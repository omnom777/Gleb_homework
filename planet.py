# class Meme:
#     def __init__(self, tempelate, caption)
#         self.tempelate = tempelate
#         self.caption = caption
#     def post(self):
#         return f'[{tempelate}]:{caption}'
# m = Meme("солом", 'привет')
class Planet:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
    def diameter(self):
        return 2*self.radius
mercury = Planet("Mercury", 1000)
print(mercury.diameter())
