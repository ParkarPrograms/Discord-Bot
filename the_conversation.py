import responses
import re


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response(responses.R_GREET(), ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response(responses.R_FAREWELL(), ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!. Have a good day', ['thank', 'thanks'], single_response=True)
    response('I love you too.', ['i', 'love', 'bot', 'you'], required_words=['love', 'bot'])
    response(responses.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(responses.R_EATING, ['what', 'you', 'have', 'eat', 'lunch', 'dinner'], required_words=['you', 'eat'])
    response("The weather is always clear where I live", ['how', 'is','the','weather'],required_words=['weather'])
    response(responses.Bot(), ['who','are','you','what'],required_words=['you'])
    response(responses.R_DAY, ['how', 'was', 'your', 'day'], required_words=['day'])
    response(responses.R_JOKE(), ['tell', 'joke', 'laugh', ], required_words=['joke'])
    response("I am not on any social media", ["insta", "instagram", "linkedin", "twitter"])
    response("The name's Steve. Bot Steve",["what","is","your","name"], required_words= ["name"])
    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return responses.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


