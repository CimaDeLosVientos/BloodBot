from modules.score.coach import Coach


class Report:
    def __init__(self, coach: Coach):
        self.coach = coach
        self.td_owns = 0
        self.td_others = 0
        self.cas_owns = 0
        self.cas_others = 0
        self.is_reported = False

    def update_data(self, td_owns: int, td_others: int, cas_owns: int, cas_others: int):
        self.td_owns = td_owns
        self.td_others = td_others
        self.cas_owns = cas_owns
        self.cas_others = cas_others
        self.is_reported = True
