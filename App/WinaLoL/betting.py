from .wallet import add_coins, remove_coins, get_balance

# Structure pour stocker les paris en cours
active_bets = {}
currently_ingame=[]

def add_summoner_to_active_bets(summoner_name):
    # Vérifie si le joueur est déjà dans active_bets
    if summoner_name not in active_bets:
        # Initialise les données associées au joueur
        active_bets[summoner_name] = {
            'bets': [],       # Liste des paris associés à ce joueur
            'closed': False,  # Indicateur pour savoir si les paris sont fermés
            'win': [],        # Liste des gagnants
            'lose': []        # Liste des perdants
        }
        print(f"Summoner {summoner_name} ajouté dans active_bets.")
    else:
        print(f"Summoner {summoner_name} est déjà présent dans active_bets.")

# Fermer les paris pour un ami
def close_betting_for_summoner(summoner_name):
    if summoner_name in active_bets:
        active_bets[summoner_name]['closed'] = True  # Marque que les paris sont fermés pour cet ami

# Placer un pari avec vérification de la fermeture des paris
def place_bet(user_id, summoner_name, amount, choice):   
    # Vérifier si le summoner joue
    if summoner_name not in currently_ingame :
        return False, "Le joueur ne joue pas."

    # Vérifier si les paris sont déjà fermés
    if summoner_name in currently_ingame and active_bets[summoner_name].get('closed', False):
        return False, "Les paris sont fermés pour cette partie."

    # Vérifier le solde de l'utilisateur
    if get_balance(user_id) < amount:
        return False, "Solde insuffisant pour placer ce pari."

    # Retirer les coins de l'utilisateur
    remove_coins(user_id, amount)

    # Ajouter le pari à la liste des paris actifs
    if summoner_name not in active_bets:
        active_bets[summoner_name] = {'win': [], 'lose': [], 'closed': False}  # Initialiser avec "closed" à False
        print(f"Summoner {summoner_name} ajouté dans active_bets.")
    # Enregistrer le pari
    active_bets[summoner_name][choice].append({'user_id': user_id, 'amount': amount})

    return True, f"Tu as parié {amount} akhy coins sur la {'victoire' if choice == 'win' else 'défaite'} de {summoner_name}."

# Calcul des gains à la fin d'une partie
def distribute_gains(friend_name, result):
    if friend_name not in active_bets:
        return

    # Récupérer les parieurs qui ont misé sur cette partie
    bets = active_bets.pop(friend_name, None)
    if not bets:
        return

    winners = bets[result]  # Liste des gagnants (ceux qui ont parié sur le bon résultat)
    losers = bets['win' if result == 'lose' else 'lose']  # Ceux qui ont perdu

    # Répartir les gains : on multiplie la mise gagnée par 1.8
    for winner in winners:
        winnings = int(winner['amount'] * 1.8)
        add_coins(winner['user_id'], winnings)
        print(f"{winner['user_id']} a gagné {winnings} akhy coins grâce à {friend_name}.")

    return winners, losers

    # Rien à faire pour les perdants, ils ont déjà perdu leurs mises

# Fonction pour récupérer les paris fermés mais dont la partie n'est pas encore finie
def get_active_bets():
    active_bets_list = []
    
    # Parcourir les paris actifs
    for friend_name, bets_data in active_bets.items():
        if 'result' not in bets_data:  # Si le résultat n'est pas encore connu
            for bet_type in ['win', 'lose']:
                for bet in bets_data[bet_type]:
                    active_bets_list.append({
                        'friend_name': friend_name,
                        'user_id': bet['user_id'],
                        'amount': bet['amount'],
                        'bet_type': bet_type
                    })

    # Trier par montant décroissant
    sorted_bets = sorted(active_bets_list, key=lambda x: x['amount'], reverse=True)
    
    # Limiter à 30 paris
    return sorted_bets[:30]

# Ajouter une fonction pour supprimer les paris après la fin de la partie
def remove_finished_bets(friend_name):
    if friend_name in active_bets:
        del active_bets[friend_name]