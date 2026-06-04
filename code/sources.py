"""
Creates: sources.csv
Creates a data frame with the bibliographical references of the works used during the compilation process of the dataset.
"""

import pandas as pd
import numpy as np
from config import get_output_path

# Create comprehensive sources data
sources_data = []

# Books
books = [
    ('Ahlborn, Gunnar', 1946, 'Le Patois de Ruffieu-En-Valromey (Ain)', 'Elander', 'Göteborg', None, None, None, None),
    ('Álvarez Blanco, Rosario; Xove, Xosé', 2002, 'Gramática da Lingua Galega', 'Editorial Galaxia', 'Vigo', None, None, None, None),
    ('Ariza Viguera, Manuel', 1994, 'Sobre Fonética Histórica del Español', 'Arco/Libros', 'Madrid', None, None, None, None),
    ('Ariza Viguera, Manuel', 2012, 'Fonología y Fonética Históricas del Español', 'Arco/Libros', 'Madrid', None, None, None, None),
    ('Bonet, Eulália; Lloret, Maria-Rosa', 1998, 'Fonologia Catalana', 'Ariel', 'Barcelona', None, None, None, None),
    ('Bonfante, Giuliano', 1990, 'The Origin of the Romance Languages: Stages in the Development of Latin', 'Winter', 'Heidelberg', None, None, None, None),
    ('Celdrán Gomáriz, Pancracio', 2009, 'Diccionario de Topónimos Españoles y sus Gentilicios', 'Espasa', 'Madrid', None, None, None, None),
    ('Corominas, Joan; Pascual, José Antonio', 2012, 'Diccionario Crítico Etimológico Castellano e Hispánico', 'Gredos', 'Madrid', None, None, 'DCECH', None),
    ('Cuveiro Piñol, Juan', 1876, 'Diccionario Gallego', None, 'Barcelona', None, None, None, None),
    ('Dutton, Brian', 1992, 'Gonzalo de Berceo. Vida de San Millán de la Cogolla', 'Espasa-Calpe', 'Madrid', None, None, None, None),
    ('Carballeira Anllo, Xosé M.', None, 'Dicionario Xerais da Lingua', 'Xerais', 'Vigo', None, None, 'DXL', None),
    ('Echenique Elizondo, María Teresa; Martínez Alcalde, María José', 2011, 'Diacronía y Gramática Histórica de La Lengua Española', 'Tirant Humanidades', 'Valencia', None, None, None, None),
    ('Ferreiro Fernández, Manuel', 1996, 'Gramática Histórica Galega I', 'Laiovento', 'Santiago de Compostela', None, None, None, None),
    ('García González, Constantino', 1985, 'Glosario de Voces Galegas de Hoxe', 'Universidade de Santiago', None, None, None, None, None),
    ('García Turza, Claudio', 1992, 'Gonzalo de Berceo. Los Milagros de Nuestra Señora', 'Espasa-Calpe', 'Madrid', None, None, None, None),
    ('Andrés Díaz, Ramón de', 2013, 'Gramática Comparada de las Lenguas Ibéricas', 'Trea', 'Gijón', None, None, 'GCLI', None),
    ('Georges, Karl Ernst', 1998, 'Ausführliches Lateinisch-Deutsches Handwörterbuch', 'Wissenschaftliche Buchgesellschaft', 'Darmstadt', None, 'http://www.zeno.org', 'Georges', 'March 30, 2025'),
    ('García de Diego, Vicente; García de Diego, Carmen', 1989, 'Diccionario Etimológico Español e Hispánico', 'Espasa-Calpe', 'Madrid', None, None, 'DEEH', None),
    ('Houaiss, Antônio; Villar, Mauro; Franco, Francisco Manoel de Mello', 2004, 'Dicionário Eletronico Houaiss Da Língua Portuguesa', 'Objetiva', 'Rio de Janeiro', None, None, 'DEHLP', None),
    ('Rivas Quintas, Eligio', 2015, 'Dicionario Etimolóxico Da Lingua Galega', 'Tórculo', 'Santiago de Compostela', None, None, 'DELG', None),
    ('Cortelazzo, Manlio; Zolli, Paolo', 2021, 'Il Nuovo Etimologico: DELI - Dizionario Etimologico della Lingua Italiana', 'Zanichelli', 'Bologna', None, None, 'DELI', None),
    ('Diez, Friedrich; Scheler, Auguste', 1887, 'Etymologisches Wörterbuch der romanischen Sprachen', 'De Gruyter', 'Berlin; Boston', '10.1515/9783112605646', None, None, None),
    ('Figueiredo, Cândido de', 1939, 'Novo Dicionário da Língua Portuguesa', 'Bertrand', 'Lisboa', None, None, 'NDLP', None),
    ('Nunes, José J.', 1975, 'Compêndio de Gramática Histórica Portuguesa: (Fonética e Morfologia)', 'Teixeira', 'Lisboa', None, None, None, None),
    ('Glare, P. G. W.', 2012, 'Oxford Latin Dictionary', 'Oxford University Press', 'Oxford', None, None, 'OLD', None),
    ('Pagés, Aniceto de', 1914, 'Gran Diccionario de la Lengua Castellana (de Autoridades)', 'Fomento comercial del libro', 'Barcelona', None, None, None, None),
    ('Sobreira, Fr. J.; Pensado, J. L. (ed.)', 1979, 'Papeletas de un Diccionario Gallego', 'Instituto de Estudios Orensanos "Padre Feijoó"', 'Ourense', None, None, 'PDG', None),
    ('Penny, Ralph J.', 2002, 'A History of the Spanish Language', 'Cambridge University Press', 'Cambridge', None, None, None, None),
    ('Real Academia Española', 2011, 'Nueva Gramática de la Lengua Española. 3/1. Fonética y Fonología', 'Espasa Libros', 'Madrid', None, None, None, None),
    ('Regueira, Xosé L.', 2010, 'Dicionario de Pronuncia da Lingua Galega', 'Real Academia Galega', 'A Coruña', None, None, None, None),
    ('Ríos Panisse, M. do Carme', 1977, 'Nomenclatura de la Flora y Fauna Marítimas de Galicia. I. Invertebrados y Peces', 'Universidade de Santiago', None, None, None, None, None),
    ('Roberts, Edward A.', 2014, 'A Comprehensive Etymological Dictionary of the Spanish Language', 'Xlibris', 'Bloomington', None, None, None, None),
    ('Rodrigues Lapa, Manuel', 1931, 'Livro de Falcoaria de Pero Menino', 'Impresa da Universidade', 'Coimbra', None, None, None, None),
    ('Rodrigues Lapa, Manuel', 1970, "Cantigas d'escarnho e de Mal Dizer Dos Cancioneiros Medievais Galego-Portugueses", 'Galaxia', 'Vigo', None, None, None, None),
    ('Llorente Maldonado de Guevara, Antonio; Llorente Pinto, Mª del Rosario', 2003, 'Toponimia Salmantina', 'Diputación de Salamanca', 'Salamanca', None, None, None, None),
    ('Lorenzo Vázquez, Ramón', 1968, 'Sobre Cronologia Do Vocabulário Galego-Português', 'Galaxia', 'Vigo', None, None, 'CVGP', None),
    ('Lausberg, Heinrich', 1967, 'Romanische Sprachwissenschaft II: Konsonantismus', 'de Gruyter', 'Berlin', None, None, None, None),
    ('Lewis, Charlton T.; Short, Charles', 1879, 'A Latin Dictionary', None, None, None, 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.04.0059', 'LS', 'March 30, 2025'),
    ('Mariño Paz, Ramón', 2017, 'Fonética e Fonoloxía Históricas da Lingua Galega', 'Edicións Xerais de Galicia', 'Vigo', None, None, 'FF', None),
    ('Mariño Paz, Ramón', 2008, 'Historia de la Lengua Gallega', 'Lincom Europa', 'Muenchen', None, None, None, None),
    ('Mateus, Maria H. M.; d\'Andrade, Ernesto', 2000, 'The phonology of Portuguese', 'Oxford University Press', 'Oxford', None, None, None, None),
    ('Meyer-Lübke, Wilhelm', 1972, 'Grammatik der Romanischen Sprachen I. Romanische Lautlehre', 'Georg Olms Verlag', 'Hildesheim', None, None, None, None),
    ('Meyer-Lübke, Wilhelm', 1935, 'Romanisches etymologisches Wörterbuch', 'Winter', 'Heidelberg', None, None, 'REW', None),
    ('Pensado Ruiz, Carmen', 1984, 'Cronología Relativa del Castellano', 'Ediciones Universidad de Salamanca', 'Salamanca', None, None, 'CRC', None),
    ('Azevedo Maia, Clarinda de', 1986, 'História Do Galego-Português', 'Instituto nacional de Investigação Científica', 'Coimbra', None, None, 'HGP', None),
]

for book in books:
    sources_data.append({
        'source_type': 'book', 'author': book[0], 'year': book[1], 'title': book[2],
        'publisher': book[3], 'place': book[4], 'doi': book[5], 'url': book[6],
        'source_code': book[7], 'access_date': book[8], 'pages': None, 'database_name': None,
        'version': None, 'isbn': None
    })

# Edited volumes and manuscripts
edited_vols = [
    ('Brea, Mercedes (coord.)', 1996, 'Lírica Profana Galego-Portuguesa', 'Centro de Investigacións Lingüísticas e Literarias "Ramón Piñeiro"', 'Santiago de Compostela', 'LPGP'),
    ('Cintra, Luís F. L. (ed.)', 1959, 'A Linguagem Dos Foros de Castelo Rodrigo', 'Centro de Estudos Filológicos', 'Lisboa', 'FCR'),
    ('Costa, P. Avelino de Jesús da (ed.)', 1999, 'Livro Preto. Cartulário da Sé de Coimbra', 'Arquivo da Universidade de Coimbra', 'Coimbra', None),
    ('Duro Peña, Emilio (ed.)', 1972, 'El Monasterio de S. Pedro de Rocas y su Colección Documental', 'Instituto de Estudios Orensanos "Padre Feijoó"', 'Ourense', 'MPR'),
    ('Fernández de Viana y Vieites, José I. (ed.)', 1995, 'Colección Diplomática del Monasterio de Santa María de Ferreira de Pantón', 'Servicio de Publicaciones de la Diputación Provincial de Lugo', 'Lugo', 'MSMDFP'),
    ('Graña Cid, María del Mar (ed.)', 1990, 'Las Órdenes Mendicantes en el Obispado de Mondoñedo', None, None, 'OMOM'),
    ('Hernández, Fabián (ed.)', 1866, 'Becerro de las Behetrías de Castilla', 'Librería de Fabián Hernández', 'Santander', None),
    ('Herrera, María T.; Sánchez, María Nieves (eds.)', 2000, 'Traducción de la Historia de Jerusalem abreviada de Jacobo de Vitriaco', 'Universidad de Salamanca', 'Salamanca', None),
    ('Herrero Jiménez, Mauricio', 2004, 'Documentos de la Colección de Pergaminos del Archivo de la Real Chancillería de Valladolid (934-1300)', None, 'León', None),
    ('Lorenzo, Ramón', 1985, 'Crónica Troiana. Introducción e Texto', 'Fundación Pedro Barrié de la Maza, Conde de Fenosa', 'A Coruña', 'CT'),
    ('Lorenzo, Ramón (ed.)', '1975/1977', 'La Traducción Gallega de La Crónica General y de La Crónica de Castilla', 'Instituto de Estudios Orensanos Padre Feijoó', 'Ourense', 'TC'),
    ('López Ferreiro, Antonio (ed.)', 1975, 'Fueros Municipales de Santiago y de su Tierra', 'Ediciones Castilla', 'Madrid', 'FMST'),
    ('López Ferreiro, Antonio (ed.)', 1901, 'Galicia Histórica. Colección Diplomática', 'Tipografía Galaica', 'Santiago de Compostela', 'GHCD'),
    ('Lucas Álvarez, Manuel', 1986, 'El Tumbo de San Julián de Samos (siglos VIII-XII)', 'Caixa Galicia', 'Santiago de Compostela', None),
    ('Lucas Álvarez, Manuel; Lucas Domínguez, Pedro (eds.)', 1988, 'San Pedro de Ramirás. Un Monasterio Femenino en la Edad Media', 'Publicacións de Caixa Galicia', 'Santiago', 'PRMF'),
    ('Martínez López, Ramón (ed.)', 1963, 'General Estoria. Versión Gallega Del Siglo XIV', 'Publicacións de Archivum', 'Oviedo', 'XH'),
    ('Martínez Salazar, Andrés (ed.)', 1911, 'Documentos Gallegos de Los Siglos XIII al XVI', 'Casa de la Misericordia', 'A Coruña', 'DGS13-16'),
    ('Mettmann, Walter (ed.)', 1959, 'Cantigas de Santa Maria', 'Acta Universitatis Conimbrigensis', 'Coimbra', 'CSM'),
    ('Parker, Kelvin M. (ed.)', 1975, 'Historia Troyana', 'Instituto Padre Sarmiento', 'Santiago de Compostela', 'HT'),
    ('Pensado Tomé, José Luís (ed.)', 1958, 'Os Miragres de Santiago', 'C.S.I.C', 'Madrid', 'MS'),
    ('Pensado Tomé, José L. (ed.)', 2004, 'Tratado de Albeitaria', 'Centro "Ramón Piñeiro"', 'Santiago de Compostela', 'TA'),
    ('Pérez Rodríguez, Francisco J. (ed.)', 2004, 'Os Documentos do Tombo de Toxos Outos', 'Consello da Cultura Galega', 'Santiago de Compostela', 'DTT'),
    ('Portela Silva, Ermelindo (ed.)', 1976, 'La Región Del Obispado de Tuy En Los Siglos XII a XV', 'Fundación "Pedro Barrié de la Maza', 'A Coruña', 'ROT'),
    ('Rodríguez González, Ángel (ed.)', 1992, 'Libro do Concello de Santiago (1416-1422)', 'Consello da Cultura Galega', 'Santiago de Compostela', 'LCS'),
    ('Rodríguez González, Angel; Armas Castro, José (eds.)', 1992, 'Minutario Notarial de Pontevedra (1433-1435)', 'Consello da Cultura Galega', 'Santiago de Compostela', 'MNP'),
    ('Rodríguez Núñez, Clara (ed.)', 1989, 'Santa María de Belvís, un Convento Mendicante Femenino en la Baja Edad Media (1305-1400)', None, None, 'MB'),
    ('Romaní Martínez, Miguel (ed)', '1989-93', 'La Colección Diplomática de Santa María de Oseira (1025-1310)', None, 'Santiago de Compostela', 'CDMO'),
    ('Sánchez-Prieto Borja, Pedro', 2004, 'Ferrer Sayol. Libro de palladio. BNM 10211', 'Universidad de Alcalá de Henares', 'Alcalá de Henares', None),
    ('Tato Plaza, Fernando R.', 1999, 'Libro de Notas de Álvaro Pérez, Notarío da Terra de Rianxo e Postmarcos (1457)', 'Consello de Cultura Galega', 'Santiago de Compostela', None),
    ('Cabana Outeiro, Alexandra (ed.)', 2003, 'O Tombo H da Catedral de Santiago', 'Concello de Valga', 'Valga', 'THCS'),
    ('Portugaliae Monumenta Historica', '1856-1917', 'Portugaliae Monumenta Historica', 'Academia das Ciências de Lisboa', 'Lisbon', 'PMH'),
]

for vol in edited_vols:
    sources_data.append({
        'source_type': 'edited_volume', 'author': vol[0], 'year': vol[1], 'title': vol[2],
        'publisher': vol[3], 'place': vol[4], 'source_code': vol[5], 'doi': None, 'url': None,
        'access_date': None, 'pages': None, 'database_name': None, 'version': None, 'isbn': None
    })

# Dissertations
dissertations = [
    ('Freitas, Odília de Jesus', 1948, 'Estudo do Falar de Santa Valha', 'University of Coimbra'),
    ('Salgueiro, Mariana de Lourdes', 1945, 'Contribuição para um estudo Linguístico-Etnográfico de Quatro Aldeias', 'University of Coimbra'),
]

for diss in dissertations:
    sources_data.append({
        'source_type': 'dissertation', 'author': diss[0], 'year': diss[1], 'title': diss[2],
        'publisher': diss[3], 'place': None, 'source_code': None, 'doi': None, 'url': None,
        'access_date': None, 'pages': None, 'database_name': None, 'version': None, 'isbn': None
    })

# Articles
articles = [
    ('Álvarez Blanco, Rosario', 1991, 'O Sistema Fonolóxico do Galego. Comparación co do Portugués', '517-530', None),
    ('Bombien, Lasse; Hoole, Philip', 2013, 'Articulatory Overlap as a Function of Voicing in French and German Consonant Clusters', '539-50', '10.1121/1.4807510'),
    ('Castro, Teresa de', 2001, 'El Tratado Sobre el Vestir, Calzar y Comer del Arzobispo Hernando de Talavera', '11-92', None),
    ('D\'Ovidio, Francesco; Meyer, Wilhelm', None, 'Die italienische Sprache', '489-560', None),
    ('Lloyd, Paul M.', 1970, 'A Note on Latin Syllable Structure', '41-42', None),
    ('Lorenzo Vázquez, Ramón', 1962, 'Estudios Etnográfico-Lingüísticos sobre la Mahía y Aledaños. El horno y el arado', '487-522', None),
    ('Michaëlis de Vasconcelos, Carolina', 1920, 'Glossário do Cancioneiro da Ajuda', '1-95', None),
    ('Otero Álvarez, Aníbal', 1951, 'Hipótesis Etimológicas Referentes al Gallego-Portugués', '83-114', None),
    ('Repetti, Lori; Tuttle, Edward F.', 1987, 'The Evolution of Latin pl, bl, and cl, gl in Western Romance', '53-115', None),
    ('Torreblanca, Máximo', 1990, 'La Evolución /kl-, pl-, fl-/ > ll en Español', '317-27', '10.3989/rfe.1990.v70.i3/4.670'),
    ('Viudas Camarasa, Antonio', 1979, 'Sobre La Evolución de \'pl-\' a \'Pll-\' y \'Cl-\' a \'Cll-\' En Aragonés Antiguo', '355-75', None),
]

for art in articles:
    sources_data.append({
        'source_type': 'article', 'author': art[0], 'year': art[1], 'title': art[2],
        'pages': art[3], 'doi': art[4], 'publisher': None, 'place': None, 'source_code': None,
        'url': None, 'access_date': None, 'database_name': None, 'version': None, 'isbn': None
    })

# Online dictionaries and databases
online_sources = [
    ('online_dictionary', 'Aragonario', 2025, 'Aragonario. Diccionario Castellano/Aragonés, Aragonés/Castellano', 'https://aragonario.aragon.es', 'March 30, 2025', 'Aragonario', None),
    ('online_corpus', 'Lopes, Graça Videira; Ferreira, Manuel Pedro et al.', '2011-', 'Cantigas Medievais Galego Portuguesas', 'http://cantigas.fcsh.unl.pt', 'March 30, 2025', 'CMGP', None),
    ('online_corpus', 'Corpus Documentale Latinum Gallaeciae', 2023, 'Corpus Documentale Latinum Gallaeciae', 'http://corpus.cirp.es/codolga', 'March 30, 2025', 'CODOLGA', '20'),
    ('online_corpus', 'Real Academia Española', None, 'Banco de Datos (CORDE). Corpus Diacrónico Del Español', 'http://www.rae.es', 'March 30, 2025', 'CORDE', None),
    ('online_dictionary', 'Santamarina, Antón (cood.)', None, 'Diccionario de Diccionarios', 'https://ilg.usc.gal/ddd/index.php', 'March 30, 2025', 'DDD', None),
    ('online_dictionary', 'González Seoane, Ernesto (coord.); Álvarez de la Granja, María; Boullón Agrelo, Ana I.', '2006-2022', 'Dicionario de Dicionarios Do Galego Medieval', 'http://ilg.usc.gal/ddgm/', 'March 30, 2025', 'DDGM', None),
    ('online_dictionary', 'García Arias, Xose L.', 2025, 'Diccionario General de La Lengua Asturiana', 'https://mas.lne.es/diccionario/', 'March 30, 2025', 'DGLA', None),
    ('online_dictionary', 'Real Academia Española', None, 'Diccionario de la Lengua Española', 'https://dle.rae.es', 'March 30, 2025', 'DRAE', '23.8'),
    ('online_dictionary', 'González González, Manuel (dir.)', None, 'Dicionario da Real Academia Galega', 'https://academia.gal/dicionario', 'March 30, 2025', 'DRAG', None),
    ('online_dictionary', 'Real Academia Española', None, 'Nuevo Tesoro Lexicográfico de la Lengua Española', 'https://apps.rae.es/ntlle/SrvltGUILoginNtlle', 'March 30, 2025', 'NTLLE', None),
    ('online_dictionary', 'Real Academia Española', 2021, 'Tesoro de Los Diccionarios Históricos de La Lengua Española', 'https://www.rae.es/tdhle/', 'March 30, 2025', 'TDHLE', None),
    ('online_corpus', 'Santamarina, Antón (dir.); González Seoane, Ernesto; Álvarez de la Granja, María', None, 'Tesouro Informatizado de Lingua Galega', 'http://ilg.usc.gal/TILG/', 'March 30, 2025', 'TILG', '4.1'),
    ('online_corpus', 'Álvarez, Rosario (coord.)', None, 'Tesouro do Léxico Patrimonial Galego e Portugués', 'http://ilg.usc.es/Tesouro', 'March 30, 2025', 'TLPGP', None),
    ('online_corpus', 'Varela Barreiro, Xavier (dir.)', '2004-', 'Tesouro Medieval Informatizado Da Lingua Galega', 'http://ilg.usc.es/tmilg', 'March 30, 2025', 'TMILG', None),
    ('online_corpus', 'Ferreiro, Manuel (dir.)', '2018-', 'Universo Cantigas. Edición Crítica da Poesía Medieval Galego-Portuguesa', 'http://universocantigas.gal', 'June 10, 2025', 'UC', None),
    ('online_project', 'Fernandes, Maria A.', None, 'Chaves. In Toponimia de Galicia e Portugal', 'http://toponhisp.org', 'June 24, 2025', None, None),
    ('online_project', 'Fuente Cornejo, Toribio', None, 'Riaño. In Toponimia asturiano-leonesa', 'http://toponhisp.org', 'June 26, 2025', None, None),
]

for src in online_sources:
    sources_data.append({
        'source_type': src[0], 'author': src[1], 'year': src[2], 'title': src[3],
        'url': src[4], 'access_date': src[5], 'source_code': src[6], 'version': src[7],
        'publisher': None, 'place': None, 'doi': None, 'pages': None, 'database_name': None,
        'isbn': None
    })

# Create DataFrame
sources_df = pd.DataFrame(sources_data)

# Reorder columns
column_order = ['source_type', 'author', 'year', 'title', 'publisher', 'place', 
                'pages', 'url', 'access_date', 'database_name', 'source_code', 
                'version', 'isbn', 'doi']
sources_df = sources_df[column_order]

# Add source_id as index (starts from 1)
sources_df.index = range(1, len(sources_df) + 1)
sources_df.index.name = 'source_id'

# Display info
# print(f"Total sources: {len(sources_df)}")
# print(f"\nSource types distribution:")
# print(sources_df['source_type'].value_counts())
# print(f"\nFirst few rows:")

# Optional: save to CSV
sources_df.to_csv(get_output_path('sources.csv'))
print("Created: sources.csv")

# # The DataFrame is now ready to use
# print(sources_df)
