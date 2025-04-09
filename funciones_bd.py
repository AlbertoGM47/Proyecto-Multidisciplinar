import sqlite3
import os
from datetime import datetime

def rellenar_tabla(BD="BD_Puesto_Lean_copia.db"):
    connection = sqlite3.connect(BD)
    cursor = connection.cursor()
    # Insertar datos en BOM
    cursor.executemany('''INSERT INTO BOM (ID, Ref_padre, Ref_hijo) VALUES (?, ?, ?)''', [
        (100, 'MG-R12-0-12-65-T', 'S1'),
        (101, 'MG-R12-0-12-65-T', 'WPP1'),
        (102, 'MG-R12-0-12-65-T', 'BU_12'),
        (103, 'MG-R12-0-12-65-T', 'BO_M8x65'),
        (104, 'MG-R12-0-12-65-T', 'NUT_M8'),
        (105, 'MG-R20-1-12-65-T', 'S1'),
        (106, 'MG-R20-1-12-65-T', 'WPP2'),
        (107, 'MG-R20-1-12-65-T', 'BEARING'),
        (108, 'MG-R20-1-12-65-T', 'BU_12'),
        (109, 'MG-R20-1-12-65-T', 'BO_M8x65'),
        (110, 'MG-R20-1-12-65-T', 'NUT_M8'),
        (111, 'MG-H20-1-12-65-T', 'S1'),
        (112, 'MG-H20-1-12-65-T', 'WP1'),
        (113, 'MG-H20-1-12-65-T', 'BEARING'),
        (114, 'MG-H20-1-12-65-T', 'B_12'),
        (115, 'MG-H20-1-12-65-T', 'BO_M8x65'),
        (116, 'MG-H20-1-12-65-T', 'NUT_M8'),
        (117, 'MG-B12-0-12-65-T', 'S1'),
        (118, 'MG-B12-0-12-65-T', 'WN1'),
        (119, 'MG-B12-0-12-65-T', 'BU_12'),
        (120, 'MG-B12-0-12-65-T', 'BO_M8x65'),
        (121, 'MG-B12-0-12-65-T', 'NUT_M8'),
        (122, 'MG-B14-0-14-65-T', 'S1'),
        (123, 'MG-B14-0-14-65-T', 'WN2'),
        (124, 'MG-B14-0-14-65-T', 'BU_14'),
        (125, 'MG-B14-0-14-65-T', 'BO_M8x65'),
        (126, 'MG-B14-0-14-65-T', 'NUT_M8'),
        (127, 'MG-B20-1-12-65-T', 'S1'),
        (128, 'MG-B20-1-12-65-T', 'WN3'),
        (129, 'MG-B20-1-12-65-T', 'BEARING'),
        (130, 'MG-B20-1-12-65-T', 'BU_12'),
        (131, 'MG-B20-1-12-65-T', 'BO_M8x65'),
        (132, 'MG-B20-1-12-65-T', 'NUT_M8'),
        (133, 'MP-R12-0-12-60-T', 'S2'),
        (134, 'MP-R12-0-12-60-T', 'WPP1'),
        (135, 'MP-R12-0-12-60-T', 'BU_12'),
        (136, 'MP-R12-0-12-60-T', 'BO_M8x60'),
        (137, 'MP-R12-0-12-60-T', 'NUT_M8'),
        (138, 'MP-R20-1-12-60-T', 'S2'),
        (139, 'MP-R20-1-12-60-T', 'WPP2'),
        (140, 'MP-R20-1-12-60-T', 'BEARING'),
        (141, 'MP-R20-1-12-60-T', 'BU_12'),
        (142, 'MP-R20-1-12-60-T', 'BO_M8x60'),
        (143, 'MP-R20-1-12-60-T', 'NUT_M8'),
        (144, 'MP-H20-1-12-60-T', 'S2'),
        (145, 'MP-H20-1-12-60-T', 'WP1'),
        (146, 'MP-H20-1-12-60-T', 'BEARING'),
        (147, 'MP-H20-1-12-60-T', 'BU_12'),
        (148, 'MP-H20-1-12-60-T', 'BO_M8x60'),
        (149, 'MP-H20-1-12-60-T', 'NUT_M8'),
        (150, 'MP-B12-0-12-60-T', 'S2'),
        (151, 'MP-B12-0-12-60-T', 'WN1'),
        (152, 'MP-B12-0-12-60-T', 'BU_12'),
        (153, 'MP-B12-0-12-60-T', 'BO_M8x60'),
        (154, 'MP-B12-0-12-60-T', 'NUT_M8'),
        (155, 'MP-B14-0-14-60-T', 'S2'),
        (156, 'MP-B14-0-14-60-T', 'WN2'),
        (157, 'MP-B14-0-14-60-T', 'BU_14'),
        (158, 'MP-B14-0-14-60-T', 'BO_M8x60'),
        (159, 'MP-B14-0-14-60-T', 'NUT_M8'),
        (160, 'MP-B20-1-12-60-T', 'S2'),
        (161, 'MP-B20-1-12-60-T', 'WN3'),
        (162, 'MP-B20-1-12-60-T', 'BEARING'),
        (163, 'MP-B20-1-12-60-T', 'BU-12'),
        (164, 'MP-B20-1-12-60-T', 'BO_M8x60'),
        (165, 'MP-B20-1-12-60-T', 'NUT_M8'),
        (166, 'FG-R12-0-12-65-T', 'S3'),
        (167, 'FG-R12-0-12-65-T', 'WPP1'),
        (168, 'FG-R12-0-12-65-T', 'BU_12'),
        (169, 'FG-R12-0-12-65-T', 'BO_M8x65'),
        (170, 'FG-R12-0-12-65-T', 'NUT_M8'),
        (171, 'FG-R20-1-12-65-T', 'S3'),
        (172, 'FG-R20-1-12-65-T', 'WPP2'),
        (173, 'FG-R20-1-12-65-T', 'BEARING'),
        (174, 'FG-R20-1-12-65-T', 'BU_12'),
        (175, 'FG-R20-1-12-65-T', 'BO_M8x65'),
        (176, 'FG-R20-1-12-65-T', 'NUT_M8'),
        (177, 'FG-H20-1-12-65-T', 'S3'),
        (178, 'FG-H20-1-12-65-T', 'WP1'),
        (179, 'FG-H20-1-12-65-T', 'BEARING'),
        (180, 'FG-H20-1-12-65-T', 'BU_12'),
        (181, 'FG-H20-1-12-65-T', 'BO_M8x65'),
        (182, 'FG-H20-1-12-65-T', 'NUT_M8'),
        (183, 'FG-B12-0-12-65-T', 'S3'),
        (184, 'FG-B12-0-12-65-T', 'WN1'),
        (185, 'FG-B12-0-12-65-T', 'BU_12'),
        (186, 'FG-B12-0-12-65-T', 'BO_M8x65'),
        (187, 'FG-B12-0-12-65-T', 'NUT_M8'),
        (188, 'FG-B14-0-14-65-T', 'S3'),
        (189, 'FG-B14-0-14-65-T', 'WN2'),
        (190, 'FG-B14-0-14-65-T', 'BU_14'),
        (191, 'FG-B14-0-14-65-T', 'BO_M8x65'),
        (192, 'FG-B14-0-14-65-T', 'NUT_M8'),
        (193, 'FG-B20-1-12-65-T', 'S3'),
        (194, 'FG-B20-1-12-65-T', 'WN3'),
        (195, 'FG-B20-1-12-65-T', 'BEARING'),
        (196, 'FG-B20-1-12-65-T', 'BU_12'),
        (197, 'FG-B20-1-12-65-T', 'BO_M8x65'),
        (198, 'FG-B20-1-12-65-T', 'NUT_M8'),
        (199, 'FP-R12-0-12-60-T', 'S4'),
        (200, 'FP-R12-0-12-60-T', 'WPP1'),
        (201, 'FP-R12-0-12-60-T', 'BU_12'),
        (202, 'FP-R12-0-12-60-T', 'BO_M8x60'),
        (203, 'FP-R12-0-12-60-T', 'NUT_M8'),
        (204, 'FP-R20-1-12-60-T', 'S4'),
        (205, 'FP-R20-1-12-60-T', 'WPP2'),
        (206, 'FP-R20-1-12-60-T', 'BEARING'),
        (207, 'FP-R20-1-12-60-T', 'BU_12'),
        (208, 'FP-R20-1-12-60-T', 'BO_M8x60'),
        (209, 'FP-R20-1-12-60-T', 'NUT_M8'),
        (210, 'FP-H20-1-12-60-T', 'S4'),
        (211, 'FP-H20-1-12-60-T', 'WP1'),
        (212, 'FP-H20-1-12-60-T', 'BEARING'),
        (213, 'FP-H20-1-12-60-T', 'BU_12'),
        (214, 'FP-H20-1-12-60-T', 'BO_M8x60'),
        (215, 'FP-H20-1-12-60-T', 'NUT_M8'),
        (216, 'FP-B12-0-12-60-T', 'S4'),
        (217, 'FP-B12-0-12-60-T', 'WN1'),
        (218, 'FP-B12-0-12-60-T', 'BU_12'),
        (219, 'FP-B12-0-12-60-T', 'BO_M8x60'),
        (220, 'FP-B12-0-12-60-T', 'NUT_M8'),
        (221, 'FP-B14-0-14-60-T', 'S4'),
        (222, 'FP-B14-0-14-60-T', 'WN2'),
        (223, 'FP-B14-0-14-60-T', 'BU_14'),
        (224, 'FP-B14-0-14-60-T', 'BO_M8x60'),
        (225, 'FP-B14-0-14-60-T', 'NUT_M8'),
        (226, 'FP-B20-1-12-60-T', 'S4'),
        (227, 'FP-B20-1-12-60-T', 'WN3'),
        (228, 'FP-B20-1-12-60-T', 'BEARING'),
        (229, 'FP-B20-1-12-60-T', 'BU_12'),
        (230, 'FP-B20-1-12-60-T', 'BO_M8x60'),
        (231, 'FP-B20-1-12-60-T', 'NUT_M8')
    ])

    # Insertar datos en Stock_Minimo
    cursor.executemany('''INSERT INTO Stock_Minimo (Nombre, Stock_minimo) VALUES (?, ?)''', [
        ('S1', 2),
        ('S2', 2),
        ('S3', 2),
        ('S4', 2),
        ('WN1', 2),
        ('WN2', 2),
        ('WN3', 2),
        ('WP1', 2),
        ('WPP1', 2),
        ('WPP2', 2),
        ('BEARING', 2),
        ('BU_14', 2),
        ('BU_12', 2),
        ('BO_M8x65', 2),
        ('BO_M8x60', 2),
        ('NUT_M8', 2)
    ])

    # Insertar datos en Componente_Bien
    timestamp_actual = int(datetime.now().timestamp())  # Obtener la marca de tiempo actual
    cursor.executemany('''INSERT INTO Componente_Bien (ID, Nombre, Descripcion, CosteUnitario, Proveedor, Stock, Stock_minimo, FechaIngreso) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', [
        (100, 'S1', None, 1.0, 1, 10, 2, timestamp_actual),
        (101, 'S2', None, 1.5, 1, 10, 2, timestamp_actual),
        (102, 'S3', None, 2.0, 1, 10, 2, timestamp_actual),
        (103, 'S4', None, 1.75, 1, 10, 2, timestamp_actual),
        (104, 'WN1', None, 0.5, 1, 5, 2, timestamp_actual),
        (105, 'WN2', None, 0.45, 1, 5, 2, timestamp_actual),
        (106, 'WN3', None, 0.6, 1, 5, 2, timestamp_actual),
        (107, 'WP1', None, 0.9, 1, 5, 2, timestamp_actual),
        (108, 'WPP1', None, 0.99, 1, 5, 2, timestamp_actual),
        (109, 'WPP2', None, 1.05, 1, 5, 2, timestamp_actual),
        (110, 'BEARING', None, 0.2, 1, 6, 2, timestamp_actual),
        (111, 'BU_12', None, 0.15, 1, 2, 2, timestamp_actual),
        (112, 'BU_14', None, 0.15, 1, 7, 2, timestamp_actual),
        (113, 'BO_M8x65', None, 0.1, 1, 5, 2, timestamp_actual),
        (114, 'BO_M8x60', None, 0.08, 1, 2, 2, timestamp_actual),
        (115, 'NUT_M8', None, 0.05, 1, 6, 2, timestamp_actual),
    ])

    # Insertar datos en pedidos
    cursor.executemany('''INSERT INTO pedidos (ID, cliente, fecha, referencia, unidades, orden_fabricacion, estado) VALUES (?, ?, ?, ?, ?, ?, ?)''', [
        (1, 'Bricomart', 1740748380, 'MG-R12-0-12-65-T', 4, 567, 'PENDIENTE'),
        (2, 'Leroy Merlin', 1740748450, 'MG-B12-0-12-65-T', 7, 565, 'EN PROCESO')
    ])

    connection.commit()
    connection.close()

def create_database(BD="BD_Puesto_Lean_copia.db"):
    connection = sqlite3.connect(BD)
    cursor = connection.cursor()

    # Crear tabla BOM
    cursor.execute('''CREATE TABLE IF NOT EXISTS BOM (
                        ID INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        Ref_padre TEXT NOT NULL,
                        Ref_hijo TEXT NOT NULL);''')

    # Crear tabla Componente_Bien
    cursor.execute('''CREATE TABLE IF NOT EXISTS Componente_Bien (
                        ID INTEGER PRIMARY KEY NOT NULL,
                        Nombre TEXT NOT NULL,
                        Descripcion TEXT,
                        CosteUnitario REAL NOT NULL,
                        Proveedor INTEGER NOT NULL,
                        Stock INTEGER NOT NULL,
                        Stock_minimo INTEGER NOT NULL,
                        FechaIngreso INTEGER NOT NULL,
                        FOREIGN KEY (Stock_minimo) REFERENCES Stock_Minimo(Stock_minimo)
                   );''')  # Cerramos correctamente el paréntesis

    # Crear tabla pedidos
    cursor.execute('''CREATE TABLE IF NOT EXISTS pedidos (
                        ID INTEGER PRIMARY KEY,
                        cliente TEXT NOT NULL,
                        fecha INTEGER NOT NULL,
                        referencia TEXT NOT NULL,
                        unidades INTEGER NOT NULL,
                        orden_fabricacion INTEGER,
                        tiempo_inicio INTEGER,
                        tiempo_fin INTEGER,
                        duracion INTEGER,
                        estado TEXT NOT NULL
                    );''')

    # Crear tabla Stock_Minimo
    cursor.execute('''CREATE TABLE IF NOT EXISTS Stock_Minimo (
                        Nombre TEXT PRIMARY KEY NOT NULL,
                        Stock_minimo INTEGER NOT NULL);''')

    connection.commit()
    connection.close()