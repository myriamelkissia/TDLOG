Ce script Python utilise le framework FastAPI pour mettre en place une API RESTful. L'API expose plusieurs routes, 
chacune correspondant à une fonctionnalité du jeu de bataille navale.

La classe GameService contient les fonctionnalités du jeu, comme la création et la récupération d'un jeu, 
l'ajout de joueurs et de navires, ou encore le tir d'un navire sur un autre.

Les routes de l'API sont définies avec des décorateurs @app.route(). Chaque route prend en entrée des données sous forme de modèles Pydantic,
qui permettent de valider et de caster automatiquement les données reçues.

Les routes permettent de créer un nouveau jeu, de récupérer un jeu existant, d'ajouter un joueur à un jeu,
d'ajouter un navire à un jeu, de tirer sur un navire dans un jeu, et de récupérer le statut d'un jeu pour un joueur donné.

La route "/create-game" permet de créer un nouveau jeu en prenant en entrée le nom du joueur et les dimensions du terrain de jeu.
Elle retourne l'identifiant du jeu créé.

La route "/get-game" permet de récupérer un jeu existant en prenant en entrée l'identifiant du jeu.
Elle retourne le jeu correspondant.

La route "/join-game" permet à un joueur de rejoindre un jeu existant en prenant en entrée l'identifiant du jeu et le nom du joueur. 
Elle retourne un booléen indiquant si l'ajout du joueur au jeu a réussi ou non.

La route "/add-vessel" permet d'ajouter un navire à un jeu en prenant en entrée l'identifiant du jeu, le nom du joueur, le type de navire et les coordonnées où le navire doit être placé. Elle retourne un booléen indiquant si l'ajout a été réussi ou non.

La route "/shoot-at" permet de tirer sur un navire dans un jeu en prenant en entrée l'identifiant du jeu, le nom du tireur,
l'identifiant du navire visé et les coordonnées du tir. Elle retourne un booléen indiquant si le tir a été réussi ou non.

La route "/game-status" permet de récupérer le statut d'un jeu pour un joueur donné en prenant en entrée l'identifiant du jeu et le nom du joueur. 
Elle retourne une chaîne de caractères indiquant le statut du jeu.

L'application utilise également le framework Uvicorn pour être lancée sur un serveur.
Enfin, l'application gère les exceptions en retournant une réponse JSON avec un code d'erreur et un message d'erreur en cas d'exception levée.
