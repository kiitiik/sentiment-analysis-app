from app.sentiment import predict_sentiment

def test_positive_emotion():
    assert predict_sentiment("Я так рад, что всё получилось!") in ["радость"]

def test_negative_emotion():
    assert predict_sentiment("Мне очень плохо. Хочется плакать.") in ["печаль", "гнев"]

def test_neutral_emotion():
    assert predict_sentiment("Сегодня я ходил в магазин.") in ["нейтральный"]

def test_empty_input():
    try:
        result = predict_sentiment("")
        assert isinstance(result, str) and result in ['нейтральный', 'радость', 'печаль', 'гнев', 'страх', 'удивление']
    except Exception:
        assert False, "Ошибка при обработке пустой строки"

def test_long_input():
    long_text = "Я не знаю, что происходит. " * 100
    result = predict_sentiment(long_text)
    assert isinstance(result, str)

def test_weird_characters():
    result = predict_sentiment("Что это?! 🤔😠🔥")
    assert isinstance(result, str)

def test_english_input():
    result = predict_sentiment("I am happy today")
    assert isinstance(result, str)
