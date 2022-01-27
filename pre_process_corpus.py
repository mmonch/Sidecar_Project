# preprocess and normalize Text

# in case text not english
def remove_accented_chars(text):
  text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
  return text

# preprocessing
def pre_process_corpus(docs):
  norm_docs = []
  for string in tqdm.tqdm(docs):
    string = string.replace("_", " ")
    string = string.translate(string.maketrans("\n\t\r", "   "))
    string = remove_accented_chars(string)
    # insert space where an uppercase letter follows a lowercase letter
    string = re.sub(r'(?<![A-Z\W])(?=[A-Z])', ' ', string)
    string = contractions.fix(string)
    # remove special characters or whitespaces
    string = re.sub(r"[^a-zA-Z0-9\s]", "", string, flags=re.I|re.A)
    string = string.lower()
    string = string.strip()
    norm_docs.append(string)
  return norm_docs