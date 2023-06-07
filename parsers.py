import shapefile as sh

def parse_trees_hight(file_path):
    records = []

    with sh.Reader(file_path) as sf:
        fields = [field[0] for field in sf.fields[1:]]  # Получаем названия полей из шейпфайла
        for shape_record in sf.shapeRecords():
            attributes = dict(zip(fields, shape_record.record))  # Создаем словарь атрибутов
            # geometry = shape_record.shape.__geo_interface__  # Получаем геометрию в формате GeoJSON
            # feature = {"attributes": attributes, "geometry": geometry}

            keys = ['NAME', 'GM_LAYER', 'MAP_NAME', 'LAYER', 'POINT_SYMB',
                    'FONT_SIZE', 'FONT_COLOR', 'FONT_CHARS'] # Вроде бесполезная информация.{Elevation также можно удалить}

            for key in keys:
                attributes.pop(key, None)

            if attributes['TreeID'] is not None:
                records.append(attributes)

    return records
