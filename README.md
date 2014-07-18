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
	_RFCReceptor_Fecha_RFCemisor_serie_folio_subtotal_iva_total_descuento_tipoComprobante_version.xml

Donde:
 * RFCReceptor: RFC de quien recibe el cfd/cfdi, es opcional y controlado por la opción -r
 * Fecha: Fecha en que se generó el comprobante
 * RFCemisor: RFC de quien emite el cfd/cfdi
 * Serie y Folio: Numero de Serie y folio de la factura
 * Subtotal, iva, total: Importes de la factura.
 * Descuento: Monto de descuento , es opcional y controlado por la opción -d
 * Tipo de comprobante: Ingreso/Egreso
 * Version: Version del CFDI



### TODO:
  * Separar los tipos de impuestos (IVA e ISR).

### CHANGE LOG

 17-07-2014 (@pixelead0)
 - FIXED:
   - Se arregla el IVA, en algunos XML el atributo 'totalImpuestosTrasladados' está vacío.
 - IMPLEMENT FEATURE:
   - Se agrega columna de 'DESCUENTO', para las compras que tienen descuentos, por ejemplo una compra en el super con promoción del 2x1.

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

### Ejemplos
```bash
$ python renamecfd.py -h
Usage: renamecfd.py [opciones] archivocfd.xml|*.xml

Options:
  -h, --help         muestra este mensaje de ayuda y termina
  -v, --verbose      Va mostrando la lista de los archivos modificados
  -r, --receptorrfc  Adiciona el rfc del receptor al inicio de cada nombre
  -d, --descuentos   Adiciona el monto de descuento del comprobante
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
Convierte todos los archivos con extensión xml en la carpeta actual y con la opción
-v muestra la lista de los archivos que ha convertido.

```bash
$ python renamecfd.py -r -v *.xml
archivo1.xml => rfcreceptor_fecha_rfc_etc.xml
archivo2.xml => rfcreceptor2_fecha2_rfc2_etc2.xml
...
$
```
Convierte todos los archivos con extensión xml en la carpeta actual, con la opción
-v muestra la lista de los archivos que ha convertido y con la opción -r adiciona al
inicio del nombre el rfc del receptor.

