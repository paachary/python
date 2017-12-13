from nltk.tokenize import sent_tokenize, word_tokenize

example_text = """
                hello Mr. Prashant, how are you doing today?
                The weather is great and Python is awesome.
                Please dont eat what you generally eat, but eat everything.
                """

print(sent_tokenize(example_text))

print(word_tokenize(example_text))
