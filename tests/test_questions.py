import pytest
from selenium import webdriver
from page_objects.main_page import MainPage

# Предположим, что у нас 3 вопроса
questions = [
    {"question": "Как заказать самокат?", "answer": "Чтобы заказать самокат, нажмите на кнопку Заказать..."},
    {"question": "Когда привезут самокат?", "answer": "Самокат будет доставлен в течение 24 часов..."},
    {"question": "Как отменить заказ?", "answer": "Чтобы отменить заказ, обратитесь к нашей службе поддержки..."},
]


@pytest.mark.parametrize("question_data", questions)
def test_faq_questions(question_data):
    driver = webdriver.Chrome()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    main_page = MainPage(driver)

    # Находим индекс вопроса
    question_index = questions.index(question_data)

    # Нажимаем на соответствующий вопрос
    main_page.click_faq_question(question_index)

    # Находим текст ответа
    answer_text = main_page.get_faq_answer_text(question_index)

    # Проверяем, что ответ соответствует ожидаемому
    assert answer_text == question_data['answer'], f"Expected: {question_data['answer']}, but got: {answer_text}"

    driver.quit()