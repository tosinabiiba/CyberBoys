# Define a list of rules
rules = [
    {'pattern': 'hi', 'response': 'Hello!'},
    {'pattern': 'how are you', 'response': 'I am doing well, thank you.'},
    {'pattern': 'what is your name', 'response': 'My name is AI.'},
    {'pattern': 'what is the weather like today', 'response': 'I am not sure, you can check a weather app or website for that information.'},
    {'pattern': 'do you like ice cream', 'response': 'I am an AI and do not have personal preferences.'}
]

# Define a function to find the first rule that matches the user input
def find_matching_rule(input_text):
    for rule in rules:
        if rule['pattern'] in input_text:
            return rule['response']
    return 'Sorry, I do not understand what you are saying.'

# Main loop
while True:
    # Get user input
    input_text = input('> ')

    # Find the first matching rule
    response = find_matching_rule(input_text)

    # Print the response
    print(response)
