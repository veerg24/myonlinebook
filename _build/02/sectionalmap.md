---
interact_link: content/02/sectionalmap.ipynb
kernel_name: python3
has_widgets: false
title: 'Sectional Map'
prev_page:
  url: /02/histogram.html
  title: 'Histogram'
next_page:
  url: /02/timeseries.html
  title: 'Time Series'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Sectional Map Method



![](sectionalmap.png)



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
import numpy as np
import pandas as pd
import xarray as xr
import datetime as dt
from scipy.interpolate import griddata
import db
import subset
import common as com
import climatology as clim
from bokeh.io import output_notebook
from datetime import datetime, timedelta
import time
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.palettes import all_palettes
from bokeh.models import HoverTool, LinearColorMapper, BasicTicker, ColorBar
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
#TESTS NETCDF-COMPATIBLE FUNCTION
xFile = xr.open_dataset('http://3.88.71.225:80/thredds/dodsC/las/id-a1d60eba44/data_usr_local_tomcat_content_cbiomes_20190510_20_darwin_v0.2_cs510_darwin_v0.2_cs510_nutrients.nc.jnl')

tables = [xFile]    # see catalog.csv  for the complete list of tables and variable names
variabels = ['O2']                            # see catalog.csv  for the complete list of tables and variable name
dt1 = '2016-04-22'   # PISCES is a weekly model, and here we are using monthly climatology of Darwin model
dt2 = '2016-04-22'
lat1, lat2 = 23, 55
lon1, lon2 = -159, -157
depth1, depth2 = 0, 3597
fname = 'sectional'
exportDataFlag = False       # True if you you want to download data

xarraySectionMap(tables, variabels, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)

```
</div>

</div>

