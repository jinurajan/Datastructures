def mostFrequent(helpText, wordsToExclude):
    # Write your code here
    words_to_exclude = set(wordsToExclude)
    punctuations = set(['!', ' ', '#', '"', '%', '$', "'", '&', ')', '(', '*', '-', ',', '/', '.', ';', ':', '<', '?', '>', '@', '[', ']', '\\', '_', '^', '{', '}', '~'])
    search_dict = {}
    words = helpText.split(" ")
    max_count = 0
    result = []
    formatted_help_text = ''
    for char in helpText:
        try:
            int(char)
        except:
            if char in punctuations:
                formatted_help_text += ' '
            else:
                formatted_help_text += char
    words = formatted_help_text.split(" ")
    for word in words:
        if word in words_to_exclude:
            continue
        word.strip()
        if not word:
            continue
        word = word.lower()
        if word not in search_dict:
            search_dict[word] = 1
        else:
            search_dict[word] += 1
        if search_dict[word] > max_count:
            max_count = search_dict[word]
    for key, value in search_dict.items():
        if value == max_count:
            result.append(key)
    return sorted(result)


# helpText = "Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's favorite food."
# wordsToExclude = [5, 'and', 'he', 'the', 'to', 'is']
helpText = "helpabc hgf kjl yhgd wgedhjsGDSEJKS yhgd shdfasgas wgedhjsGDSEJKS abc hgf"
wordsToExclude = ['Abc', 'hgF']
print mostFrequent(helpText, wordsToExclude)
# helpText = "abc def Abc1 abC12 is are def xyz XWS XyZ XYZ4 pqr PQR pqr3 sgadh45 sgadh sgadh"
# wordsToExclude = ['def', 'is', 'are']
# print mostFrequent(helpText, wordsToExclude)
# helpText = "Revenge is a dish best served cold"
# wordsToExclude = ['Revenge', 'is', 'a', 'dish', 'best', 'served', 'cold']
# print mostFrequent(helpText, wordsToExclude)
