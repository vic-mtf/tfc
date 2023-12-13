#Déclaration des variables
montant_total_general = 0
montant_total = None
frais_inscription = 100
frais_examen = 50
frais_cours = 200
frais_transport = 50

# Fonction pour calculer le montant total des frais académiques
calculer_frais = lambda frais_inscription, frais_examen, frais_cours, frais_transport : frais_inscription + frais_examen + frais_cours + frais_transport

# Demander à l'utilisateur le nombre d'étudiants à inscrire
nombre_etudiants = int(input("Combien d'étudiants souhaitez-vous inscrire ? "))

# Boucle pour demander les informations pour chaque étudiant et calculer le montant total des frais
for i in range(nombre_etudiants):
    # Demander le nom de l'étudiant
    nom = input("Entrez le nom de l'étudiant : ")
    # Demander le prénom de l'étudiant
    prenom = input("Entrez le prénom de l'étudiant : ")
    # Demander le niveau d'études de l'étudiant
    niveau = input("Entrez le niveau d'études de l'étudiant : ")
    # Calculer le montant total des frais pour cet étudiant
    montant_total = calculer_frais(frais_inscription, frais_examen, frais_cours, frais_transport)
    montant_total_general += montant_total
    # Afficher le montant total des frais pour cet étudiant
    print("Le montant total des frais pour", prenom, nom, "en", niveau, "est de", montant_total, "USD.")

# Afficher le montant total des frais pour tous les étudiants
print("Le montant total des frais pour tous les étudiants est de", montant_total_general, "USD.")