
class Student:
    def __init__(self, name, korscore, engscore, mathscore):
        self.name = name
        self.korscore = int(korscore)
        self.engscore = int(engscore)
        self.mathscore = int(mathscore)

    def total_score(self):
        return self.korscore + self.engscore + self.mathscore
    
    def avg_score(self):
        return self.total_score() / 3




