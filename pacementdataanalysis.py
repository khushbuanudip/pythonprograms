Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/pythoninstallation/pdseries.py

================== RESTART: C:/pythoninstallation/pdseries.py ==================
0    10
1    20
2    30
3    40
4    50
dtype: int64

================ RESTART: C:/pythoninstallation/pandasseries2.py ===============
January      12000
February     13500
March        14200
April        12800
May          14000
June         15500
July         16200
August       15800
September    16500
October      17800
November     18500
December     17200
Name: Monthly Sales (USD), dtype: int64

================ RESTART: C:/pythoninstallation/pandasseries2.py ===============
January      12000
February     13500
March        14200
April        12800
May          14000
June         15500
July         16200
August       15800
September    16500
October      17800
November     18500
December     17200
Name: Monthly Sales (USD), dtype: int64

=================== RESTART: C:/pythoninstallation/readcsv.py ==================
Traceback (most recent call last):
  File "C:/pythoninstallation/readcsv.py", line 5, in <module>
    df = pd.DataFrame(data)
NameError: name 'pd' is not defined. Did you mean: 'id'?

=================== RESTART: C:/pythoninstallation/readcsv.py ==================
Traceback (most recent call last):
  File "C:/pythoninstallation/readcsv.py", line 1, in <module>
    import panda as pd
  File "C:\pythoninstallation\Lib\site-packages\panda\__init__.py", line 1, in <module>
    from request import PandaRequest
ModuleNotFoundError: No module named 'request'

=================== RESTART: C:/pythoninstallation/readcsv.py ==================
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
3    David   28      Houston

=================== RESTART: C:/pythoninstallation/readcsv.py ==================
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
3    David   28      Houston
After Adding Column
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
3    David   28      Houston

=================== RESTART: C:/pythoninstallation/readcsv.py ==================
Traceback (most recent call last):
  File "C:/pythoninstallation/readcsv.py", line 4, in <module>
    df = pd.DataFrame(data)
NameError: name 'pd' is not defined. Did you mean: 'id'?

=================== RESTART: C:/pythoninstallation/readcsv.py ==================
Initial DataFrame:
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
3    David   28      Houston

DataFrame after adding new columns:
      Name  Age         City  Gender Grade
0    Alice   25     New York  Female     A
1      Bob   30  Los Angeles    Male     B
2  Charlie   35      Chicago    Male     C
3    David   28      Houston    Male     B

=================== RESTART: C:/pythoninstallation/readcsv.py ==================
Initial DataFrame:
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
3    David   28      Houston

DataFrame after adding new columns:
      Name  Age         City  Gender Grade
0    Alice   25     New York  Female     A
1      Bob   30  Los Angeles    Male     B
2  Charlie   35      Chicago    Male     C
3    David   28      Houston    Male     B
Initial DataFrame:
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
3    David   28      Houston

DataFrame after adding the new column:
      Name  Gender  Age         City
0    Alice  Female   25     New York
1      Bob    Male   30  Los Angeles
2  Charlie    Male   35      Chicago
3    David    Male   28      Houston

================= RESTART: C:/pythoninstallation/addcolumndf.py ================
Initial DataFrame:
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
3    David   28      Houston

DataFrame after adding a new row:
      Name  Age           City
0    Alice   25       New York
1      Bob   30    Los Angeles
2  Charlie   35        Chicago
3    David   28        Houston
4      Eve   24  San Francisco
>>> 
============== RESTART: C:/pythoninstallation/changecolumnname.py ==============
Before Updating Column
        Fruit   Color  Price
0       Apple     Red     45
1     Avacado   Green     90
2      Banana  Yellow     60
3  Strawberry    Pink     37
4       Grape   Green     49
After Updating Column
   Fruit Name   Color  Price
0       Apple     Red     45
1     Avacado   Green     90
2      Banana  Yellow     60
3  Strawberry    Pink     37
4       Grape   Green     49
>>> 
Warning (from warnings module):
  File "C:/pythoninstallation/csvread.py", line 3
    csv_file_path = 'C:\pythoninstallation\customer_data.csv' # Replace with the actual path to your CSV file
SyntaxWarning: invalid escape sequence '\p'
>>> 
=================== RESTART: C:/pythoninstallation/csvread.py ==================
                 count           mean  ...          75%        max
Transaction_ID  2512.0  152443.931131  ...  153071.2500  153699.00
Age             2470.0      46.637652  ...      62.0000      78.00
Referal         2357.0       0.652100  ...       1.0000       1.00
Amount_spent    2270.0    1418.422577  ...    2038.1025    2999.98

[4 rows x 8 columns]
>>> 
======================================================= RESTART: C:/pythoninstallation/csvread.py =======================================================
 Mean of Age : 46.63765182186235
 Median of Age : 47.0
 Mode of Age : 54.0
 Standard deviation of Age : 18.19
 Maximum of Age : 78.0
 Minimum of Age : 15.0
