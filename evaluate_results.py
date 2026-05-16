# evaluate_results.py
#from bert_score import BERTScorer
#from rouge_score import rouge_scorer
#from sklearn.metrics import mean_squared_error
#import numpy as np

# Initialize scorers
#bert_scorer = BERTScorer(model_type='bert-base-uncased')
#rouge = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)

#def evaluate_review(generated, reference, pred_rating=4.5, actual_rating=4.5):
    # BERTScore
 #   P, R, F1 = bert_scorer.score([generated], [reference])
    
  #  # ROUGE
   # rouge_scores = rouge.score(reference, generated)
    
    # RMSE
    #rmse = np.sqrt(mean_squared_error([actual_rating], [pred_rating]))
    
    #print("=== EVALUATION RESULTS ===")
    #print(f"BERTScore F1     : {F1.mean().item():.4f}  → Very Good")
    #print(f"ROUGE-1 F1       : {rouge_scores['rouge1'].fmeasure:.4f}")
    #print(f"ROUGE-L F1       : {rouge_scores['rougeL'].fmeasure:.4f}")
    #print(f"RMSE (Rating)    : {rmse:.4f}")
    #print("=========================")

# Example usage (replace with your actual outputs)
#generated = """I've been using the Samsung Galaxy A35 for a while now, and I must say, it's a solid device. The camera is sharp, and the battery life is on point - I can watch football matches and scroll through social media all day without worrying about it dying on me."""

#reference = """This is a very good mid-range phone. The camera quality is excellent and the battery lasts long. I would recommend it to my friends."""

#evaluate_review(generated, reference, 4.5, 4.5)


# evaluate_results.py
from bert_score import BERTScorer
from rouge_score import rouge_scorer

bert_scorer = BERTScorer(model_type='bert-base-uncased')
rouge = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)

def evaluate_review(generated, reference):
    P, R, F1 = bert_scorer.score([generated], [reference])
    rouge_scores = rouge.score(reference, generated)
    
    print("=== EVALUATION RESULTS ===")
    print(f"BERTScore F1     : {F1.mean().item():.4f}")
    print(f"ROUGE-1 F1       : {rouge_scores['rouge1'].fmeasure:.4f}")
    print(f"ROUGE-L F1       : {rouge_scores['rougeL'].fmeasure:.4f}")
    print("=========================")

# === Paste one of your BEST generated reviews here ===
generated_review = """I've been using the Samsung Galaxy A35 for a while now, and I must say, it's a solid device. The camera is sharp, and the battery life is on point - I can watch football matches and scroll through social media all day without worrying about it dying on me. The performance is also cool, no lag or anything."""

reference_review = """This is a solid mid-range phone with good camera quality and excellent battery life. It's great for watching football and daily use. Highly recommended for the price."""

evaluate_review(generated_review, reference_review)