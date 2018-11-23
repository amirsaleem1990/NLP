from collections import Counter
text = '''The Sri Lanka T20 squad were surrounded by 'extraordinary' security arrangements upon 
their arrival in Lahore on Sunday morning, for the third T20I at the Gaddafi Stadium. This is the first 
Sri Lanka team to visit Pakistan since the terror attack targeting Sri Lanka's team bus in Lahore in 2009.
The side, which flew in from Abu Dhabi, was escorted to the team hotel in a bomb-proof bus. The routes from 
the Allama Iqbal Airport in Lahore were virtually sealed off with thousands of armed police deployed along 
the 14 km route. The streets leading to Mall Road were also deserted as the team was flanked by a large 
convoy of police commandos. The arrangements were similar to the security protocol followed for a presidential 
visit.'''
tokens = word_tokenize(text)
token_count = Counter(tokens)
# Counter({'the': 9, 'in': 6, '.': 6, 'The': 5, 'were': 4, 'team': 4, 'to': 4, 'Sri': 3, 'Lanka': 3, 'Lahore': 3, ',': 3, 'a': 3, 'by': 2, 'security': 2, 'arrangements': 2, 'for': 2, 'visit': 2, 'bus': 2, 'from': 2, 'was': 2, 'of': 2, 'police': 2, 'T20': 1, 'squad': 1, 'surrounded': 1, "'extraordinary": 1, "'": 1, 'upon': 1, 'their': 1, 'arrival': 1, 'on': 1, 'Sunday': 1, 'morning': 1, 'third': 1, 'T20I': 1, 'at': 1, 'Gaddafi': 1, 'Stadium': 1, 'This': 1, 'is': 1, 'first': 1, 'Pakistan': 1, 'since': 1, 'terror': 1, 'attack': 1, 'targeting': 1, "'s": 1, '2009': 1, 'side': 1, 'which': 1, 'flew': 1, 'Abu': 1, 'Dhabi': 1, 'escorted': 1, 'hotel': 1, 'bomb-proof': 1, 'routes': 1, 'Allama': 1, 'Iqbal': 1, 'Airport': 1, 'virtually': 1, 'sealed': 1, 'off': 1, 'with': 1, 'thousands': 1, 'armed': 1, 'deployed': 1, 'along': 1, '14': 1, 'km': 1, 'route': 1, 'streets': 1, 'leading': 1, 'Mall': 1, 'Road': 1, 'also': 1, 'deserted': 1, 'as': 1, 'flanked': 1, 'large': 1, 'convoy': 1, 'commandos': 1, 'similar': 1, 'protocol': 1, 'followed': 1, 'presidential': 1})

# Print the 10 most common words
print(token_count.most_common(10))
# [('team', 4), ('sri', 3), ('lanka', 3), ('lahore', 3), ('security', 2), ('arrangement', 2), ('visit', 2), ('bus', 2), ('route', 2), ('police', 2)]
