Ce script définit une classe GameService qui fournit des services liés aux jeux de combat navals.
La classe possède une méthode create_game qui permet de créer un nouveau jeu de combat naval en ajoutant un joueur au jeu
et en créant un champ de bataille pour ce joueur. La classe possède également une méthode join_game qui permet à un joueur
de rejoindre un jeu existant en ajoutant ce joueur au jeu.

Il y a également une méthode get_game qui permet de récupérer un jeu en utilisant l'identifiant du jeu.
La classe possède une méthode add_vessel qui permet à un joueur de ajouter un navire à son champ de bataille.
La classe possède également une méthode shoot_at qui permet à un joueur de tirer sur un navire ennemi en utilisant un navire de son propre champ de bataille.

Enfin, il y a une méthode get_game_status qui permet de récupérer l'état actuel du jeu en vérifiant si un joueur a perdu ou gagné.
La classe utilise une instance de la classe GameDao pour accéder à la base de données et enregistrer et récupérer des données.
