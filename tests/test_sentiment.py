from app.sentiment import predict_sentiment


def test_sentiment_on_russian_text():
    assert predict_sentiment("Это отлично!") in ["радость"]
    assert predict_sentiment("Мне грустно и плохо.") in ["печаль", "гнев"]
    assert predict_sentiment("Просто обычный день.") in ["нейтральный"]
