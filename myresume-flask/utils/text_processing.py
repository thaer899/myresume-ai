from fastapi import HTTPException
import spacy
from nltk.corpus import wordnet

nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    # For example, converting to lowercase and removing punctuation
    text = text.lower()
    text = text.replace("?", "")
    return text


def extract_keywords(text):
    try:
        text = preprocess_text(text)

        # Extract keywords using spaCy
        doc = nlp(text)
        keywords = []

        for token in doc:
            word = token.text
            pos = token.pos_
            synonyms = []

            # Extract synonyms using NLTK's WordNet
            if pos in ["NOUN", "VERB", "ADJ", "ADV"]:
                synsets = wordnet.synsets(word)
                for synset in synsets:
                    synonyms.extend(synset.lemma_names())

            keywords.append({
                "word": word,
                "pos": pos,
                # Remove duplicates from synonyms
                "synonyms": list(set(synonyms))
            })

        return keywords
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
