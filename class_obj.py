class Games_record:
    def __init__(self, name, score, hours):
        self.name = name
        self.score = score
        self.hours = hours

    def high_score(self):
        print(f"{self.name} has reached a high score of {self.score}")

    def score_per_time(self):
        print(f"{self.name} achieved a high score at the rate of {int(self.score/self.hours)} per hour.")

caio = Games_record("Caio", 2000, 3)
caio.high_score()
caio.score_per_time()
