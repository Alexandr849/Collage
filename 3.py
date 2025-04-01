import dearpygui.dearpygui as dpg

def save_callback():
    print("Save Clicked")

dpg.create_context()
dpg.create_viewport(width=700, height=800)
dpg.setup_dearpygui()


image_path = "C:/Users/user/Desktop/logotype.png"  # Или любой другой путь к файлу
width, height, channels, data = dpg.load_image(image_path)
    
with dpg.texture_registry(show=False):
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")


with dpg.font_registry():
    with dpg.font("C:/Windows/Fonts/times.ttf", 20) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

with dpg.window(label="Example Window", width=700, height=800, no_move=True):
    dpg.bind_font(default_font)
    dpg.add_image("texture_tag", width=width / 2, height=height / 2)
    dpg.add_same_line()
    
    with dpg.group():
        dpg.add_text("Директору  КГБПОУ\n«Красноярский колледж отраслевых\nтехнологий и предпринимательства»\nН.В. Журовой")
        full_name = dpg.add_input_text(label="ФИО", width=dpg.get_available_content_region())
        dpg.add_text("Паспорт")
        dpg.add_same_line()
        pass_serial = dpg.add_input_text(label="серия", width=145)
        dpg.add_same_line()
        pass_number = dpg.add_input_text(label="номер", width=145)



dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()