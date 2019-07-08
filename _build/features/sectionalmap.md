---
interact_link: content/features/sectionalmap.ipynb
kernel_name: python3
has_widgets: false
title: 'Sectional Map'
prev_page:
  url: /features/histogram
  title: 'Histogram'
next_page:
  url: /features/features
  title: 'Features'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


## Reformat NetCDF4 File for Function Call



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import opedia
import sys
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

```
</div>

</div>



### Testing Space



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#THIS TESTS THE ORIGINAL SECTIONAL FUNCTION

tables = ['tblDarwin_Nutrient_Climatology']    # see catalog.csv  for the complete list of tables and variable names
variabels = ['CDOM_darwin_clim']                            # see catalog.csv  for the complete list of tables and variable names

dt1 = '2016-04-30'   # PISCES is a weekly model, and here we are using monthly climatology of Darwin model
dt2 = '2016-04-30'
lat1, lat2 = 23, 55
lon1, lon2 = -159, -157
depth1, depth2 = 0, 3597
fname = 'sectional'
exportDataFlag = False       # True if you you want to download data

sectionMap(tables, variabels, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_data_text}
```
HBox(children=(IntProgress(value=0, description='overall', max=1, style=ProgressStyle(description_width='initi…
```

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1: CDOM_darwin_clim retrieved (tblDarwin_Nutrient_Climatology).
[0m------------------Times:
[4]
------------------Lats:
[23.25 23.75 24.25 24.75 25.25 25.75 26.25 26.75 27.25 27.75 28.25 28.75
 29.25 29.75 30.25 30.75 31.25 31.75 32.25 32.75 33.25 33.75 34.25 34.75
 35.25 35.75 36.25 36.75 37.25 37.75 38.25 38.75 39.25 39.75 40.25 40.75
 41.25 41.75 42.25 42.75 43.25 43.75 44.25 44.75 45.25 45.75 46.25 46.75
 47.25 47.75 48.25 48.75 49.25 49.75 50.25 50.75 51.25 51.75 52.25 52.75
 53.25 53.75 54.25 54.75]
------------------Lons:
[-158.75 -158.25 -157.75 -157.25]
------------------Depths:
[3581.25  3274.25  2990.25  2729.25  2491.25  2276.225 2084.035 1914.15
 1765.135 1634.175 1517.095 1409.15  1306.205 1205.535 1105.905 1007.155
  909.74   814.47   722.4    634.735  552.71   477.47   409.93   350.68
  299.93   257.47   222.71   194.735  172.4    154.47   139.74   127.15
  115.87   105.31    95.095   85.025   75.005   65.      55.      45.
   35.      25.      15.       5.   ]
[None]

[array([[[6.8717864e-06, 8.8437350e-06, 1.1581308e-05, ...,
         2.4946356e-05, 2.5531384e-05, 2.5630745e-05],
        [6.8319710e-06, 8.7574620e-06, 1.1432205e-05, ...,
         2.5309380e-05, 2.5913885e-05, 2.6015790e-05],
        [6.7323062e-06, 8.6646520e-06, 1.1285433e-05, ...,
         2.5821144e-05, 2.6483263e-05, 2.6606067e-05],
        [6.6369220e-06, 8.5737590e-06, 1.1150599e-05, ...,
         2.5968282e-05, 2.6611655e-05, 2.6733394e-05]],

       [[6.8761715e-06, 8.9284940e-06, 1.1621626e-05, ...,
         2.3032475e-05, 2.3415081e-05, 2.3505352e-05],
        [6.8337026e-06, 8.8479850e-06, 1.1510043e-05, ...,
         2.3282142e-05, 2.3693245e-05, 2.3788010e-05],
        [6.7609640e-06, 8.7622675e-06, 1.1389939e-05, ...,
         2.3559707e-05, 2.4011912e-05, 2.4117560e-05],
        [6.6872640e-06, 8.6790970e-06, 1.1272472e-05, ...,
         2.3688563e-05, 2.4146691e-05, 2.4252735e-05]],

       [[6.9827100e-06, 9.1137745e-06, 1.1840825e-05, ...,
         2.1143130e-05, 2.1403635e-05, 2.1481272e-05],
        [6.9335356e-06, 9.0356350e-06, 1.1738929e-05, ...,
         2.1311229e-05, 2.1590713e-05, 2.1672267e-05],
        [6.8654520e-06, 8.9537420e-06, 1.1626759e-05, ...,
         2.1482761e-05, 2.1783782e-05, 2.1871423e-05],
        [6.7966835e-06, 8.8732860e-06, 1.1515997e-05, ...,
         2.1587772e-05, 2.1892850e-05, 2.1981203e-05]],

       ...,

       [[2.4745566e-05, 3.1973454e-05, 4.1437404e-05, ...,
         1.2241026e-03, 1.2088884e-03, 1.2045271e-03],
        [2.4887651e-05, 3.2035037e-05, 4.1505285e-05, ...,
         1.2256880e-03, 1.2100849e-03, 1.2056433e-03],
        [2.5035342e-05, 3.1961634e-05, 4.1381278e-05, ...,
         1.2296783e-03, 1.2138510e-03, 1.2094046e-03],
        [2.5148449e-05, 3.1911088e-05, 4.1244282e-05, ...,
         1.2337800e-03, 1.2179590e-03, 1.2135955e-03]],

       [[2.4980576e-05, 3.2223892e-05, 4.1711133e-05, ...,
         1.1963627e-03, 1.1823146e-03, 1.1784420e-03],
        [2.5178548e-05, 3.2314223e-05, 4.1811574e-05, ...,
         1.1971928e-03, 1.1821620e-03, 1.1777933e-03],
        [2.5367926e-05, 3.2219108e-05, 4.1658008e-05, ...,
         1.2037051e-03, 1.1882413e-03, 1.1836630e-03],
        [2.5654725e-05, 3.2218046e-05, 4.1491630e-05, ...,
         1.2101186e-03, 1.1943401e-03, 1.1896730e-03]],

       [[          nan,           nan,           nan, ...,
         1.1783360e-03, 1.1795750e-03, 1.1761963e-03],
        [          nan,           nan,           nan, ...,
         1.1773405e-03, 1.1657276e-03, 1.1619234e-03],
        [          nan,           nan,           nan, ...,
         1.1822752e-03, 1.1691484e-03, 1.1652291e-03],
        [2.6309608e-05, 3.2503383e-05, 4.1516127e-05, ...,
         1.1870101e-03, 1.1727276e-03, 1.1686694e-03]]])]
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#TESTS NETCDF-COMPATIBLE FUNCTION
xFile = xr.open_dataset('http://engaging-opendap.mit.edu:8080/thredds/dodsC/las/id-a1d60eba44/data_usr_local_tomcat_content_cbiomes_20190510_20_darwin_v0.2_cs510_darwin_v0.2_cs510_nutrients.nc.jnl')

tables = [xFile]    # see catalog.csv  for the complete list of tables and variable names
variabels = ['O2']                            # see catalog.csv  for the complete list of tables and variable name
dt1 = '2016-04-21'   # PISCES is a weekly model, and here we are using monthly climatology of Darwin model
dt2 = '2016-04-23'
lat1, lat2 = 23, 55
lon1, lon2 = -159, -157
depth1, depth2 = 0, 3597
fname = 'sectional'
exportDataFlag = False       # True if you you want to download data

xarraySectionMap(tables, variabels, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_data_text}
```
HBox(children=(IntProgress(value=0, description='overall', max=1, style=ProgressStyle(description_width='initi…
```

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
------------------Times:
['2016-04-22T12:00:00.000000000']
------------------Lats:
[23.25 23.75 24.25 24.75 25.25 25.75 26.25 26.75 27.25 27.75 28.25 28.75
 29.25 29.75 30.25 30.75 31.25 31.75 32.25 32.75 33.25 33.75 34.25 34.75
 35.25 35.75 36.25 36.75 37.25 37.75 38.25 38.75 39.25 39.75 40.25 40.75
 41.25 41.75 42.25 42.75 43.25 43.75 44.25 44.75 45.25 45.75 46.25 46.75
 47.25 47.75 48.25 48.75 49.25 49.75 50.25 50.75 51.25 51.75 52.25 52.75
 53.25 53.75 54.25 54.75]
------------------Lons:
[-158.75 -158.25 -157.75 -157.25]
------------------Depths:
[   5.           15.           25.           35.           45.
   55.           65.           75.00499725   85.02500153   95.09500122
  105.30999756  115.87000275  127.15000153  139.74000549  154.47000122
  172.3999939   194.73500061  222.71000671  257.47000122  299.92999268
  350.67999268  409.92999268  477.47000122  552.71002197  634.73498535
  722.40002441  814.4699707   909.73999023 1007.1550293  1105.9050293
 1205.53503418 1306.20495605 1409.15002441 1517.0949707  1634.17504883
 1765.13500977 1914.15002441 2084.03491211 2276.22509766 2491.25
 2729.25       2990.25       3274.25       3581.25      ]

[array([[[217.72581 , 216.81123 , 214.0529  , ..., 230.42786 ,
         229.17262 , 231.33789 ],
        [233.9318  , 234.01979 , 231.77782 , ..., 266.105   ,
         266.24622 , 272.6455  ],
        [271.14008 , 267.5709  , 270.03146 , ..., 291.15668 ,
         289.13187 , 286.4821  ],
        [293.4539  , 290.29108 , 288.36252 , ..., 317.2291  ,
         316.32886 , 314.52707 ]],

       [[317.17874 , 315.7166  , 314.08313 , ..., 325.32346 ,
         325.19644 , 324.50272 ],
        [324.8363  , 324.9312  , 323.8824  , ..., 218.6293  ,
         216.3647  , 214.4391  ],
        [218.26263 , 220.42119 , 218.32784 , ..., 247.69958 ,
         236.04405 , 233.75935 ],
        [242.77306 , 244.85489 , 251.91418 , ..., 269.25162 ,
         270.12946 , 274.0666  ]],

       [[276.8333  , 274.2667  , 274.4905  , ..., 289.88556 ,
         289.83417 , 289.1105  ],
        [293.06216 , 291.07034 , 290.4885  , ..., 316.25833 ,
         313.7674  , 312.94287 ],
        [317.34076 , 317.73276 , 318.027   , ..., 323.91815 ,
         323.8229  , 323.13007 ],
        [325.03622 , 324.5677  , 324.23425 , ..., 223.38698 ,
         221.38574 , 215.03766 ]],

       ...,

       [[118.56813 , 122.07851 , 124.37722 , ..., 138.89113 ,
         138.28128 , 138.15404 ],
        [138.55788 , 138.34163 , 137.74638 , ..., 133.62332 ,
         132.74957 , 133.28917 ],
        [132.97987 , 132.95703 , 132.69957 , ..., 129.67747 ,
         128.99763 , 130.27586 ],
        [131.3726  , 130.79448 , 131.56548 , ..., 124.89965 ,
         126.59851 , 125.47857 ]],

       [[125.57555 , 125.44564 , 125.426025, ..., 127.749275,
         127.31362 , 127.262085],
        [127.70962 , 127.40387 , 126.59454 , ..., 125.88385 ,
         129.53844 , 133.18211 ],
        [125.24015 , 129.04002 , 129.05605 , ..., 145.91988 ,
         144.16055 , 143.67812 ],
        [145.19058 , 144.38684 , 143.67772 , ..., 141.33304 ,
         141.07362 , 141.54594 ]],

       [[140.71703 , 141.06773 , 141.67303 , ..., 139.8576  ,
         139.12973 , 138.6735  ],
        [139.78937 , 139.35306 , 138.66321 , ..., 135.03003 ,
         134.89113 , 134.96988 ],
        [134.81976 , 135.67053 , 135.26762 , ..., 135.24072 ,
         135.11833 , 134.84845 ],
        [136.04054 , 136.10843 , 135.20757 , ...,        nan,
                nan,        nan]]], dtype=float32)]
low: 
213.64651
low: 213.64651
high: 317.2291
```
</div>
</div>
</div>



### Original Function



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sectionMap(tables, variabels, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag):
    data, lats, lons, subs, frameVars, units = [], [], [], [], [], []
    xs, ys, zs = [], [], []
    for i in tqdm(range(len(tables)), desc='overall'):
        if not db.hasField(tables[i], 'depth'):
            continue        
        df = subset.section(tables[i], variabels[i], dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)
        if len(df) < 1:
            com.printTQDM('%d: No matching entry found: Table: %s, Variable: %s ' % (i+1, tables[i], variabels[i]), err=True )
            continue
        com.printTQDM('%d: %s retrieved (%s).' % (i+1, variabels[i], tables[i]), err=False)

        ############### export retrieved data ###############
        if exportDataFlag:      # export data
            dirPath = 'data/'
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)                
            exportData(df, path=dirPath + fname + '_' + tables[i] + '_' + variabels[i] + '.csv')
        #####################################################

        times = df[df.columns[0]].unique()
        lats = df.lat.unique()
        lons = df.lon.unique()
        depths = df.depth.unique()
        shape = (len(lats), len(lons), len(depths))
        
        print('------------------Times:')
        print(times)
        print('------------------Lats:')
        print(lats)
        print('------------------Lons:')
        print(lons)
        print('------------------Depths:')
        print(depths)

        hours =  [None]
        if 'hour' in df.columns:
            hours = df.hour.unique()

        unit = com.getUnit(tables[i], variabels[i])
        
        print(hours)

        for t in times:
            for h in hours:
                frame = df[df[df.columns[0]] == t]
                sub = variabels[i] + unit + ', ' + df.columns[0] + ': ' + str(t) 
                if h != None:
                    frame = frame[frame['hour'] == h]
                    sub = sub + ', hour: ' + str(h) + 'hr'
                try:    
                    shot = frame[variabels[i]].values.reshape(shape)
                except Exception as e:
                    continue    
                data.append(shot)
                
                xs.append(lons)
                ys.append(lats)
                zs.append(depths)

                frameVars.append(variabels[i])
                units.append(unit)
                subs.append(sub)
                
    print(data)            
    bokehSec(data=data, subject=subs, fname=fname, ys=ys, xs=xs, zs=zs, units=units, variabels=frameVars)
    return

```
</div>

</div>



### NetCDF Compatible Function



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def xarraySectionMap(tables, variabels, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag):
    data, lats, lons, subs, frameVars, units = [], [], [], [], [], []
    xs, ys, zs = [], [], []
    for i in tqdm(range(len(tables)), desc='overall'):
        
        toDateTime = tables[i].indexes['TIME'].to_datetimeindex()
        tables[i]['TIME'] = toDateTime
        table = tables[i].sel(TIME = slice(dt1, dt2), LAT_C = slice(lat1, lat2), LON_C = slice(lon1, lon2), DEP_C = slice(depth1, depth2))
        ############### export retrieved data ###############
        if exportDataFlag:      # export data
            dirPath = 'data/'
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)                
            exportData(df, path=dirPath + fname + '_' + tables[i] + '_' + variabels[i] + '.csv')
        #####################################################

        times = np.unique(table.variables['TIME'].values)
        lats = np.unique(table.variables['LAT_C'].values)
        lons = np.unique(table.variables['LON_C'].values)
        depths = np.unique(table.variables['DEP_C'].values)
        shape = (len(lats), len(lons), len(depths))
        
        hours = [None]

        unit = '[PLACEHOLDER]'

        for t in times:
            for h in hours:
                frame = table.sel(TIME = t, method = 'nearest')
                sub = variabels[i] + unit + ', TIME: ' + str(t) 
                if h != None:
                    frame = frame[frame['hour'] == h]
                    sub = sub + ', hour: ' + str(h) + 'hr'
                try:    
                    shot = frame[variabels[i]].values.reshape(shape)
                    shot[shot < 0] = float('NaN')
                except Exception as e:
                    continue    
                data.append(shot)
                
                xs.append(lons)
                ys.append(lats)
                zs.append(depths)

                frameVars.append(variabels[i])
                units.append(unit)
                subs.append(sub)
    
    print(data)
    bokehSec(data=data, subject=subs, fname=fname, ys=ys, xs=xs, zs=zs, units=units, variabels=frameVars)
    return

```
</div>

</div>



### Helper Functions



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def bokehSec(data, subject, fname, ys, xs, zs, units, variabels):
    TOOLS="crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
    w = 1000
    h = 500
    p = []
    data_org = list(data)
    for ind in range(len(data_org)):
        data = data_org[ind]
        lon = xs[ind]
        lat = ys[ind]
        depth = zs[ind]      
        
        bounds = (None, None)
        paletteName = com.getPalette(variabels[ind], 10)
        low, high = bounds[0], bounds[1]
        if low == None:
            print("low: ")
            print(np.min(data[ind]))
            low, high = np.nanmin(data[ind].flatten()), np.nanmax(data[ind].flatten())
        color_mapper = LinearColorMapper(palette=paletteName, low=low, high=high)
        
        print("low: " + str(low))
        print("high: " + str(high))
        
        if len(lon) > len(lat):
            p1 = figure(tools=TOOLS, toolbar_location="above", title=subject[ind], plot_width=w, plot_height=h, x_range=(np.min(lon), np.max(lon)), y_range=(-np.max(depth), -np.min(depth)))
            data = np.nanmean(data, axis=0)
            data = np.transpose(data)
            data = np.squeeze(data)
            xLabel = 'Longitude'
            data = regulate(lat, lon, depth, data)
            p1.image(image=[data], color_mapper=color_mapper, x=np.min(lon), y=-np.max(depth), dw=np.max(lon)-np.min(lon), dh=np.max(depth)-np.min(depth))
        else:
            p1 = figure(tools=TOOLS, toolbar_location="above", title=subject[ind], plot_width=w, plot_height=h, x_range=(np.min(lat), np.max(lat)), y_range=(-np.max(depth), -np.min(depth)))
            data = np.nanmean(data, axis=1)
            data = np.transpose(data)
            data = np.squeeze(data)
            xLabel = 'Latitude'      
            data = regulate(lat, lon, depth, data)
            p1.image(image=[data], color_mapper=color_mapper, x=np.min(lat), y=-np.max(depth), dw=np.max(lat)-np.min(lat), dh=np.max(depth)-np.min(depth))

        p1.xaxis.axis_label = xLabel
        p1.add_tools(HoverTool(
            tooltips=[
                (xLabel.lower(), '$x'),
                ('depth', '$y'),
                (variabels[ind]+units[ind], '@image'),
            ],
            mode='mouse'
        ))

        p1.yaxis.axis_label = 'depth [m]'
        color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                        label_standoff=12, border_line_color=None, location=(0,0))
        p1.add_layout(color_bar, 'right')
        p.append(p1)
    dirPath = 'embed/'
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)        
   # if not inline:      ## if jupyter is not the caller
   #     output_file(dirPath + fname + ".html", title="Section Map")
    show(column(p))
    return

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def regulate(lat, lon, depth, data):
    depth = -1* depth 
    deltaZ = np.min( np.abs( depth - np.roll(depth, -1) ) )
    newDepth =  np.arange(np.min(depth), np.max(depth), deltaZ)        

    if len(lon) > len(lat):
        lon1, depth1 = np.meshgrid(lon, depth)
        lon2, depth2 = np.meshgrid(lon, newDepth)
        lon1 = lon1.ravel()
        lon1 = list(lon1[lon1 != np.isnan])
        depth1 = depth1.ravel()
        depth1 = list(depth1[depth1 != np.isnan])
        data = data.ravel()
        data = list(data[data != np.isnan])
        data = griddata((lon1, depth1), data, (lon2, depth2), method='linear')
    else:   
        lat1, depth1 = np.meshgrid(lat, depth)
        lat2, depth2 = np.meshgrid(lat, newDepth)
        lat1 = lat1.ravel()
        lat1 = list(lat1[lat1 != np.isnan])
        depth1 = depth1.ravel()
        depth1 = list(depth1[depth1 != np.isnan])
        data = data.ravel()
        data = list(data[data != np.isnan])
        data = griddata((lat1, depth1), data, (lat2, depth2), method='linear')

    depth = -1* depth 
    return data

```
</div>

</div>

