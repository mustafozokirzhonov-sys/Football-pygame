"""
Режем спрайт-лист на отдельные кадры, обрезаем пустое место вокруг
персонажа и увеличиваем масштаб — чтобы кадры были готовы для игры.

Как пользоваться:
1. Положи свой спрайт-лист рядом с этим скриптом (или укажи полный путь)
2. Поменяй SHEET_PATH, FRAME_COUNT и TARGET_HEIGHT под свой файл
3. Запусти: python slice_sprites.py
4. В папке frames_output появятся отдельные PNG — idle_1.png, idle_2.png и т.д.
"""

from PIL import Image
import os

# =========================================================
# НАСТРОЙКИ — поменяй под свой файл
# =========================================================
SHEET_PATH = "RUNNING.png"   # путь к скачанному файлу
FRAME_COUNT = 4                              # сколько кадров в листе (считаем сами по картинке)
TARGET_HEIGHT = 120                          # до какой высоты увеличить персонажа (пикселей)
OUTPUT_DIR = "player-running"
OUTPUT_PREFIX = ""                       # imя_1.png, имя_2.png ...


def trim_transparent(image):
    """Обрезает прозрачные поля вокруг персонажа, оставляя только сам рисунок."""
    bbox = image.getbbox()   # находит границы непрозрачных пикселей
    if bbox:
        return image.crop(bbox)
    return image


def main():
    sheet = Image.open(SHEET_PATH).convert("RGBA")
    sheet_width, sheet_height = sheet.size

    # ширина одного кадра = вся ширина листа / количество кадров
    frame_width = sheet_width // FRAME_COUNT

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for i in range(FRAME_COUNT):
        # 1. вырезаем i-й кадр из общего листа
        left = i * frame_width
        box = (left, 0, left + frame_width, sheet_height)
        frame = sheet.crop(box)

        # 2. убираем пустое прозрачное поле вокруг персонажа
        frame = trim_transparent(frame)

        # 3. увеличиваем до нужного размера, сохраняя пропорции
        #    NEAREST — важно для пиксель-арта, чтобы картинка не размылась
        scale = TARGET_HEIGHT / frame.height
        new_size = (round(frame.width * scale), round(frame.height * scale))
        frame = frame.resize(new_size, Image.NEAREST)

        # 4. сохраняем готовый кадр
        out_path = os.path.join(OUTPUT_DIR, f"{i + 1}.png")
        frame.save(out_path)
        print(f"Сохранил {out_path}  —  размер {frame.size}")


if __name__ == "__main__":
    main()