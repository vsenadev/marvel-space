class CharacterUtils:
    def battle(self, player1, player2):
        result = []
        attributes = ['affiliations', 'abilities_and_powers', 'strength', 'speed', 'durability', 'agility',
                      'combat_experience', 'recovery', 'intelligence', 'equipment']

        for attr in attributes:
            p1_value = int(player1[attr])
            p2_value = int(player2[attr])

            if p1_value > p2_value:
                result.append(player1['name'])
            elif p2_value > p1_value:
                result.append(player2['name'])

        player1_Occurrences = result.count(player1['name'])
        player2_Occurrences = result.count(player2['name'])

        if player1_Occurrences > player2_Occurrences:
            return "{0} Win".format(player1['name'])
        else:
            return "{0} Win".format(player2['name'])

