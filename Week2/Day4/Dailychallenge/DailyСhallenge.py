import string
import re
import sys
import os
from collections import Counter

STOP_WORDS = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
    'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
    'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
    'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
    'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
    'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
    'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
    'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
    'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
    'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
    'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'
}

class Text:
    def __init__(self, text):
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")
        self.text = text
        self._cleaned_words = self._get_cleaned_words()

    def _get_cleaned_words(self):
        translator = str.maketrans('', '', string.punctuation)
        clean_text = self.text.translate(translator).lower()
        return clean_text.split()

    def word_frequency(self, word):
        target_word = word.lower()
        count = self._cleaned_words.count(target_word)
        
        if count == 0:
            return None
        return count

    def most_common_word(self):
        if not self._cleaned_words:
            return "No words found in text."
            
        word_counts = Counter(self._cleaned_words)
        most_common = word_counts.most_common(1)
        
        if most_common:
            return most_common[0][0]
        return "Could not determine the most common word."

    def unique_words(self):
        unique_set = set(self._cleaned_words)
        return list(unique_set)

    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                return cls(content)
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File not found at path: {file_path}")
        except Exception as e:
            raise IOError(f"Error reading file: {e}")

class TextModification(Text):
    
    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        return self.text.translate(translator)

    def remove_stop_words(self):
        no_punc_text = self.remove_punctuation()
        words = no_punc_text.lower().split()
        
        filtered_words = [word for word in words if word not in STOP_WORDS]
        
        return ' '.join(filtered_words)

    def remove_special_characters(self):
        return re.sub(r'[^a-zA-Z0-9\s]', '', self.text)


if __name__ == "__main__":
    
    print("\n==================================")
    print("DEMO I: Text Analysis from String")
    print("==================================")
    
    sample_text = "The quick brown fox jumps over the lazy dog. The fox is quick and brown."
    text_analyst = Text(sample_text)
    
    print(f"Original Text: {sample_text}")
    print(f"Frequency of 'the': {text_analyst.word_frequency('the')}")
    print(f"Frequency of 'fox': {text_analyst.word_frequency('fox')}")
    print(f"Most Common Word: {text_analyst.most_common_word()}")
    print(f"Unique Words Count: {len(text_analyst.unique_words())}")
    
    print("\n==================================")
    print("DEMO II: Text Modification")
    print("==================================")

    modification_text = "Hello, world! This is a test string 123. It's meant to show cleaning methods."
    text_modifier = TextModification(modification_text)
    print(f"Original Text: {modification_text}")

    cleaned_punc = text_modifier.remove_punctuation()
    print(f"\n[PUNCTUATION REMOVED]: {cleaned_punc}")

    cleaned_stops = TextModification(cleaned_punc).remove_stop_words()
    print(f"[STOP WORDS REMOVED]: {cleaned_stops}")

    special_char_text = "This text has #special! @characters$ to test the cleaner."
    text_modifier_sc = TextModification(special_char_text)
    cleaned_special = text_modifier_sc.remove_special_characters()
    print(f"\nOriginal Special Char Text: {special_char_text}")
    print(f"[SPECIAL CHARS REMOVED]: {cleaned_special}")
