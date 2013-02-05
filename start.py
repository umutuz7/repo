import facebook

token = 'AAACEdEose0cBAMXL9dfczAfk59kRpABCrIefbYB903LMAEEWRDN6pB3TzWhZAre6R6sqs7gmvTfEMc5noyPRf5N5dRRCtlV2Lbma7LwZDZD'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")

friend_list = [friend['name'] for friend in friends['data']]

print friend_list
