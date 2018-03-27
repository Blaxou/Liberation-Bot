
# IMPORTS

import json
import re
import threading

from utils.database import Database
from utils.logging import Logger
from Parsers.sismondi import Parser
from telebot import TeleBot, types

# INITIATE ALL CLASSES

logger = Logger('test.log')
bot = TeleBot("469704664:AAGRVbPOd_0nfRLbb0-1dNYBv_G7fPoq1CM")
mydb = Database('db.json')
parser = Parser()

# REGISTER COMMANDS


@bot.message_handler(commands=['admin'])
def c_admin(message):
    if str(message.from_user.id) in mydb.read()['users']:
        bot.reply_to(message, "Vous êtes admin :D")
    else:
        bot.reply_to(message, "Vous n'êtes pas administrateur ! ")


@bot.message_handler(commands=['start', 'menu'])
def c_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('/1 Ajouter un cours')
    itembtn2 = types.KeyboardButton('/2 Liste tous les cours enregistrés')
    itembtn3 = types.KeyboardButton('/3 Reset tout les cours')
    itembtn4 = types.KeyboardButton('/4 Afficher les libérations')
    itembtn5 = types.KeyboardButton('/5 Help')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    bot.reply_to(message, """
Bienvenue !

Ce bot permets de t’envoyer une notif quand t’es libéré dans un cours à Sismondi.""", reply_markup=markup)
    mydb.register_user(message.from_user.id)


@bot.message_handler(commands=['1'])
def c_add_cours(message):
    text = """
Pour ajouer un cours, envoie le nom complet du cours.
Il sera automatiquement ajouté !

Pour supprimer le cours, renvoie le même cours.
	"""
    bot.reply_to(message, text)


@bot.message_handler(commands=['2'])
def c_list_cours(message):
    lessons = mydb.get_user_data(message.from_user.id)['lessons']
    if lessons != []:
        text = 'Cours enregistrés :\n\n • '
        text += '\n • '.join(lessons)
        text += '\n\n'
    else:
        text = "Vous n’avez enregistré aucun cours !"
    bot.reply_to(message, text)


@bot.message_handler(commands=['3'])
def c_reset_cours(message):
    reg_user(message.from_user.id)
    bot.reply_to(message, "✅ Tous tes cours ont été reinitialisés !")


@bot.message_handler(commands=['4'])
def c_show_librs(message):
    global parser
    if len(parser.librs) > 0:
        text = ''
        for l in parser.librs:
            text += '\n • ' + l['text']
    else:
        text = "Il n'y a pas de libérations 😞"
    bot.reply_to(message, text)


@bot.message_handler(commands=['help', '5'])
def c_help(message):
    text = '''
Commandes :

	• /menu
	• /help'''
    bot.reply_to(message, text)


@bot.message_handler(regexp=parser.lesson_regexp)
def test_if_lesson(message):
    ud = mydb.get_user_data(message.from_user.id)
    if not message.text in ud['lessons']:
        bot.reply_to(message, '✅ Ajouté')
        mydb.add_lesson(message.from_user.id, message.text)
    else:
        bot.reply_to(message, '❌ Supprimé')
        mydb.remove_lesson(message.from_user.id, message.text)
    c_list_cours(message)


@bot.message_handler(func=lambda msg: True)
def not_a_cours(message):
    bot.reply_to(message, '⚠️ Cela ne semble pas être un cours !')


def check_for_liberations():
    global parser, interval
    reg = re.compile(parser.lesson_regexp)
    logger.info('Checking for liberations ...')
    last_librs = parser.librs
    parser.check()
    if last_librs != parser.librs:
        logger.info('Sending notifs ...')
        db = mydb.read()
        for userID in db['users']:
            for lesson in db['users'][userID]['lessons']:
                for libr in parser.librs:
                    if libr['groups'][:5] == reg.match(cours).groups()[:5]:
                        bot.send_message(int(userID), 'Vous êtes libéré le ' +
                                         libr['header'] + ' en ' + libr['text'])
    else:
        logger.info('No need to send notif, no change.')

    try :
        threading.Timer(interval, check_for_liberations, ()).start()
    except Exception as e :
        logger.critical(e)
        exit(1)




logger.info('Bot launched !')

bot.polling()

parser.check()

interval = 60

check_for_liberations()
