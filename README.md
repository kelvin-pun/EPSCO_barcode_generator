# EPSCO Barcode Generator

## Calculate the check digit and generate barcode for PPS

>Barcode symbology of Code 128 Set B is recommended. Code 128 is very high density alphanumeric barcode,though EPSCO barcode template uses numeric only. The X-dimension (the dimension of the narrowest element of barcode symbol) of 7.5 mils is recommended. 7.5 mils equal 0.0075 inch. Additional information about Code 128 is available e.g. at www.idautomation.com or www.barcodingfonts.com


**Example: 9999956002021312**
|     | code   | Description                            | width    |
| --- | ---    | ---                                    | ---      |
| A   | 9999   | Fixed Prefix assigned by EPSCO         | 4 digits | 
| B   | 111    | Merchant Code assigned by EPSCO        | 3 digits |
| C   | 00     | Bill Type assigned by merchant         | 2 digits |
| D   | 222222 | Bill Account No. Assigned by mechant   | 6 digits |
| E   | 2      | Check digit base on above barcode data | 1 digit  |

The validation algorithm will be as follows:
- Weights follow a 1,2,1,2…… pattern, start from right most digit of the bill account number
- Using 10 as Module
- The check digit will be [Module - MOD (Total sum of Digits, Module)]
- If MOD (Total sum of Digits, Module) = 0 then check digit is equal to 0

### Docker build and run
```bash
docker build -t epsco_barcode .
docker run -d --name my_epsco -p 80:80 epsco_barcode
```
