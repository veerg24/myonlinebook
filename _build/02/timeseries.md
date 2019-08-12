---
interact_link: content/02/timeseries.ipynb
kernel_name: python3
has_widgets: false
title: 'Time Series'
prev_page:
  url: /02/sectionalmap
  title: 'Sectional Map'
next_page:
  url: /02/xyplot
  title: 'XY plot'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Time Series Method



![](timeseries.png)



### Import Functions



<div markdown="1" class="cell code_cell">
<div class="input_area hidecode" markdown="1">
```python
import sys
!{sys.executable} -m pip install netCDF4
!{sys.executable} -m pip install xarray
import opedia
import netCDF4
import os
import json
import xarray as xr
from datetime import datetime
from netCDF4 import num2date, date2num
import numpy as np
import pandas as pd
import db
import common as com
import timeSeries as TS
from datetime import datetime, timedelta
import time
from math import pi
from bokeh.io import output_notebook
from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.models import DatetimeTickFormatter
from bokeh.palettes import all_palettes
from bokeh.models import HoverTool
from bokeh.embed import components
import jupyterInline as jup
if jup.jupytered():
    from tqdm import tqdm_notebook as tqdm
else:
    from tqdm import tqdm
%run -i 'externalfunctions.py'

```
</div>

</div>



### Testing Space



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#TESTS XARRAY IMPLEMENTATION

xFile = xr.open_dataset('http://3.88.71.225:80/thredds/dodsC/las/id-a1d60eba44/data_usr_local_tomcat_content_cbiomes_20190510_20_darwin_v0.2_cs510_darwin_v0.2_cs510_nutrients.nc.jnl')

tables = [xFile]    # see catalog.csv  for the complete list of tables and variable names
variables = ['O2']                                        # see catalog.csv  for the complete list of tables and variable names
startDate = '2000-12-31'
endDate = '2001-12-31'
lat1, lat2 = 25, 30
lon1, lon2 = -160, -155
depth1, depth2 = 0, 10
fname = 'TS'
exportDataFlag = False      # True if you you want to download data

plotTSX(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)

```
</div>

</div>

