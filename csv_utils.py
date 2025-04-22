import pandas as pd
import chardet as cd

def detect_encoding(filename, bytes=10000):
     with open(filename, 'rb') as f:
          encoding = cd.detect(f.read(bytes))
     print(encoding['confidence'])
     return encoding['encoding']


filename = "test_contactos.csv"
new_filename = filename.replace(".csv", "") + "_converted.csv"
old_encoding = detect_encoding(filename)

df_no_utf8 = pd.read_csv(filename, encoding=old_encoding)
df_no_utf8.to_csv(new_filename, index=False, encoding='utf-8-sig')

df = pd.read_csv(new_filename)

column_mapping = {
    'First Name': ['Primer nombre', 'Nombre'],
    'Last Name': ['Apellido', 'Apellidos'],
    'Nickname': ['Apodo'],
    'Display Name': ['Nombre mostrado', 'Nombre en pantalla'],
    'E-mail Address': ['Dirección de correo electrónico principal'],
    'E-mail 2 Address': ['Dirección de correo electrónico secundaria'],
    'Business Phone': ['Teléfono (Trabajo)'],
    'Home Phone': ['Teléfono particular'],
    'Business Fax': ['Fax'],
    'Pager': ['Buscapersonas'],
    'Mobile Phone': ['Teléfono móvil'],
    'Home Street': ['Dirección personal'],
    'Home City': ['Ciudad donde vive'],
    'Home State': ['Provincia'],
    'Home Postal Code': ['Código postal'],
    'Home Country/Region': ['País de residencia'],
    'Business Street': ['Dirección de trabajo'],
    'Business City': ['Ciudad (Trabajo)'],
    'Business State': ['Provincia (Trabajo)'],
    'Business Postal Code': ['Código postal (Trabajo)'],
    'Business Country/Region': ['País (Trabajo)'],
    'Job Title': ['Cargo', 'Puesto'],
    'Department': ['Departamento'],
    'Company': ['Compañía', 'Organización'],
    'Web Page': ['Página web 1'],
    'Notes': ['Notas']
}

num_of_columns = df.shape[1]

for column in df.columns:
     for new_title in column_mapping:
          if(column in column_mapping[new_title]):
               df.rename(columns={column:new_title}, inplace=True)
               break


df.to_csv(new_filename, index=False)
