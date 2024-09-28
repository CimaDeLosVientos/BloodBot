from modules.score.coach import Coach
from modules.score.report import Report


class Match:
    def __init__(self, index: int, coach_home: Coach, coach_away: Coach):
        self.index = index
        self.report_home: Report = Report(coach_home)
        self.report_away: Report = Report(coach_away)

    def is_coach_on_match(self, coach_name: str) -> bool:
        return self.report_home.coach.name == coach_name or self.report_away.coach.name == coach_name

    def update_data(self, coach_name: str, td_owns: int, td_others: int, cas_owns: int, cas_others: int):
        if not self.is_coach_on_match(coach_name):
            raise KeyError(f"{coach_name} is not a coach")
        self.get_report_by_coach(coach_name).update_data(td_owns, td_others, cas_owns, cas_others)

    def is_ok(self) -> bool:
        return (self.has_two_reports()
                and self.report_home.td_owns == self.report_away.td_others
                and self.report_home.td_others == self.report_away.td_owns
                and self.report_home.cas_owns == self.report_away.cas_others
                and self.report_home.cas_others == self.report_away.cas_owns
                )

    def has_two_reports(self) -> bool:
        return self.report_home.is_reported and self.report_away.is_reported

    def get_report_trace(self) -> str:
        if not self.is_ok():
            return "ERROR"
        return f"T{self.index},{self.report_home.coach.name},{self.report_away.coach.name},{self.report_home.td_owns}," \
               f"{self.report_home.td_others},{self.report_home.cas_owns},{self.report_home.cas_others}"

    def get_match_trace(self) -> str:
        return f"T{self.index} {self.report_home.coach.name} vs {self.report_away.coach.name}"

    def get_report_by_coach(self, coach_name: str) -> Report:
        if self.report_home.coach.name == coach_name:
            return self.report_home
        if self.report_away.coach.name == coach_name:
            return self.report_away
        raise KeyError(f"{coach_name} is not a coach")
