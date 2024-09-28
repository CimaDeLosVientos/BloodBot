############
## SCORER ##
############
from ..score.tournament import Tournament
from ..util.send_message_command import SendMessageCommand
from ..util.telegram_command import TelegramCommand
from ..util.telegram_methods import *
from ..util.checkinator import *


class ScorerHandlerTexts:
    def __init__(self):
        self.no_tournament_active = "No hay ningún torneo en curso"
        self.link_id_successful = "¡Perfecto! Tu id ya está vinculado al entrenador {}"
        self.link_id_fail = "¡Error! No existe ningún coach con el nombre {} registrado en el torneo. Asegurate de que has escrito correctamente tu nombre de entrenador"
        self.tournament_created_successful = "Torneo creado exitosamente"
        self.tournament_created_error = "El archivo de equipos {} no ha sido encontrado"
        self.round_created_successful = "La ronda se ha creado exitosamente"
        self.round_created_error = "Ha habido un error al crear la ronda"
        self.report_error = "No has escrito bien tu nombre de entrenador. Revísalo e intentalo de nuevo, por favor"
        self.first_report_received = "Reporte recibido correctamente. Tu oponente aún no ha mandado el suyo"
        self.second_report_received_ok = "Reporte recibido correctamente. Los datos coinciden con los de tu oponente, la organización estará feliz"
        self.second_report_received_fail = "Reporte recibido correctamente. Pero los datos NO COINCIDEN con los de tu oponente, tratad de poneros de acuerdo y volved a reportar según proceda"
        self.is_all_reported_true = "Todos los reportes han sido enviados"
        self.is_all_reported_false = "Faltan los reportes de {}"
        self.is_all_ok_true = "Todos los reportes coinciden"
        self.is_all_ok_false = "Hay discrepancias en los reportes del partido {}"


class ScorerHandler(object):
    """
    ! ESTO ESTÁ PLANTEADO DE MANERA QUE SÓLO EXISTIRÁ UNA INSTANCIA, ES DECIR, NO PUEDE HABER TORNEOS PARALELOS.
    """

    def __init__(self):
        self.texts = ScorerHandlerTexts()
        self.tournament = None
        # Command dictionaries
        self.commands_with_backslash = {
            '/link_user': self.link_user,
            '/create_tournament': self.create_tournament,
            '/set_round': self.set_round,
            '/report': self.report,
            '/is_all_reported': self.is_all_reported,
            '/is_all_ok': self.is_all_ok
        }

        self.commands_without_backslash = {

        }

    #@checkinator(("coach_name", check_string), contains_command=True)
    def link_user(self, arguments) -> TelegramCommand:
        if self.tournament is None:
            return SendMessageCommand(self.texts.no_tournament_active, arguments['chat'], False)
        coach_name = arguments['text'][arguments['text'].index(" ") + 1:]
        if coach_name in self.tournament.coaches_dict.keys():
            self.tournament.coaches_dict[coach_name].telegram_id = arguments['chat']
            return SendMessageCommand(self.texts.link_id_successful.format(coach_name), arguments['chat'], False)
        return SendMessageCommand(self.texts.link_id_fail.format(coach_name), arguments['chat'], False)

    def create_tournament(self, arguments) -> TelegramCommand:
        filename = arguments['text'][arguments['text'].index(" ") + 1:]
        try:
            self.tournament = Tournament(filename)
            return SendMessageCommand(self.texts.tournament_created_successful, arguments['chat'], False)
        except:
            return SendMessageCommand(self.texts.tournament_created_error, arguments['chat'], False)

    def set_round(self, arguments) -> TelegramCommand:
        matches_print = arguments['text'][arguments['text'].index(" ") + 1:]
        try:
            self.tournament.set_round(matches_print)
            return SendMessageCommand(self.texts.round_created_successful, arguments['chat'], False)
        except:
            return SendMessageCommand(self.texts.round_created_error, arguments['chat'], False)

    @checkinator(("coach_name", check_string), ("td_owns", check_int), ("td_others", check_int), ("cas_owns", check_int), ("cas_others", check_int), contains_command=True)
    def report(self, arguments) -> TelegramCommand:
        match = None
        try:
            match = self.tournament.get_current_round().match_by_coach_name[arguments['coach_name']]
        except KeyError:
            return SendMessageCommand(self.texts.report_error, arguments['chat'], False)
        match.update_data(arguments['coach_name'], arguments['td_owns'], arguments['td_others'], arguments['cas_owns'], arguments['cas_others'])

        if match.has_two_reports():
            if match.is_ok():
                return SendMessageCommand(self.texts.second_report_received_ok, arguments['chat'], False)
            return SendMessageCommand(self.texts.second_report_received_fail, arguments['chat'], False)
        return SendMessageCommand(self.texts.first_report_received, arguments['chat'], False)

    def is_all_reported(self, arguments) -> TelegramCommand:
        coaches_have_not_reported = self.tournament.get_current_round().get_coaches_have_not_reported()
        if coaches_have_not_reported:
            response_text = ", ".join([coach.name for coach in coaches_have_not_reported])
            return SendMessageCommand(self.texts.is_all_reported_false.format(response_text), arguments['chat'], False)
        return SendMessageCommand(self.texts.is_all_reported_true, arguments['chat'], False)

    def is_all_ok(self, arguments) -> TelegramCommand:
        matches_are_not_ok = self.tournament.get_current_round().get_matches_are_not_ok()
        if matches_are_not_ok:
            response_text = "\n".join([match.get_match_trace() for match in matches_are_not_ok])
            return SendMessageCommand(self.texts.is_all_ok_false.format(response_text), arguments['chat'], False)
        return SendMessageCommand(self.texts.is_all_ok_true, arguments['chat'], False)
