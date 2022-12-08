# EPSCO Barcode Generator
Calculate the check digit and generate barcode for PPS

>Barcode symbology of Code 128 Set B is recommended. Code 128 is very high density alphanumeric barcode,though EPSCO barcode template uses numeric only. The X-dimension (the dimension of the narrowest element of barcode symbol) of 7.5 mils is recommended. 7.5 mils equal 0.0075 inch. Additional information about Code 128 is available e.g. at www.idautomation.com or www.barcodingfonts.com


**Example: 9999956002021312**\
A. 9999    Fixed Prefix assigned by EPSCO         - 4 digits\
B. 956     Merchant Code assigned by EPSCO        - 3 digits\
C. 00      Bill Type assigned by merchant         - 2 digits\
D. 202131  Bill Account No. Assigned by mechant   - 6 digits\
E. 2       Check digit base on above barcode data - 1 digit\
