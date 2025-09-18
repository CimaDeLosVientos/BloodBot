import xml.etree.ElementTree as ET
from typing import Dict

from modules.score.coach import Coach
from modules.score.round import Round
from modules.score.match import Match

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
            index = 0
            reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            next(reader, None)
            for index, row in enumerate(reader):
                coach_name = row[3]
                if coach_name == "" or row[-1] == 'false':
                    continue
                if coach_name in coach_dict.keys():
                    raise ValueError(f'Duplicate coach coach_name: {coach_name}')
                coach_dict[coach_name] = Coach(index, coach_name, "-1")
        return coach_dict

    def write_rounds(self) -> None:
        root = ET.Element("xml")
        for round_index, round in enumerate(self.rounds):
            round_element = ET.SubElement(root, "round", number=f"{round_index}")
            self.write_round(round, round_element)

        tree = ET.ElementTree(root)
        tree.write("filename.xml")

    def write_round(self, round: Round, root: ET.Element) -> None:
        ET.SubElement(root, "time").text = " "
        for match in round.matches:
            game = ET.SubElement(root, "game", table=f"{match.index-1}")
            self.write_game(match, game)

    def write_game(self, match: Match, root: ET.Element) -> None:
        ET.SubElement(root, "team1").text = str(match.report_home.coach.index)
        ET.SubElement(root, "team2").text = str(match.report_away.coach.index)
        ET.SubElement(root, "td1").text = str(match.report_home.td_owns)
        ET.SubElement(root, "td2").text = str(match.report_home.td_others)
        ET.SubElement(root, "cas1").text = str(match.report_home.cas_owns)
        ET.SubElement(root, "cas2").text = str(match.report_home.cas_others)
        ET.SubElement(root, "conceded1").text = "-1"
        ET.SubElement(root, "conceded2").text = "-1"
        ET.SubElement(root, "bonus1").text = "-99999"
        ET.SubElement(root, "bonus2").text = "-99999"
