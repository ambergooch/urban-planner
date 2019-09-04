import datetime

class Building:

    def __init__(self, address, stories):
        self.designer = "Amber Gooch"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now().strftime("%m/%d/%Y")

    def purchase(self, name):
        self.owner = name

    def __str__(self):
        return f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories"




