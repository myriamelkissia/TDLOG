Ce script utilise le framework SQLAlchemy pour définir des classes de modèles de données mappant des objets 
Python à des tables de base de données. Il définit des classes pour les jeux, les joueurs, les champs de bataille,
les navires et les armes. Chacune de ces classes hérite de la classe Base de SQLAlchemy, 
ce qui leur permet d'être mappées à une table de base de données. 
Les classes sont également liées entre elles grâce à des relations définies avec l'attribut relationship de SQLAlchemy.
Enfin, le script définit des méthodes permettant de mapper des objets Python vers des objets de ces classes de modèles de données, et inversement. 
Ces méthodes sont utilisées pour enregistrer et récupérer des données depuis la base de données.
