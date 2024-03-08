import nltk
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction
from rouge import Rouge
import nltk
from nltk.translate.meteor_score import meteor_score
from nltk.tokenize import word_tokenize

def calculate_meteor(reference_texts, candidate_text):
    tokenized_candidate = word_tokenize(candidate_text)
    tokenized_references = [word_tokenize(ref) for ref in reference_texts]
    scores = [meteor_score([ref], tokenized_candidate) for ref in tokenized_references]
    return max(scores)
def calculate_rouge_scores(hypothesis, reference):
    rouge = Rouge()
    scores = rouge.get_scores(hypothesis, reference)
    return scores
def calculate_bleu(reference_texts, candidate_text, n):
    references = [nltk.word_tokenize(ref) for ref in reference_texts]
    candidate = nltk.word_tokenize(candidate_text)
    weights = [1.0/n] * n + [0.0] * (4-n)
    smoothing_function = SmoothingFunction().method1
    score = sentence_bleu(references, candidate, weights=weights, smoothing_function=smoothing_function)
    return score

a = "reference_text_here"
reference_texts = [a]
candidate_text = "candidate_text_here"

scores = calculate_rouge_scores(candidate_text, a)
score = calculate_meteor(reference_texts, candidate_text)


print(f"BLEU-1: {calculate_bleu(reference_texts, candidate_text, 1)}")
print(f"BLEU-2: {calculate_bleu(reference_texts, candidate_text, 2)}")
print(scores)
print(f"METEOR Score: {score}")


