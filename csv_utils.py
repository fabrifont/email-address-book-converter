import pandas as pd
import chardet as cd

column_mapping = {
     'First Name': ['Primer nombre', 'Nombre'],
     'Last Name': ['Apellido', 'Apellidos'],
     'Nickname': ['Apodo'],
     #'Display Name': ['NO Nombre mostrado', 'Nombre en pantalla'],
     'E-mail Address': ['Dirección de correo electrónico principal', 'DirecciÃ³n de correo electrÃ³nico principal', 'Emails'],
     'E-mail 2 Address': ['Dirección de correo electrónico secundaria', 'DirecciÃ³n de correo electrÃ³nico secundaria'],
     'Business Phone': ['Teléfono (Trabajo)', 'TelÃ©fono (Trabajo)'],
     'Home Phone': ['Teléfono particular', 'TelÃ©fono particular'],
     'Business Fax': ['Fax'],
     'Pager': ['Buscapersonas'],
     'Mobile Phone': ['Teléfono móvil', 'TelÃ©fono mÃ³vil', 'Phone Numbers'],
     'Home Street': ['Dirección personal', 'Address'],
     'Home City': ['Ciudad donde vive'],
     'Home State': ['Provincia'],
     'Home Postal Code': ['Código postal'],
     'Home Country/Region': ['País de residencia'],
     'Business Street': ['Dirección de trabajo'],
     'Business City': ['Ciudad (Trabajo)'],
     'Business State': ['Provincia (Trabajo)'],
     'Business Postal Code': ['Código postal (Trabajo)'],
     'Business Country/Region': ['País (Trabajo)'],
     'Job Title': ['Cargo', 'Puesto', 'Designation'],
     'Department': ['Departamento'],
     'Company': ['Compañía', 'Organización'],
     'Web Page': ['Página web 1'],
     'Notes': ['Notas']
}

def detect_encoding(filename, bytes=10000):
     with open(filename, 'rb') as f:
          encoding = cd.detect(f.read(bytes))
     print(encoding['confidence'])
     return encoding['encoding']

def convert_csv_utf8(file):
     new_filename = file.replace(".csv", "") + "_utf8.csv"
     old_encoding = detect_encoding(file)
     df_no_utf8 = pd.read_csv(file, encoding=old_encoding)
     df_no_utf8.to_csv(new_filename, index=False, encoding='utf-8-sig')
     return new_filename

def format_csv(file):
     df = pd.read_csv(file)
     for column in df.columns:
          found = 0
          for new_title in column_mapping:
               if(column in column_mapping[new_title]):
                    df.rename(columns={column:new_title}, inplace=True)
                    found = 1
                    break
          if(not found):
               df = df.drop(column, axis=1)
     return df

def save_csv(df, new_filename):
     df.to_csv(new_filename, index=False)
