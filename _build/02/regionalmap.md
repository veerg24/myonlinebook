---
interact_link: content/02/regionalmap.ipynb
kernel_name: python3
has_widgets: false
title: 'Regional Map'
prev_page:
  url: /02/query
  title: 'Data Query'
next_page:
  url: /02/histogram
  title: 'Histogram'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Regional Map Method



![](regionalmap.png)



### Import Functions



<div markdown="1" class="cell code_cell">
<div class="input_area hidecode" markdown="1">
```python
import sys
!{sys.executable} -m pip install netCDF4
!{sys.executable} -m pip install xarray
import opedia
import math
import common as com
from opedia import plotRegional as REG
import netCDF4
import xarray as xr
import numpy as np
from datetime import datetime
from dateutil.parser import parse
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.palettes import all_palettes
from bokeh.models import HoverTool, LinearColorMapper, BasicTicker, ColorBar, DatetimeTickFormatter
from bokeh.models.annotations import Title
from bokeh.embed import components
from tqdm import tqdm_notebook as tqdm
from netCDF4 import num2date, date2num
%run -i 'externalfunctions.py'

```
</div>

</div>



### Testing Space



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# NetCDF4 file(s) to read from:
xFile = xr.open_dataset('http://3.88.71.225:80/thredds/dodsC/las/id-a1d60eba44/data_usr_local_tomcat_content_cbiomes_20190510_20_darwin_v0.2_cs510_darwin_v0.2_cs510_nutrients.nc.jnl')

tables = [xFile]
variables = ['O2']
startDate = '2016-04-30'
endDate = '2017-04-30'
lat1, lat2 = -50, 90
lon1, lon2 = -100, 170
depth1, depth2 = 0, 50
fname = 'regional'
exportDataFlag = False

regionalMap(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)

```
</div>

</div>

