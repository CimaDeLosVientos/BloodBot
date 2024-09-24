import xml.etree.ElementTree as ET
from typing import Dict

from modules.score.coach import Coach
from modules.score.round import Round

import csv




class Tournament:
    def __init__(self, coaches_file: str):
        self.rounds = []
        self.coaches_dict = self.load_coaches_csv(coaches_file)
        self.current_index_round = 0

    # DEPRECATED
    def load_coaches_xml(self, coaches_file: str) -> Dict[str, Coach]:
        xml_data = ET.parse(coaches_file)
        coach_dict = {}
        root = xml_data.getroot()
        for coach in root[1]:
            name = coach[0].text
            if name in coach_dict.keys():
                raise ValueError(f'Duplicate coach name: {name}')
            coach_dict[name] = Coach(name, "-1")
        return coach_dict

    def set_telegram_id(self, coach_name: str, telegram_id: str) -> bool:
        for coach_name, coach in self.coaches_dict:
            if coach.name == coach_name:
                coach.telegram_id = telegram_id
                return True
        return False

    def set_round(self, matches_print: str):
        self.rounds.append(Round(matches_print, self.coaches_dict))

    def get_current_round(self) -> Round:
        return self.rounds[self.current_index_round]

    def set_match_data(self, coach_name: str, td_owns: int, td_others: int, cas_owns: int, cas_others: int) -> None:
        self.get_current_round().update_data(coach_name, td_owns, td_others, cas_owns, cas_others)

    def load_coaches_csv(self, coaches_file: str) -> Dict[str, Coach]:
        coach_dict = {}
        with open(coaches_file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            next(reader, None)
            for row in reader:
                coach_name = row[3]
                if coach_name == "" or row[-1] == 'false':
                    continue
                if coach_name in coach_dict.keys():
                    raise ValueError(f'Duplicate coach coach_name: {coach_name}')
                coach_dict[coach_name] = (Coach(coach_name, "-1"))
        return coach_dict

