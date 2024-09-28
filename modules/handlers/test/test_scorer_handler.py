import unittest
import inspect

from modules.handlers.scorer_handler import ScorerHandler
from modules.score.tournament import Tournament
from modules.util.send_message_command import SendMessageCommand


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.scorer = ScorerHandler()
        self.arguments = {
            'chat': '335',
            'text': ""
        }
        self.scorer.tournament = Tournament("teams.csv")
        for coach_index, coach in enumerate(self.scorer.tournament.coaches_dict.values()):
            coach.telegram_id = coach_index

        self.basic_match = inspect.cleandoc("""/set_round T1 - Misifu (Ogre) 1 (0) v 0 (1) Mygaitero (Orc)
            T2 - Fran Mutado (Dwarf) 2 (6) v 1 (0) H3ct0r (Chaos Chosen)
            T3 - Abaddon (Underworld Denizens) 2 (6) v 1 (0) Karrashantemi (Elf Union)
            T4 - glukosidiko (Underworld Denizens) 2 (3) v 0 (1) Jose_Q (Shambling Undead)
            T5 - Metzar (Elf Union) 0 (0) v 2 (2) MapacheCoactivo (Imperial Nobility)
            T6 - Estertor (Dwarf) 0 (0) v 1 (1) Dakathllu (Human)
            T7 - zZKing (Human) 3 (2) v 1 (2) Totay (Khorne)
            T8 - Aguss (Khorne) 1 (3) v 0 (0) RojoCinco (Chaos Renegade)
            T9 - Shirokov (Underworld Denizens) 2 (3) v 1 (3) Xinalake (Chaos Renegade)
            T10 - Gpo (Tomb Kings) 1 (0) v 1 (0) jaruib (Dwarf)
            T11 - Pablo1880 (Underworld Denizens) 1 (1) v 0 (4) Tharsis (Khorne)
            T12 - Chache Perrache (Necromantic Horror) 1 (1) v 0 (2) Duke_Luthor_Von_Hawkfire (Dwarf)
            T13 - Weiss Akenatae (Chaos Dwarf) 1 (1) v 0 (1) Kwe (Chaos Chosen)
            T14 - Hurgh (Black Orc) 0 (3) v 2 (0) Ironcat (Dark Elf)
            T15 - Manra69 (Shambling Undead) 1 (0) v 2 (1) Rafmar (Dwarf)
            T16 - Celata (Norse) 1 (0) v 0 (1) Koki (Dark Elf)
            T17 - Calltroop (Amazon) 1 (2) v 0 (3) Paezinho (Shambling Undead)
            T18 - Ziost (Elf Union) 0 (0) v 1 (4) Maquinator (Khorne)
            T19 - Kale (Black Orc) 0 (3) v 1 (3) eu4rico (Shambling Undead)
            T20 - Azaghtogh (Dark Elf) 1 (0) v 1 (2) Lord Arioch (Shambling Undead)
            T21 - Hachablanca (Dark Elf) 2 (2) v 2 (0) David_Q (Human)
            T22 - Judaspainkiller (Shambling Undead) 1 (5) v 1 (1) adrianeden (Goblin)
            T23 - Bileman (Underworld Denizens) 1 (1) v 0 (7) LOBERAS (Shambling Undead)
            T24 - Serserius (Necromantic Horror) 0 (4) v 2 (5) Javin_23 (Underworld Denizens)
            T25 - SirSergio (Amazon) 0 (0) v 2 (2) BARBANCHO (Nurgle)
            T26 - Troloe (Goblin) 0 (3) v 1 (5) Xiete (Nurgle)
            T27 - Godzilla (Khorne) 3 (2) v 0 (2) bululito (Imperial Nobility)
            T28 - MagdaBB (Orc) 0 (0) v 2 (1) Galle (Halfling)
            T29 - Bubba (Snotling) 2 (2) v 1 (7) Jull45 (Necromantic Horror)
            T30 - Chemarvi (Halfling) 1 (4) v 1 (1) Ferre (Nurgle)
            T31 - Ronda (Necromantic Horror) 2 (3) v 0 (7) Lord_buba (Goblin)
            T32 - Sir Mayans (Chaos Renegade) 2 (3) v 1 (1) Pawel406 (Underworld Denizens)
            T33 - EduarSmoka (Lizardmen) 0 (3) v 3 (6) SrLombard (Dark Elf)
            T34 - Nopher (Skaven) 5 (6) v 1 (1) Leinad (Amazon)
            T35 - Harec (Snotling) 0 (1) v 1 (5) Pas_Mao (Orc)
            T36 - Serrano 65 (Elf Union) 6 (5) v 1 (0) Yorch (Goblin)
            T37 - skaripense (Norse) 2 (5) v 1 (1) Neo_Chains (Goblin)
            T38 - Purohit (Underworld Denizens) 0 (3) v 1 (2) Gabillas (Dark Elf)
            T39 - Sandor (Necromantic Horror) 2 (2) v 0 (4) Peluwo (Necromantic Horror)
            T40 - Pececito (Dark Elf) 2 (0) v 0 (3) Coates (Dwarf)
            T41 - Emiliakus (Dark Elf) 2 (0) v 0 (4) Golum89 (Norse)
        """)
        #'/link_user': self.link_user,
        #'/create_tournament': self.create_tournament,
        #'/set_round': self.set_round,
        #'/report': self.report,
        #'/is_all_reported': self.is_all_reported,
        #'/is_all_ok': self.is_all_ok

    def test_link_user_not_tournament(self):
        self.scorer.tournament = None
        self.arguments['text'] = "/link_user Misifu"
        response = self.scorer.link_user(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.no_tournament_active,
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)

    def test_link_user_ok(self):
        self.arguments['text'] = "/link_user Misifu"
        response = self.scorer.link_user(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.link_id_successful.format("Misifu"),
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)

    def test_link_user_fail(self):
        self.arguments['text'] = "/link_user MisiFALSO"
        response = self.scorer.link_user(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.link_id_fail.format("MisiFALSO"),
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)

    def test_create_tournament_ok(self):
        self.arguments['text'] = "/link_user teams.csv"
        response = self.scorer.create_tournament(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.tournament_created_successful,
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)

    def test_create_tournament_fail(self):
        self.arguments['text'] = "/link_user teams.csv"
        response = self.scorer.create_tournament(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.tournament_created_successful,
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)

    def test_create_tournament_bad_parameters(self):
        self.arguments['text'] = "/link_user teams.csv"
        response = self.scorer.create_tournament(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.tournament_created_successful.format("teasms.csv"),
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)

    def test_create_round_ok(self):
        self.arguments['text'] = self.basic_match
        response = self.scorer.set_round(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.round_created_successful,
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)

    def test_create_round_fail(self):
        self.arguments['text'] = inspect.cleandoc("""/set_round T1 - MisiFALSO (Ogre) 1 (0) v 0 (1) Mygaitero (Orc)
                    T2 - Fran Mutado (Dwarf) 2 (6) v 1 (0) H3ct0r (Chaos Chosen)
                    T3 - Abaddon (Underworld Denizens) 2 (6) v 1 (0) Karrashantemi (Elf Union)
                    T4 - glukosidiko (Underworld Denizens) 2 (3) v 0 (1) Jose_Q (Shambling Undead)
                    T5 - Metzar (Elf Union) 0 (0) v 2 (2) MapacheCoactivo (Imperial Nobility)
                    T6 - Estertor (Dwarf) 0 (0) v 1 (1) Dakathllu (Human)
                    T7 - zZKing (Human) 3 (2) v 1 (2) Totay (Khorne)
                    T8 - Aguss (Khorne) 1 (3) v 0 (0) RojoCinco (Chaos Renegade)
                    T9 - Shirokov (Underworld Denizens) 2 (3) v 1 (3) Xinalake (Chaos Renegade)
                    T10 - Gpo (Tomb Kings) 1 (0) v 1 (0) jaruib (Dwarf)
                    T11 - Pablo1880 (Underworld Denizens) 1 (1) v 0 (4) Tharsis (Khorne)
                    T12 - Chache Perrache (Necromantic Horror) 1 (1) v 0 (2) Duke_Luthor_Von_Hawkfire (Dwarf)
                    T13 - Weiss Akenatae (Chaos Dwarf) 1 (1) v 0 (1) Kwe (Chaos Chosen)
                    T14 - Hurgh (Black Orc) 0 (3) v 2 (0) Ironcat (Dark Elf)
                    T15 - Manra69 (Shambling Undead) 1 (0) v 2 (1) Rafmar (Dwarf)
                    T16 - Celata (Norse) 1 (0) v 0 (1) Koki (Dark Elf)
                    T17 - Calltroop (Amazon) 1 (2) v 0 (3) Paezinho (Shambling Undead)
                    T18 - Ziost (Elf Union) 0 (0) v 1 (4) Maquinator (Khorne)
                    T19 - Kale (Black Orc) 0 (3) v 1 (3) eu4rico (Shambling Undead)
                    T20 - Azaghtogh (Dark Elf) 1 (0) v 1 (2) Lord Arioch (Shambling Undead)
                    T21 - Hachablanca (Dark Elf) 2 (2) v 2 (0) David_Q (Human)
                    T22 - Judaspainkiller (Shambling Undead) 1 (5) v 1 (1) adrianeden (Goblin)
                    T23 - Bileman (Underworld Denizens) 1 (1) v 0 (7) LOBERAS (Shambling Undead)
                    T24 - Serserius (Necromantic Horror) 0 (4) v 2 (5) Javin_23 (Underworld Denizens)
                    T25 - SirSergio (Amazon) 0 (0) v 2 (2) BARBANCHO (Nurgle)
                    T26 - Troloe (Goblin) 0 (3) v 1 (5) Xiete (Nurgle)
                    T27 - Godzilla (Khorne) 3 (2) v 0 (2) bululito (Imperial Nobility)
                    T28 - MagdaBB (Orc) 0 (0) v 2 (1) Galle (Halfling)
                    T29 - Bubba (Snotling) 2 (2) v 1 (7) Jull45 (Necromantic Horror)
                    T30 - Chemarvi (Halfling) 1 (4) v 1 (1) Ferre (Nurgle)
                    T31 - Ronda (Necromantic Horror) 2 (3) v 0 (7) Lord_buba (Goblin)
                    T32 - Sir Mayans (Chaos Renegade) 2 (3) v 1 (1) Pawel406 (Underworld Denizens)
                    T33 - EduarSmoka (Lizardmen) 0 (3) v 3 (6) SrLombard (Dark Elf)
                    T34 - Nopher (Skaven) 5 (6) v 1 (1) Leinad (Amazon)
                    T35 - Harec (Snotling) 0 (1) v 1 (5) Pas_Mao (Orc)
                    T36 - Serrano 65 (Elf Union) 6 (5) v 1 (0) Yorch (Goblin)
                    T37 - skaripense (Norse) 2 (5) v 1 (1) Neo_Chains (Goblin)
                    T38 - Purohit (Underworld Denizens) 0 (3) v 1 (2) Gabillas (Dark Elf)
                    T39 - Sandor (Necromantic Horror) 2 (2) v 0 (4) Peluwo (Necromantic Horror)
                    T40 - Pececito (Dark Elf) 2 (0) v 0 (3) Coates (Dwarf)
                    T41 - Emiliakus (Dark Elf) 2 (0) v 0 (4) Golum89 (Norse)
                """)
        response = self.scorer.set_round(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.round_created_error,
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)

    def test_error_data(self):
        self.arguments['text'] = self.basic_match
        self.scorer.set_round(self.arguments)
        self.arguments['text'] = "/report MisiFalso 1 2 3 4"
        response = self.scorer.report(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.report_error,
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)

    def test_first_data(self):
        self.arguments['text'] = self.basic_match
        self.scorer.set_round(self.arguments)
        self.arguments['text'] = "/report Misifu 1 2 3 4"
        response = self.scorer.report(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.first_report_received,
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)


    def test_second_data_ok(self):
        self.arguments['text'] = self.basic_match
        self.scorer.set_round(self.arguments)
        self.scorer.tournament.get_current_round().update_data("Misifu", 1, 2, 3, 4)
        self.arguments['text'] = "/report Mygaitero 2 1 4 3"
        response = self.scorer.report(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.second_report_received_ok,
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)


    def test_second_data_bad(self):
        self.arguments['text'] = self.basic_match
        self.scorer.set_round(self.arguments)
        self.scorer.tournament.get_current_round().update_data("Misifu", 1, 2, 3, 4)
        self.arguments['text'] = "/report Mygaitero 2 1 4 4"
        response = self.scorer.report(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.second_report_received_fail,
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)

    def test_is_all_reported_yes(self):
        self.arguments['text'] = self.basic_match
        self.scorer.set_round(self.arguments)
        for match in self.scorer.tournament.get_current_round().matches:
            match.report_home.is_reported = True
            match.report_away.is_reported = True
        self.arguments['text'] = "/is_all_reported"
        response = self.scorer.is_all_reported(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.is_all_reported_true,
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)

    def test_is_all_reported_no(self):
        self.arguments['text'] = self.basic_match
        self.scorer.set_round(self.arguments)
        for match in self.scorer.tournament.get_current_round().matches:
            match.report_home.is_reported = True
            match.report_away.is_reported = True
        self.scorer.tournament.get_current_round().match_by_coach_name["Misifu"].report_home.is_reported = False
        self.scorer.tournament.get_current_round().match_by_coach_name["Hurgh"].report_home.is_reported = False
        self.arguments['text'] = "/is_all_reported"
        response = self.scorer.is_all_reported(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.is_all_reported_false.format("Misifu, Hurgh"),
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)

    def test_is_all_ok_yes(self):
        self.arguments['text'] = self.basic_match
        self.scorer.set_round(self.arguments)
        for match in self.scorer.tournament.get_current_round().matches:
            match.report_home.is_reported = True
            match.report_away.is_reported = True
        self.arguments['text'] = "/is_all_ok"
        response = self.scorer.is_all_ok(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.is_all_ok_true,
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)

    def test_is_all_ok_no(self):
        self.arguments['text'] = self.basic_match
        self.scorer.set_round(self.arguments)
        for match in self.scorer.tournament.get_current_round().matches:
            match.report_home.is_reported = True
            match.report_away.is_reported = True
        self.scorer.tournament.set_match_data("Misifu", 1, 2, 3, 4)
        self.scorer.tournament.set_match_data("Mygaitero", 1, 2, 3, 4)
        self.arguments['text'] = "/is_all_ok"
        response = self.scorer.is_all_ok(self.arguments)
        expected_response = SendMessageCommand(self.scorer.texts.is_all_ok_false.format("T1 Misifu vs Mygaitero"),
                                               self.arguments['chat'])
        self.assertEqual(expected_response.url_command, response.url_command)

if __name__ == '__main__':
    unittest.main()
