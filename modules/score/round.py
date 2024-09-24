from modules.score.coach import Coach
from modules.score.match import Match
from typing import List, Dict, Tuple


class Round:
    def __init__(self, matches_list: str, coaches_dict: Dict[str, Coach]):
        self.coaches_dict = coaches_dict
        self.matches: List[Match] = []
        self.match_by_coach_name: Dict[str, Match] = {}
        self.load_matches(matches_list)

    def update_data(self, coach_name: str, td_owns: int, td_others: int, cas_owns: int, cas_others: int):
        self.match_by_coach_name[coach_name].update_data(coach_name, td_owns, td_others, cas_owns, cas_others)

    def load_matches(self, matches_list: str) -> None:
        matches_raw = matches_list.split('\n')
        for match in matches_raw:
            if match == "":
                continue
            matches_tuple = self.parse_match(match)
            match_object = Match(
                int(matches_tuple[0][1:]),
                self.coaches_dict[matches_tuple[1]],
                self.coaches_dict[matches_tuple[2]]
            )
            self.matches.append(match_object)
            self.match_by_coach_name[matches_tuple[1]] = match_object
            self.match_by_coach_name[matches_tuple[2]] = match_object


    def parse_match(self, match: str) -> Tuple[str, str, str]:
        index = match[:match.find(' -')]
        home_coach_name = match[match.find('- ')+2:match.find(' (')]
        second_part = match[match.find(' v '):]
        away_coach_name = second_part[second_part.find(') ')+2:second_part.rfind(' (')]
        return index, home_coach_name, away_coach_name

    def get_coaches_have_not_reported(self) -> List[Coach]:
        coaches_have_not_reported = []
        for match in self.matches:
            if not match.report_home.is_reported:
                coaches_have_not_reported.append(match.report_home.coach)
            if not match.report_away.is_reported:
                coaches_have_not_reported.append(match.report_away.coach)
        return coaches_have_not_reported

    def get_matches_are_not_ok(self) -> List[Match]:
        matches_are_not_ok = []
        for match in self.matches:
            if not match.is_ok():
                matches_are_not_ok.append(match)
        return matches_are_not_ok
