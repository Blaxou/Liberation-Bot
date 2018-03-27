# Liberation Bot - Prix d’Informatique 2018
### Gaëtan Schwartz

## Problématique

Depuis le début de ma scolarité au collège de Sismondi (Genève), j’ai découvert les libérations, et de temps à autre arrivait le cas où l’on venait à l’école pour un cours dont on ne savais même pas la libération, et cela était relativement frustrant. Je voulais donc créer un système permettant d’être plus facilement mis au courant des différentes libérations, en effet, les systèmes actuels permettant d'accéder aux différentes libérations étaient très peu pratiques et consistaient en un "slide-show". Voici le site du collège où sont annoncées les libérations :
https://cours.sismondi.ch/ecran-1/affichage_open.

## Résolution du problème

C'est ainsi que j'ai décider de créer *Liberation Bot*. Il permettrais de détecter les libérations quand il y en a et de nous notifier ces dernières par le biais de l'application [Telegram](http://t.me). Comment faire cela ? J'ai tout d'abord choisi Python comme language de programmation, car c'est le language avec lequel je suis le plus à l'aise. J'ai ensuite cherché une librairie facilitant l'intégration de l'API de Telegram dans Python, et j'ai opté pour [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) qui était très bien documentée. J'ai ensuite cherché une librairie me premettant d'analyser l'HTMl en ainsi extraire les différentes informations du site, notre collège ne possédant bien évidemment pas d'API publique. J'opte ici pour [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) étant la référence en extraction d'HTML dans Python et ainsi extrêmement bien documentée. J'ai ensuite enregistré mon "Bot" dans Telegram et commencé à coder.

## Résultat (Le projet en continuel développement, il risque d'évoluer)

### Utilisation

* Cloner le projet depuis ce repo
* Aller dans le dossier
* Installer les deux dépendances (`Beautiful Soup` et `pyTelegramBotAPI`)
```bash
git clone https://github.com/Blaxou/Liberation-Bot/
cd Liberation-Bot
pip install pyTelegramBotAPI
pip install bs4
python3 bot.py
```

Le programme est maintenant lancé. Nous pouvons accéder au `bot` [ici](https://t.me/Liberation_Bot). Le programme explique ensuite le reste du processus par lui-même, il suffit de suivre les instructions. Il suffit d'envoyer nos différents cours et il les enregistres, puis lorsqu'une libération est annoncée, il nous notifie.

## Sources :

* [Github de pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
* [Stack Overflow](https://stackoverflow.com/)
* [Documentation de Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Documentation de l'API de Telegram](https://core.telegram.org/bots)
