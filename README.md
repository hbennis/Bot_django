# Bot_django
Framework Django utilisé en suivant les guidelines du cours d'OpenClassroom. Le code a été divisé en app pour distinguer les différentes
fonctionnalités.

Utilisation:
1. Terminal: $python manage.py runserver
2. Entrer l'url: http://localhost:8000/user/index
3. Connexion: username: hba
              password: hba


Structure du code:
  1. Bot_django: App 'mère' qui redirige les urls vers les bonnes apps: voir Bot_django.urls.py
  2. bot: contient la page d'accueil pour choisir le thème de la discussion ainsi que la page de dialogue avec le bot (suivant le thème).
    Quelques fichiers importants:
      - templates: contient les deux templates nécessaires (accueil et discussion), qui font appel à l'emplacement 'static' pour 
        l'utilisation de Bootstrap notamment. 
      - models: permet de créer une base de données pour stocker les réponses du Bot et du user. 
      - views: vue d'affichage de la page d'accueil ainsi que la vue d'affichage de la discussion avec le bot. Cette dernière repose
        sur un formulaire et sur l'appel à la base de données pour avoir l'affichage des réponses du bot et de l'utilisateur.
      - urls: permet à chaque vue d'être associée à une url. 
      - forms: contient le formulaire utilisée pour la vue de discussion
  3. user: permet de gérer l'authentification de l'utilisateur pour l'accès à la page d'accueil. Utilise certains outils 
    d'authentification intégrés dans Django
  4. EcpBtBot: permet de gérer la connexion à l'API de Dialogflow à l'aide de apiai. 
      - API: Pour chaque agent conversationnel dans DialogFlow, un token a été défini. Chaque classe contruite correspond à un thème de
        discussion. L'appel à la classe permet de créer une connexion avec l'agent. La méthode get_json_response(user_message)
        permet de retourner le document json en réponse au message 'user_message'.
      - MainClass: permet de retourner la réponse à un message et de créer une connexion avec le bon agent. Une variable 
        globale dico_users permet d'avoir un dictionnaire contenant les id des utilisateurs connectés (pour avoir une seule session 
        par utilisateur) et les thèmes déjà choisis (pour pouvoir basculer de thème) 
