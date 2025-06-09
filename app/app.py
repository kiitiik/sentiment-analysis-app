import streamlit as st
from sentiment import predict_sentiment
import re
import torch
import types

# Фикс бага с torch.classes
torch.classes.__path__ = types.SimpleNamespace(_path=[])


# 1. Цветовая схема для эмоций
COLOR_MAP = {
    "радость": "lightgreen",
    "печаль": "lightblue",
    "гнев": "tomato",
    "страх": "plum",
    "удивление": "gold",
    "нейтральный": "lightgray",
}


# ───────────────────────────────────
# 2. Вспомогательные функции
def split_sentences(text: str) -> list[str]:
    """Грубое разбиение по . ! ? — хватает для демонстрации."""
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]


def highlight_html(text: str) -> str:
    """Возвращает HTML-строку с окрашенными предложениями и меткой эмоции."""
    parts = []
    for sent in split_sentences(text):
        label = predict_sentiment(sent)
        color = COLOR_MAP.get(label, "#ffffff")
        parts.append(
            f"<span style='background:{color}; padding:4px 6px; border-radius:4px; "
            f"margin:2px; display:inline-block'>{sent} [{label}]</span>"
        )
    return " ".join(parts)


# ───────────────────────────────────
# 3. Streamlit-интерфейс
st.set_page_config(page_title="Анализ тональности", layout="centered")
st.title("🎨 Подсветка эмоций в тексте")

uploaded = st.file_uploader("⬆ Загрузите .txt-файл", type=["txt"])
manual_text = st.text_area("…или введите текст ниже:", height=180)

# выбираем, откуда взять текст
text = None
if uploaded is not None:
    text = uploaded.read().decode("utf-8")
    st.subheader("📄 Текст из файла")
    st.write(text)
elif manual_text.strip():
    text = manual_text
    st.subheader("📝 Введённый текст")
    st.write(text)

# кнопка «Анализировать»
if st.button("Анализировать"):
    if not text:
        st.warning("Сначала загрузите файл или введите текст.")
    else:
        st.subheader("🔍 Результат с подсветкой")
        st.markdown(highlight_html(text), unsafe_allow_html=True)
