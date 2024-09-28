import modules.config as config
from .handlers.scorer_handler import ScorerHandler

from .util.telegram_methods import *
from .util.checkinator import *
from .util.states_handler import *

from .handlers import prueba

######################################################################
#################### PARÁMETROS MODIFICABLES #########################
######################################################################


URL = "https://api.telegram.org/bot{}/".format(config.TOKEN)
scorer = ScorerHandler()


# Aquí estaba el manejador de estados


########################
## HANDLER OF UPDATES ##
########################

def handle(update):
    """
    This function is called every time a message arrives to any chat.
    Extracts the key arguments of the update in a dictionary and evaluate what command it is or if is there ongoing process.
    Finally, executes the command invoked in the chat or the next step from ongoing process through the corresponding function and its parameters.
    It also handles exceptions during execution.

    # TODO pasar esto a una estructura para que sea más fácil de trabajar en edición
    
    :param      update:  The update
    :type       update:  Update
    """
    if 'message' in update and 'text' in update["message"]:
        arguments = {
            'text': update["message"]["text"],
            'chat': update["message"]["chat"]["id"],
            'user': update["message"]["from"]["id"],
            'message': update["message"]["message_id"],
            'reply_to_message': None
        }
        if 'reply_to_message' in update["message"].keys():  # Only replies have this field
            arguments['reply_to_message'] = update["message"]["reply_to_message"]
        if not arguments['user'] in USERS:
            send_message("Aún no tienes acceso a este bot.", arguments['chat'])
            return
    else:
        return

    try:
        if arguments['text'] == "/abort":
            if arguments['chat'] in ongoing_processes.keys() and arguments['user'] in ongoing_processes[
                arguments['chat']].keys():
                ongoing_processes[arguments['chat']][arguments['user']].finish_ongoing_process()
                send_message("El proceso por pasos en curso de {} ha sido detenido.".format(
                    update["message"]["from"]["first_name"]), arguments['chat'])
            else:
                send_message(
                    "{} no tienes ningún proceso por pasos en curso.".format(update["message"]["from"]["first_name"]),
                    arguments['chat'])
        # Ongoing process
        if arguments['chat'] in ongoing_processes.keys() and arguments['user'] in ongoing_processes[
            arguments['chat']].keys():
            ongoing_processes[arguments['chat']][arguments['user']].run(arguments)
        else:
            key = arguments['text'].split(" ")[0]
            if key not in commands_with_backslash.keys():
                send_message("no te entiendo, colega", arguments['chat'])
                return
            command = commands_with_backslash[arguments['text'].split(" ")[0]](arguments)
            if command:
                command.run()

    except (ValueError, TypeError, EnvironmentError, ReferenceError) as complaint:  # Maybe names are not necessary
        print(complaint.args)
        send_message(complaint.args[0], arguments['chat'])


######################
## GENERIC COMMANDS ##
######################


## Generic comands

def command_ping(arguments):
    """
    Classic ping. Checks bot's state.
  
    :param      arguments:  The arguments
    :type       arguments:  Dictionary
    """
    send_message("Estoy vivo", arguments['chat'])


def command_echo(arguments):
    """
    Classic echo. Repeat message
    
    :param      arguments:  The arguments
    :type       arguments:  Dictionary
    """
    message = arguments['text'][5:]  # Remove "/echo " from message
    send_message(message, arguments['chat'])


def command_start(arguments):
    if arguments['chat'] in USERS:
        send_message(
            "Bienvenido al bot de ayuda de La Cima De Los Vientos. Para ver el Menú principal, usa el comando /menu",
            arguments['chat'])


def command_help(arguments):
    send_message("Emosido engañado", arguments['chat'])


#def command_add_user():


# Command dictionaries
commands_with_backslash = {
    '/ping': prueba.command_ping,
    '/echo': command_echo,
    '/start': command_start,
    '/help': command_help,
}
commands_with_backslash.update(scorer.commands_with_backslash)

commands_without_backslash = {
    'ping': prueba.command_ping,
}
