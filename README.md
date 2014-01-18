###############################################################################
#
# RENAMECFD - Renombra archivos de CFD
# Autor: Ricardo Torres
# email: rictor@cuhrt.com
# blog: htpp://rctorr.wordpress.com
# twitter: @rctorr
#
# Descripción
# Este script leer un CFD con nombre archivo.xml para después renombrarlo
# de la siguiente manera:
#    Fecha_RFCemisor_serie_folio_subtotal_iva_total.xml
#
# Fecha: Fecha en que se generó el comprobante
# RFCemisor: RFC de quien emite el cfd/cfdi
# Serie y Folio: Numero de Serie y folio de la factura
# Subtotal, iva, total: Importes de la factura.
#
# El nombre del xml se proporciona desde la línea de comandos, de tal forma que
# se puede usar en algún otro script para automatizar el proceso.
#
# Se permite indicar archivos con algún path distinto a donde se encuentra el
# script
#
# Se aceptan comodines para procesar grupos de archivos
#
# Puede leer tanto archivos xml correspondientes a CFD y CFDi
# 
###############################################################################

