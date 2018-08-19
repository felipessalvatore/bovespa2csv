# bovespa2csv

[![Build Status](https://travis-ci.org/felipessalvatore/bovespa2csv.svg?branch=master)](https://travis-ci.org/felipessalvatore/bovespa2csv) [![License](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/felipessalvatore/bovespa2csv/blob/master/LICENSE)


## Introduction

This library was created to parse the txt files from [BM&FBOVESPA/B3 site](http://www.bmfbovespa.com.br/pt_br/servicos/market-data/historico/mercado-a-vista/series-historicas/) to a **csv file** or to an **excel file**.


### Install

The first thing you need to do is to install all the requirements by running:

```
$ pip3 install -r requirements.txt
```

## Usage

You can either use the script `parse_file.py` to create a csv file as follows:


```
  $ cd bovespa2csv 
  $ python3 parse_file.py <txt_file> example.csv
```


or to create a excel file:

```
  $ cd bovespa2csv 
  $ python3 parse_file.py -e <txt_file> example.xlsx
```

You can also use the class `BovespaParser` to get a pandas DataFrame from the txt file: 


```python
from BovespaParser import BovespaParser

parser = BovespaParser()
parser.read_txt("COTAHIST_DXXXXXX.TXT")
df = parser.df
```


## Built With

* [Pandas](https://pandas.pydata.org/)
* [XlsxWriter](https://xlsxwriter.readthedocs.io/)
