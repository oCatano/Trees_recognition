import shapefile as sh


def parse_trees_hight(file_path: str) -> list[dict()]:
    '''

    :param: file_path[str] -> Путь к файлу в одного из 5 форматов{.shp; .dbf; .prj; .shx; .cpg} который нужно распарсить.

    :return: records[list[dict()]] -> Список из attributes.

    :var: sf[<class 'shapefile.Reader'>] -> прочитанный сырой файл с данными;

          fields[list['str']] -> список из названия полей с sf:

                ['GM_LAYER', 'MAP_NAME', 'NAME', 'LAYER', 'TreeID',
                'TreeLocati', 'TreeLoca_1', 'TreeHeight', 'CrownDiame',
                'CrownArea', 'CrownVolum', 'ELEVATION', 'POINT_SYMB', 'FONT_SIZE',
                'FONT_COLOR', 'FONT_CHARS'];

          shape_record[<class 'shapefile.ShapeRecord'>] -> заключает в себе информацию об одном обьекте из sf  # метод shapeRecords() вернет geometry и attributes для всех обьектов в виде списка объектов ShapeRecord;

          attributes[dict('fields[i]': data)] -> словарь атрибутов обьекта shape_record, содержит ключи:
                ['TreeID', 'Coord_longitude', 'Coord_latitude', 'TreeHeight', 'CrownDiame',
                'CrownArea', 'CrownVolum', 'ELEVATION'];

    :add_var: keys[list['str']] -> список из ненужных ключей со списка fields

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


