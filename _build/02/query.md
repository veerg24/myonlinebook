---
interact_link: content/02/query.ipynb
kernel_name: python3
has_widgets: false
title: 'Data Query'
prev_page:
  url: /02/llc90plottingexamples
  title: 'LLC90 Plotting Examples'
next_page:
  url: /02/regionalmap
  title: 'Regional Map'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


## Query Dataset



<div markdown="1" class="cell code_cell">
<div class="input_area hidecode" markdown="1">
```python
import sys
import os
import numpy as np
import pandas as pd
import xarray as xr
from pprint import pprint
from datetime import datetime

```
</div>

</div>



### Database (with Description)



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
database = xr.open_dataset('http://engaging-opendap.mit.edu:8080/thredds/dodsC/las/id-a1d60eba44/data_usr_local_tomcat_content_cbiomes_20190510_20_darwin_v0.2_cs510_darwin_v0.2_cs510_nutrients.nc.jnl')



```
</div>

</div>



### Fields/Dimensions



<div markdown="1" class="cell code_cell">
<div class="input_area hidecode" markdown="1">
```python
fields = list(database.keys())
dims = list(database.dims)

fields = pd.Series([fields], index = ['Fields'])
fields = pd.DataFrame({'Database Fields' : fields})
dims = pd.Series([dims], index = ['Dimensions'])
dims = pd.DataFrame({'Database Dimensions' : dims})

display(fields)
display(dims)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Database Fields</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Fields</th>
      <td>[FeT, PO4, DIN, SiO2, O2]</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Database Dimensions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Dimensions</th>
      <td>[DEP_C, LAT_C, LON_C, TIME]</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
</div>



**Fields**: Generally, the variables being measured <br>
**Dimensions**: What the variable is being measured over <br>

Example: Susie measured the amount of mayflies ( _field_ ) over time ( _dimension_ )



### Dimension Descriptions



<div markdown="1" class="cell code_cell">
<div class="input_area hidecode" markdown="1">
```python
#---_Time
timeStart = datetime.fromisoformat(database.TIME.attrs['start'])
timeEnd = datetime.fromisoformat(database.TIME.attrs['end'])
yearRange = timeEnd.year - timeStart.year
timeLogged = round( (yearRange * 365) / int(database.TIME.attrs['length']) )
#----Depth
depths = database.DEP_C.values
#----Lats/Lons
lats = database.LAT_C.values
lons = database.LON_C.values

#TIME
timeSeries = pd.Series([timeStart, timeEnd, database.TIME.attrs['length'], 'every ' + str(timeLogged) + ' days'], index = ['Start', 'End', 'Length', 'Data Logged'])
majorTable = pd.DataFrame({'TIME Values' : timeSeries})

#DEPTH
depthSeries = pd.Series([database.DEP_C.attrs['start'], database.DEP_C.attrs['end'], database.DEP_C.attrs['length'], database.DEP_C.values], index = ['Start', 'End', 'Length', 'Depth List'])
majorTable['DEPTH(m) Values'] = depthSeries

#LATITUDE
latSeries = pd.Series([database.LAT_C.attrs['start'], database.LAT_C.attrs['end'], database.LAT_C.attrs['length']], index = ['Start', 'End', 'Length'])
majorTable['LATITUDE Values'] = latSeries

#LONGITUDE
lonSeries = pd.Series([database.LON_C.attrs['start'], database.LON_C.attrs['end'], database.LON_C.attrs['length']], index = ['Start', 'End', 'Length'])
majorTable['LONGITUDE Values'] = lonSeries

display(majorTable)
pd.set_option('display.max_colwidth', abs(int(database.DEP_C.attrs['end'])))

depths = pd.Series([depths], index = ['Depths List'])
depths = pd.DataFrame({'Depth List' : depths})
display(depths)
pd.set_option('display.max_colwidth', 100)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TIME Values</th>
      <th>DEPTH(m) Values</th>
      <th>LATITUDE Values</th>
      <th>LONGITUDE Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Start</th>
      <td>1992-01-02 12:00:00</td>
      <td>5</td>
      <td>-89.75</td>
      <td>-179.75</td>
    </tr>
    <tr>
      <th>End</th>
      <td>2016-08-20 12:00:00</td>
      <td>5906.25</td>
      <td>89.75</td>
      <td>179.75</td>
    </tr>
    <tr>
      <th>Length</th>
      <td>3000</td>
      <td>50</td>
      <td>360.00</td>
      <td>720.00</td>
    </tr>
    <tr>
      <th>Data Logged</th>
      <td>every 3 days</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Depth List</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Depths List</th>
      <td>[5.0, 15.0, 25.0, 35.0, 45.0, 55.0, 65.0, 75.004997253418, 85.0250015258789, 95.0950012207031, 105.309997558594, 115.870002746582, 127.150001525879, 139.740005493164, 154.470001220703, 172.399993896484, 194.735000610352, 222.710006713867, 257.470001220703, 299.929992675781, 350.679992675781, 409.929992675781, 477.470001220703, 552.710021972656, 634.734985351563, 722.400024414063, 814.469970703125, 909.739990234375, 1007.15502929688, 1105.90502929688, 1205.53503417969, 1306.20495605469, 1409.15002441406, 1517.09497070313, 1634.17504882813, 1765.13500976563, 1914.15002441406, 2084.03491210938, 2276.22509765625, 2491.25, 2729.25, 2990.25, 3274.25, 3581.25, 3911.25, 4264.25, 4640.25, 5039.25, 5461.25, 5906.25]</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
</div>



 **Definitions** <br>
**Start**: value the dimension begins at EX: (**_1_**, 2, 3...) <br>
**End**: values the dimension ends with  EX: (...4, 5, **_6_**) <br>
**Length**: amount of items in dimensions EX: (the length of the alphabet is **26**) <br>
**Data Logged**: amount of time between each data log EX: (time data is logged every _**x**_ days) <br>
**Depth List**: list of all logged depths in the database EX: (**30 meters, 40 meters, etc**)



### Field Descriptions



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
field = database.variables['O2'] #field to describe

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area hidecode" markdown="1">
```python

#Attributes 
fieldTable = pd.Series([field.dims, field.attrs['units'], field.attrs['infile_datatype'], field.attrs['direction'], field.attrs['dataset_index']], index = ['Dimensions', 'Units', 'Datatype', 'Direction', 'Dataset Index'])
fieldTable = pd.DataFrame({str(field.attrs['long_name']) : fieldTable})
display(fieldTable)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>O2 concentration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Dimensions</th>
      <td>(TIME, DEP_C, LAT_C, LON_C)</td>
    </tr>
    <tr>
      <th>Units</th>
      <td>mmol O/m^3</td>
    </tr>
    <tr>
      <th>Datatype</th>
      <td>FLOAT</td>
    </tr>
    <tr>
      <th>Direction</th>
      <td>IJKL</td>
    </tr>
    <tr>
      <th>Dataset Index</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
</div>



A description of the **variable's** attributes. To describe a variable of your choosing, enter the field name in the "database.variables['< YOUR FIELD HERE >']" space

