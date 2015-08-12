RENAMECFD - Renombra archivos de CFD/CFDI
------------------------------------
Autor: *Ricardo Torres*
email: *[rictor@cuhrt.com](mailto:rictor@cuhrt.com)*
blog: *[http://rctorr.wordpress.com](http://rctorr.wordpress.com)*
twitter: *[@rctorr](http://www.twitter.com/rctorr)*

Autor: *@pixelead0*
email: *[adangq@gmail.com](mailto:adangq@gmail.com)*
blog: *[http://pixelead0.blogspot.com](http://pixelead0.blogspot.com)*
twitter: *[@pixelead0](http://www.twitter.com/pixelead0)*



### Descripción
Este script lee un CFD/CFDI con nombre archivo.xml para después renombrarlo
de la siguiente manera:
	_RFCReceptor_Fecha_RFCemisor_serie_folio_subtotal_iva_total_descuento_tipoComprobante_version_UUID.xml

Donde:
 * RFCReceptor: RFC de quien recibe el cfd/cfdi, es opcional y controlado por la opción -r
 * Fecha: Fecha en que se generó el comprobante
 * RFCemisor: RFC de quien emite el cfd/cfdi
 * Serie y Folio: Numero de Serie y folio de la factura
 * Subtotal, iva, total: Importes de la factura.
 * Descuento: Monto de descuento , es opcional y controlado por la opción -d
 * Tipo de comprobante: Ingreso/Egreso
 * Version: Version del CFDI
 * UUID: Es el folio obtenido por el timbrado (opcional con la opción -U o --UUID)


### TO DO:
  * Separar los tipos de impuestos (IVA e ISR).

### CHANGE LOG

 12-08-2015 (@rctorr)
 - Agregando campo del UUID por solicitud de usuarios
 
 17-07-2014 (@pixelead0)
 - FIXED:
   - Se arregla el IVA, en algunos XML el atributo 'totalImpuestosTrasladados' está vacío.
 - IMPLEMENT FEATURE:
   - Se agrega parametro opcional para mostrar la columna de 'DESCUENTO', para las compras que tienen descuentos, por ejemplo una compra en el super con promoción del 2x1.
   - Se agrega parametro opcional para exportar resultados en un archivo .csv

 25-02-2014 (@pixelead0)
 - FIXES:
   - Si no existe serie y folio, se dejan los campos vacios.
   - Se valida el tipo de comprobante; si es 'egreso' los importes se dejan en negativos
   - Se agrega el campo hora
   - Se valida que el archivo final no exista.
   - Si existe un pdf con el mismo nombre que el XML se renombran ambos archivos.

 17-01-2014
 - Ahora permite indicar archivos con algún path distinto a donde está el
   script

 16-01-2014
 - Se modifica para que pueda ser utilizado en batch y haceptar comodines
   en el nombre de archivo

 Ver 1.1
 - Se corrige problema con los tags para cfdi

 Ver 1.0
 - Se lee el nombre del archivo desde la línea de comando
 - Se leer los atributos del archivo xml
 - Genera el nombre con la sintaxis solicitada
 - Renombra el archivo xml al nuevo nombre


### FEATURES

El nombre del xml se proporciona desde la línea de comandos, de tal forma que
se puede usar en algún otro script para automatizar el proceso.

Se permite indicar archivos con algún path distinto a donde se encuentra el
script

Se aceptan comodines para procesar grupos de archivos

Puede leer tanto archivos xml correspondientes a CFD y CFDi

Ejecutar cuando menos una ves con -h ya que se están agregando nuevas opciones.

### Ejemplos
```bash
$ python renamecfd.py -h
Usage: renamecfd.py [opciones] archivocfd.xml|*.xml

Options:
  -h, --help         muestra este mensaje de ayuda y termina
  -v, --verbose      Va mostrando la lista de los archivos modificados
  -r, --receptorrfc  Adiciona el rfc del receptor al inicio de cada nombre
  -d, --descuentos   Adiciona el monto de descuento del comprobante
  -o archivoSalida.csv, --output=archivoSalida.csv
                        Guarda reporte en archivo csv
```
Muestra la ayuda

```bash
$ python renamecfd.py *.xml
$
```
Renombra todos los archivos con extensión xml contenido en la misma carpeta que el programa

```bash
$ python renamecfd.py /home/user/facturas/*.xml
$
```
Renombra todos los archivos con extensión xml ubicados en la carpeta
/home/user/facturas

```bash
$ python renamecfd.py -v *.xml
archivo1.xml => fecha_rfc_etc.xml
archivo2.xml => fecha2_rfc2_etc2.xml
...
$
```
Convierte todos los archivos con extensión xml en la carpeta actual

Con la opción -v muestra la lista de los archivos que ha convertido.

```bash
$ python renamecfd.py -r -v *.xml
archivo1.xml => rfcreceptor_fecha_rfc_etc.xml
archivo2.xml => rfcreceptor2_fecha2_rfc2_etc2.xml
...
$
```
Convierte todos los archivos con extensión xml en la carpeta actual,

con la opción -v muestra la lista de los archivos que ha convertido.

con la opción -r adiciona al inicio del nombre el rfc del receptor.


```bash
$ python renamecfd.py -r -d -o reporte.csv *.xml
archivo1.xml => rfcreceptor_fecha_rfc_etc.xml
archivo2.xml => rfcreceptor2_fecha2_rfc2_etc2.xml
...
$
```
Convierte todos los archivos con extensión xml en la carpeta actual,

Con la opción -r adiciona al inicio del nombre el rfc del receptor.

Con la opción -d adiciona importe de descuento despues del subtotal.

Con la opción -o reporte.csv genera archivo CSV.

```
rfcreceptor,fecha,rfc,etc
rfcreceptor2,fecha2,rfc2,etc2
...
...
```

```bash
$ python renamecfd.py -U -v TORR711730TE5FA0000009253.xml 
TORR711730TE5FA0000009253.xml => _2014-09-11_195302_OCC911023NT7_A_9253_145.69_23.31_169.00_ingreso_3.2_E7F30F1C-5E41-4D44-B751-971746C3BDAE_.xml
$
```
Renombra el archivo indicado, pero con la opción -U agrega al final
del nombre del archivo el UUID obtenido por el timbrado.

