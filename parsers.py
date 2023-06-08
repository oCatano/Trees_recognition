import shapefile as sh
import laspy
from laspy.file import File
from typing import List
from tqdm import tqdm


def parse_trees_hight(file_path: str) -> list[dict()]:
    '''
    Функция парсит данные о высотах деревьев

    :param: file_path[str] -> Путь к файлу в одного из 5 форматов{.shp; .dbf; .prj; .shx; .cpg} который нужно распарсить.

    :return: records[list[dict()]] -> Список из attributes.

    '''

    records = []

    with sh.Reader(file_path) as sf:
        fields = [field[0] for field in sf.fields[1:]]  # Получаем названия полей
        print(fields)
        for shape_record in sf.shapeRecords():
            attributes = dict(zip(fields, shape_record.record))  # Создаем словарь атрибутов
            # geometry = shape_record.shape.__geo_interface__  # Получаем геометрию в формате GeoJSON
            # feature = {"attributes": attributes, "geometry": geometry}

            keys = ['NAME', 'GM_LAYER', 'MAP_NAME', 'LAYER', 'POINT_SYMB',
                    'FONT_SIZE', 'FONT_COLOR',
                    'FONT_CHARS']  # Вроде бесполезная информация.{Elevation также можно удалить}
            attributes['Coord_longitude'] = attributes.pop('TreeLocati')
            attributes['Coord_latitude'] = attributes.pop('TreeLoca_1')
            for key in keys:
                attributes.pop(key, None)

            if attributes['TreeID'] is not None:
                records.append(attributes)

    return records

