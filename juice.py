class FruitJuice:
    def __init__(self):
        self.vsego = 0
        self.v_first_juice = 0
        self.name_first_juice = ""
        self.first_added = False
    
    def add_juice(self, name, volume):
        if self.first_added == False:
            self.name_first_juice = name
            self.v_first_juice = volume
            self.first_added = True
        else:
            if name == self.name_first_juice:
                self.v_first_juice = self.v_first_juice + volume
        
        self.vsego = self.vsego + volume
    
    def pour_out(self, volume):
        if volume > self.vsego:
            volume = self.vsego
        if self.vsego > 0:
            ratio = self.v_first_juice / self.vsego
            self.v_first_juice = self.v_first_juice - (volume * ratio)
        
        self.vsego = self.vsego - volume
    
    def get_concentration(self):
        if self.vsego == 0:
            return 0
        else:
            return self.v_first_juice / self.vsego
    
juice = FruitJuice()
print(juice.get_concentration())
juice.add_juice("яблочный", 200)
juice.add_juice("банановый", 200)
print( juice.get_concentration())
juice.pour_out(200)
juice.add_juice("яблочный", 200)
print(juice.get_concentration())