import json
import random
import os
from datetime import datetime, timedelta

def generate_random_demog(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    output = {}
    for item in data:
        if item['type'] == 'date':
            age = random.randint(16, 80)
            birth_date = datetime.now() - timedelta(days=age*365)
            output[item['key']] = birth_date.strftime("%a, %d %b %Y %H:%M:%S GMT")
        elif item['type'] == 'list':
            output[item['key']] = random.choice(item['modalities'])['value']
    
    return output

def generate_random_acheteur (file_path, nums):
    with open(file_path, 'r') as f:
        data = json.load(f)
    result = {}
    result["numbers"] = nums

    for item in data:
        key = item["key"]
        if item["type"] == "list":
            if item["mode"] == "mono":
                result[key] = random.choice(item["modalities"])["value"]
            else:
                result[key] = [modality["value"] for modality in random.sample(item["modalities"], k=random.randint(1, len(item["modalities"])))]
        elif item["type"] == "number":
            result[key] = str(random.randint(1, 1000))

    return result

def generate_random_vendeur(file_path, nums):
    with open(file_path, 'r') as f:
        data = json.load(f)
    numbers = nums
    # Sélectionner des valeurs aléatoires pour les autres clés
    duree_activite = random.choice([m['value'] for m in data[0]['modalities']])
    type_produits_services = random.sample([m['value'] for m in data[1]['modalities']], k=random.randint(1, len(data[1]['modalities'])))
    reseaux_sociaux_vendre = random.sample([m['value'] for m in data[2]['modalities']], k=random.randint(1, len(data[2]['modalities'])))
    nombre_articles_achetes_vente = str(random.randint(1, 1000))
    nombre_articles_vendus = str(random.randint(1, int(nombre_articles_achetes_vente)))
    nombre_abonnes_pages = [{reseau: str(random.randint(1, 5000))} for reseau in reseaux_sociaux_vendre]
    nombre_vues_moyen_publication = [{reseau: str(random.randint(1, int(nombre_abonnes_pages[i][reseau])))} for i, reseau in enumerate(reseaux_sociaux_vendre)]
    paiement = random.sample([m['value'] for m in data[7]['modalities']], k=random.randint(1, len(data[7]['modalities'])))
    systeme_livraison = random.choice([m['value'] for m in data[8]['modalities']])
    defis_commerce_electronique = random.sample([m['value'] for m in data[9]['modalities']], k=random.randint(1, len(data[9]['modalities'])))

    # Créer le dictionnaire de sortie
    output = {
        "numbers": numbers,
        "duree_activite": duree_activite,
        "type_produits_services": type_produits_services,
        "reseaux_sociaux_vendre": reseaux_sociaux_vendre,
        "nombre_articles_achetes_vente": nombre_articles_achetes_vente,
        "nombre_articles_vendus": nombre_articles_vendus,
        "nombre_abonnes_pages": nombre_abonnes_pages,
        "nombre_vues_moyen_publication": nombre_vues_moyen_publication,
        "paiement": paiement,
        "systeme_livraison": systeme_livraison,
        "defis_commerce_electronique": defis_commerce_electronique
    }

    return output

def generer_dict():
    prefixes = ["080", "081", "082", "083", "084", "085", "089", "090", "091", "095", "097"]
    nums = [random.choice(prefixes) + ''.join(random.choice('0123456789') for _ in range(7))]
    donnee_demographique = generate_random_demog('./demog.json')
    data = {"num" : nums[0]}
    data["donnee_demographique"] = donnee_demographique
    if ~donnee_demographique["statut"].find('vendeur') :
        data["vendeur"] = generate_random_vendeur('./vendeur.json', nums)
    if ~donnee_demographique["statut"].find('acheteur') :
        data["acheteur"] = generate_random_acheteur('./acheteur.json', nums)
    return data

def modify_numbers(directory_path, new_numbers):
    json_files = [f for f in os.listdir(directory_path) if f.endswith('.json')]
    filename = random.choice(json_files)
    filepath = os.path.join(directory_path, filename)

    with open(filepath, 'r') as f:
        data = json.load(f)

    if 'vendeur' in data and 'numbers' in data['vendeur']:
        data['vendeur']['numbers'] = new_numbers

    if 'acheteur' in data and 'numbers' in data['acheteur']:
        data['acheteur']['numbers'] = new_numbers

    return data

def generer_fichiers(n=1, repertoire="./data"):
    for _ in range(n):
        dictionnaire = generer_dict()
        numero = dictionnaire['num']
        del dictionnaire['num']
        if random.random() < 0.60:
            dictionnaire = modify_numbers('./users_data', [numero])
        chemin = os.path.join(repertoire, f"{numero}_user.json")
        with open(chemin, 'w') as f:
            json.dump(dictionnaire, f)

generer_fichiers(572)