from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F


MODEL_NAME = "cointegrated/rubert-tiny2-cedr-emotion-detection"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# Метки классов, можно адаптировать под твои нужды
labels = ['нейтральный', 'радость', 'печаль', 'гнев', 'страх', 'удивление']


def predict_sentiment(text: str) -> str:
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = F.softmax(logits, dim=-1)
        predicted_class = torch.argmax(probs, dim=1).item()
        return labels[predicted_class]
