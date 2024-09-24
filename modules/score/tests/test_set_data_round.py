import unittest
import inspect

from modules.score.tournament import Tournament


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tournament = Tournament("teams.csv")
        self.tournament.set_round(inspect.cleandoc(
            """
            T1 - Misifu (Ogre) 1 (0) v 0 (1) Mygaitero (Orc)
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
        """))

    def test_first_data_home(self):
        self.tournament.set_match_data("Misifu", 1, 2, 3, 4)
        self.assertEqual(self.tournament.get_current_round().matches[0].report_home.td_owns, 1)
        self.assertEqual(self.tournament.get_current_round().matches[0].report_home.td_others, 2)
        self.assertEqual(self.tournament.get_current_round().matches[0].report_home.cas_owns, 3)
        self.assertEqual(self.tournament.get_current_round().matches[0].report_home.cas_others, 4)

    def test_first_data_away(self):
        self.tournament.set_match_data("Mygaitero", 1, 2, 3, 4)
        self.assertEqual(self.tournament.get_current_round().matches[0].report_away.td_owns, 1)
        self.assertEqual(self.tournament.get_current_round().matches[0].report_away.td_others, 2)
        self.assertEqual(self.tournament.get_current_round().matches[0].report_away.cas_owns, 3)
        self.assertEqual(self.tournament.get_current_round().matches[0].report_away.cas_others, 4)

    def test_has_reported(self):
        self.tournament.set_match_data("Misifu", 1, 2, 3, 4)
        self.tournament.set_match_data("Mygaitero", 1, 2, 3, 4)
        self.assertTrue(self.tournament.get_current_round().matches[0].has_two_reports())

    def test_home_has_no_reported(self):
        self.tournament.set_match_data("Misifu", 1, 2, 3, 4)
        self.assertTrue(self.tournament.get_current_round().matches[0].report_home.is_reported)

    def test_away_has_no_reported(self):
        self.tournament.set_match_data("Mygaitero", 1, 2, 3, 4)
        self.assertTrue(self.tournament.get_current_round().matches[0].report_away.is_reported)

    def test_data_ok(self):
        self.tournament.set_match_data("Misifu", 1, 2, 3, 4)
        self.tournament.set_match_data("Mygaitero", 2, 1, 4, 3)
        self.assertTrue(self.tournament.get_current_round().matches[0].is_ok())

    def test_data_no_ok(self):
        self.tournament.set_match_data("Misifu", 1, 2, 3, 4)
        self.tournament.set_match_data("Mygaitero", 1, 2, 3, 4)
        self.assertFalse(self.tournament.get_current_round().matches[0].is_ok())

    def test_coaches_has_not_reported(self):
        self.tournament.set_match_data("Misifu", 1, 2, 3, 4)
        self.tournament.set_match_data("Mygaitero", 1, 2, 3, 4)
        coaches_has_not_reported = [x for x in self.tournament.coaches_dict.values()]
        coaches_has_not_reported.remove(self.tournament.coaches_dict["Misifu"])
        coaches_has_not_reported.remove(self.tournament.coaches_dict["Mygaitero"])
        tournament_coaches_have_not_reported = self.tournament.get_current_round().get_coaches_have_not_reported()
        self.assertTrue(len(tournament_coaches_have_not_reported) == len(coaches_has_not_reported))
        for coach in coaches_has_not_reported:
            self.assertTrue(coach in tournament_coaches_have_not_reported)


    def test_matches_are_not_ok(self):
        self.tournament.set_match_data("Misifu", 3, 2, 3, 4)
        self.tournament.set_match_data("Mygaitero", 1, 2, 3, 4)
        for match in self.tournament.get_current_round().matches:
            match.report_home.is_reported = True
            match.report_away.is_reported = True
        self.assertEqual(
            [self.tournament.get_current_round().match_by_coach_name["Misifu"]],
            self.tournament.get_current_round().get_matches_are_not_ok()
        )



if __name__ == '__main__':
    unittest.main()
