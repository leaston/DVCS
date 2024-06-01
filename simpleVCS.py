
""" Ce bloc importe deux modules standard de Python :

os : Ce module permet d'interagir avec le système d'exploitation, notamment pour la gestion des répertoires et des fichiers.
hashlib : Ce module fournit des algorithmes de hachage sécurisés pour créer des hash cryptographiques (comme SHA-1). """
import os
import hashlib

""" Le bloc suivant  définit une classe appelée SimpleVCS, représentant un système de contrôle de version simplifié.

Méthode __init__
    1. Paramètre repo_dir : Le répertoire du dépôt où seront stockées les données de version.
    2. Attribut self.repo_dir : Stocke le chemin du répertoire du dépôt.
    3. Attribut self.objects_dir : Détermine le chemin du sous-répertoire objects où les objets (commits) seront stockés.
    4. Création du répertoire objects : Utilise os.makedirs pour créer le répertoire objects s'il n'existe pas déjà. """

class SimpleVCS:
    def __init__(self, repo_dir):
        self.repo_dir = repo_dir
        self.objects_dir = os.path.join(repo_dir, 'objects')
        os.makedirs(self.objects_dir, exist_ok=True)

    """ 
    La méthode suivante calcule le hash SHA-1 des données fournies.

        1. Paramètre data : Les données à hacher.
        2. Création de l'objet SHA-1 : hashlib.sha1() crée un nouvel objet SHA-1.
        3. Mise à jour avec les données : sha1.update(data) met à jour l'objet SHA-1 avec les données.
        4. Retourne le hash : sha1.hexdigest() retourne le hash sous forme de chaîne hexadécimale. """

    def hash_object(self, data):
        sha1 = hashlib.sha1()
        sha1.update(data)
        return sha1.hexdigest()
    
    """ 
    La méthode suivante écrit les données dans un fichier après avoir calculé leur hash.
        1. Calcule le hash : obj_hash = self.hash_object(data) calcule le hash des données.
        2. Détermine le chemin du fichier : obj_path = os.path.join(self.objects_dir, obj_hash) crée le chemin complet pour le fichier basé sur le hash.
        3. Écrit les données dans le fichier : with open(obj_path, 'wb') as f: f.write(data) ouvre le fichier en mode binaire pour écriture et y écrit les données.
        4. Retourne le hash : return obj_hash retourne le hash des données. """

    def write_object(self, data):
        obj_hash = self.hash_object(data)
        obj_path = os.path.join(self.objects_dir, obj_hash)
        with open(obj_path, 'wb') as f:
            f.write(data)
        return obj_hash
    
    """ 
    La dernière méthode crée un commit en enregistrant le message de commit.
        1. Encode le message : commit_data = message.encode('utf-8') convertit le message en bytes.
        2. Écrit le commit : commit_hash = self.write_object(commit_data) écrit les données du commit dans un fichier et obtient le hash du commit.
        3. Affiche le hash du commit : print(f'Committed with hash {commit_hash}') affiche le hash du commit nouvellement créé. """

    def commit(self, message):
        commit_data = message.encode('utf-8')
        commit_hash = self.write_object(commit_data)
        print(f'Committed with hash {commit_hash}')

""" Ce dernier bloc montre comment utiliser la classe SimpleVCS.
        1. Instancie un objet SimpleVCS : vcs = SimpleVCS('.my_vcs') crée un nouvel objet SimpleVCS avec le répertoire .my_vcs comme répertoire du dépôt.
        2. Fait un commit : vcs.commit('Initial commit') crée un commit avec le message 'Initial commit'. """

# Utilisation
vcs = SimpleVCS('.my_vcs')
vcs.commit('Initial commit')
