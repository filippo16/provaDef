import json


def createJsonData(df, name_path):
    json_list = []

    for index, row in df.iterrows():
        player_stats = {
            'r': row['R'],
            'nome': row['Nome'],
            'squadra': row['Squadra'],
            'pv': row['Pv'],
            'mv': row['Mv'],
            'fm': row['Fm'],
            'gf': row['Gf'],
            'gs': row['Gs'],
            # 'Rp': row['Rp'],
            # 'Amm': row['Amm'],
            # 'Esp': row['Esp'],
            # 'Au': row['Au']
        }
        json_list.append(player_stats)

    with open(f'{name_path}.json', 'w') as file:
        json.dump(json_list, file, indent=1)

    print(f"File '{name_path}.json' creato con successo.")
