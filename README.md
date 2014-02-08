RENAMECFD - Renombra archivos de CFD
------------------------------------
Autor: *Ricardo Torres*
email: *[rictor@cuhrt.com](mailto:rictor@cuhrt.com)*
blog: *[http://rctorr.wordpress.com](http://rctorr.wordpress.com)*
twitter: *[@rctorr](http://www.twitter.com/rctorr)*

### Descripción
Este script lee un CFD con nombre archivo.xml para después renombrarlo
de la siguiente manera:
   _RFCReceptor_Fecha_RFCemisor_serie_folio_subtotal_iva_total.xml

Donde:
 * RFCReceptor: RFC de quien recibe el cfd/cfdi, es opcional y controlado por la opción -r
 * Fecha: Fecha en que se generó el comprobante
 * RFCemisor: RFC de quien emite el cfd/cfdi
 * Serie y Folio: Numero de Serie y folio de la factura
 * Subtotal, iva, total: Importes de la factura.

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

