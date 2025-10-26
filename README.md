# Sprint_6
locators/ - Локаторы элементов
- base_locators.py - куки и логотипы
- main_locators.py - кнопки и FAQ на главной
- order_first_page_locators.py - форма заказа (имя, адрес, метро)
- order_second_page_locators.py - дата, срок аренды, цвет самоката
- order_modals_locators.py - всплывающие окна подтверждения

pages/ - Действия со страницами
- base_page.py - общие методы (клик, ввод, скролл)
- main_page.py - работа с главной страницей
- order_page.py - заполнение форм заказа

test_data/ - Данные для тестов
- order_data.py - 2 набора данных клиентов

tests/ - Тесты
- test_important_questions.py - проверка вопросов в FAQ
- test_order_scooter.py - полный флоу заказа самоката

Остальные файлы
- config.py - настройки (URL)
- conftest.py - настройка браузера
- .gitignore - что не коммитить