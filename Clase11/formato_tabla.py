class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
        
class FormatoTablaTXT(FormatoTabla):
   '''
   Generar una tabla en formato TXT
   '''
   def encabezado(self, headers):
       for h in headers:
           print(f'{h:>10s}', end=' ')
       print()
       print(('-'*10 + ' ')*len(headers))

   def fila(self, data_fila):
       for d in data_fila:
           print(f'{d:>10s}', end=' ')
       print()
       
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
class FormatoTablaHTML(FormatoTabla):
    '''
    Generaar unaa tabla en formato HTTML
    '''
    def encabezado(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')
    
    def fila(self, data_fila):
        print('<tr>', end='')
        for d in data_fila:
            print(f'<th>{d}</th>', end='')
        print('</tr>')
    
def crear_formateador(fmt):
    ''''
    Creo formato de salida segun indique el usuario
    '''
    if fmt == 'txt':
        return FormatoTablaTXT() # Formato TXT
    elif fmt == 'csv':
        return FormatoTablaCSV() # Formato CSV
    elif fmt == 'html':
        return FormatoTablaHTML() # Formato HTML
    else:
        raise RuntimeError(f'que es "{fmt}" chinchulin')

