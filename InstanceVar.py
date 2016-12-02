class Girl:

    gender = 'female'

    def __init__(self, name):
        self.name = name

        r=Girl("Richa")
        s=Girl("Simmi")
        print(r.gender)
        print(s.gender)
        print(r.name)
        print(s.name)