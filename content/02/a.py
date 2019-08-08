def regionalMap(tables, variabels, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag):
    for i in tqdm(range(len(tables)), desc='overall'):
        
        unit = tables[i].variables[variables[i]].attrs['units']
        
        toDateTime = tables[i].indexes['TIME'].to_datetimeindex()
        tables[i]['TIME'] = toDateTime
        table = tables[i].sel(TIME = slice(startDate, endDate), LAT_C = slice(lat1, lat2), LON_C = slice(lon1, lon2), DEP_C = slice(depth1, depth2))
        
        varData = table.variables[variables[i]][0,0,:,:].values       
        
        lats = table.variables['LAT_C'].values.tolist()
        lons = table.variables['LON_C'].values.tolist()
        
        shape = (len(lats), len(lons))
        
        varData.reshape(shape)

        varData[varData < 0] = float('NaN')
        varData = [np.asarray(varData)]
        lats = [np.asarray(lats)]
        lons = [np.asarray(lons)]
        
        bokehMap(varData, unit, 'regional', lats, lons, unit, 'OTHER', variables[i])

def bokehMap(data, subject, fname, lat, lon, units, tables, variabels):
    TOOLS="crosshair,pan,zoom_in,wheel_zoom,zoom_out,box_zoom,reset,save,"
    p = []
    for ind in range(len(data)):

        w, h = com.canvasRect(dw=np.max(lon[ind])-np.min(lon[ind]), dh=np.max(lat[ind])-np.min(lat[ind]))
        p1 = figure(tools=TOOLS, toolbar_location="right", title=subject[ind], plot_width=w, plot_height=h, x_range=(np.min(lon[ind]), np.max(lon[ind])), y_range=(np.min(lat[ind]), np.max(lat[ind])))
        p1.xaxis.axis_label = 'Longitude'
        p1.yaxis.axis_label = 'Latitude'
    
        unit = units
        
        bounds = com.getBounds(variabels[ind])
        
        paletteName = com.getPalette(variabels[ind])
        low, high = bounds[0], bounds[1]
        
        if low == None:
            low, high = np.nanmin(data[ind].flatten()), np.nanmax(data[ind].flatten())
        color_mapper = LinearColorMapper(palette=paletteName, low=low, high=high)
        p1.image(image=[data[ind]], color_mapper=color_mapper, x=np.min(lon[ind]), y=np.min(lat[ind]), dw=np.max(lon[ind])-np.min(lon[ind]), dh=np.max(lat[ind])-np.min(lat[ind]))
        p1.add_tools(HoverTool(
            tooltips=[
                ('longitude', '$x'),
                ('latitude', '$y'),
                (variabels[ind]+unit, '@image'),
            ],
            mode='mouse'
        ))
        color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                        label_standoff=12, border_line_color=None, location=(0,0))
        p1.add_layout(color_bar, 'right')
        p.append(p1)
    if len(p) > 0:
       # if not inline:      ## if jupyter is not the caller
       #     dirPath = 'embed/'
       #     if not os.path.exists(dirPath):
       #         os.makedirs(dirPath)        
       #     output_file(dirPath + fname + ".html", title="Regional Map")
        show(column(p))
    return
