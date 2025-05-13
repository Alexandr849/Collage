import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(width=1000, height=1200)
dpg.setup_dearpygui()

image_path = "C:/logotype.png"
width, height, channels, data = dpg.load_image(image_path)

with dpg.texture_registry(show=False):
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

with dpg.font_registry():
    with dpg.font("C:/Windows/Fonts/times.ttf", 20) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

with dpg.window(label="Заявление", width=1000, height=1200, no_move=True, no_resize=True):
    dpg.bind_font(default_font)

    with dpg.group(horizontal=True):
        dpg.add_image("texture_tag", width=width / 2, height=height / 2)
        with dpg.group():
            dpg.add_text("Директору  КГБПОУ\n«Красноярский колледж отраслевых\nтехнологий и предпринимательства»\nН.В. Журовой")
            dpg.add_input_text(label="ФИО", width=300)

            dpg.add_text("Паспорт")
            with dpg.group(horizontal=True):
                dpg.add_input_text(label="Серия", width=100)
                dpg.add_input_text(label="Номер", width=120)
            dpg.add_input_text(label="Кем и когда выдан", width=300)
            dpg.add_input_text(label="Проживающий по адресу", width=300)
            dpg.add_input_text(label="Телефон", width=200)

            dpg.add_separator()
            dpg.add_text("ЗАЯВЛЕНИЕ")
            dpg.add_input_text(label="ФИО, дата и место рождения", width=400)
            dpg.add_input_text(label="Код и наименование специальности", width=400)

            dpg.add_input_text(label="Дата подачи заявления", width=200)
            dpg.add_input_text(label="Подпись", width=200)

            dpg.add_checkbox(label="Очная форма обучения")
            dpg.add_checkbox(label="Заочная форма обучения")
            dpg.add_checkbox(label="За счет бюджета")
            dpg.add_checkbox(label="Платная форма")

            dpg.add_input_text(label="Возврат документов (лично/по почте)", width=400)

            dpg.add_input_text(label="Окончил(а) в (год)", width=150)
            dpg.add_input_text(label="Наименование учреждения", width=400)
            dpg.add_combo(label="Тип учреждения", items=["Общеобразовательное", "СПО", "Другое"], width=300)

            with dpg.group(horizontal=True):
                dpg.add_input_text(label="Серия аттестата", width=100)
                dpg.add_input_text(label="Номер", width=180)
            dpg.add_input_text(label="Дата выдачи", width=200)
            dpg.add_input_float(label="Средний балл", width=200)
            dpg.add_combo(label="Иностранный язык", items=["английский", "немецкий", "французский", "другой", "не изучал(а)"], width=300)

            dpg.add_checkbox(label="Ознакомлен с Уставом")
            dpg.add_checkbox(label="Ознакомлен с лицензией")
            dpg.add_checkbox(label="Ознакомлен с аккредитацией")
            dpg.add_checkbox(label="Ознакомлен с датой предоставления оригинала")
            dpg.add_checkbox(label="Ознакомлен с ответственностью за достоверность")

            dpg.add_input_text(label="Среднее проф. образование впервые (да/нет)", width=150)
            dpg.add_input_text(label="Необходимы условия по здоровью", width=400)
            dpg.add_input_text(label="Особые права при поступлении", width=400)

            dpg.add_input_text(label="Фактический адрес", width=400)
            dpg.add_input_text(label="Учет в ОППН", width=200)
            dpg.add_input_text(label="Творческие способности", multiline=True, width=400, height=50)
            dpg.add_input_text(label="Источник информации о колледже", width=400)

            dpg.add_input_text(label="Состав семьи (человек)", width=100)
            dpg.add_text("Отец (законный представитель)")
            dpg.add_input_text(label="ФИО", width=300)
            dpg.add_input_text(label="Место работы", width=300)
            dpg.add_input_text(label="Должность", width=300)
            dpg.add_input_text(label="Тел.", width=200)

            dpg.add_text("Мать (законный представитель)")
            dpg.add_input_text(label="ФИО", width=300)
            dpg.add_input_text(label="Место работы", width=300)
            dpg.add_input_text(label="Должность", width=300)
            dpg.add_input_text(label="Тел.", width=200)

            dpg.add_checkbox(label="Согласие на общественные работы")
            dpg.add_input_text(label="Ознакомлен с правилами подачи апелляции (да/нет)", width=150)
            dpg.add_input_text(label="Согласие на обработку персональных данных (ФИО)", width=400)

            dpg.add_input_text(label="Медицинские противопоказания", width=400)
            dpg.add_input_text(label="Специальность с ограничениями", width=400)
            dpg.add_input_text(label="Согласие на обследование", width=400)
            dpg.add_input_text(label="Дата", width=200)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
