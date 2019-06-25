---
interact_link: content/features/notebooks.ipynb
kernel_name: python3
has_widgets: false
title: 'Notebooks'
prev_page:
  url: /features/markdown
  title: 'Markdown'
next_page:
  url: /features/features
  title: 'Features'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

<!-- Configure and load Thebe !-->
<script type="text/x-thebe-config">
  {
    requestKernel: true,
    binderOptions: {
      repo: "binder-examples/requirements",
    },
  }
</script>

<script src="https://unpkg.com/thebelab@0.4.0/lib/index.js"></script>

<button id="activateButton"  style="width: 150px; height: 75px; font-size: 1.5em;">Activate</button>
<script>
var bootstrapThebe = function() {
    thebelab.bootstrap();
}
</script>

<script>
document.querySelector("#activateButton").addEventListener('click', bootstrapThebe)
</script>

# Content with notebooks

<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print("Welcome")
```
</div>
</div>

You can also create content with Jupyter Notebooks. The content for the current page is contained
in a Jupyter Notebook in the `notebooks/` folder of the repository. This means that we can include
code blocks and their outputs, and export them to Jekyll markdown.

**You can find the original notebook for this page [at this address](https://github.com/jupyter/jupyter-book/blob/master/jupyter_book/minimal/content/features/notebooks.ipynb)**

## Markdown + notebooks

As it is markdown, you can embed images, HTML, etc into your posts!

![](cool.jpg)

You an also $add_{math}$ and

$$
math^{blocks}
$$

or

$$
\begin{align*}
\mbox{mean} la_{tex} \\ \\
math blocks
\end{align*}
$$

But make sure you \\$Escape \\$your \\$dollar signs \\$you want to keep!

## Code blocks and image outputs

Textbooks with Jupyter will also embed your code blocks and output in your site.
For example, here's some sample Matplotlib code:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
plt.ion()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots(figsize=(10, 5))
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot']);

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/features/notebooks_2_0.png)

</div>
</div>
</div>



Note that the image above is captured and displayed by Jekyll.



## Removing content before publishing

You can also remove some content before publishing your book to the web. For example,
in [the original notebook](https://github.com/jupyter/jupyter-book/blob/master/jupyter_book/minimal/content/features/notebooks.ipynb) there
used to be a cell below...



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
thisvariable = "none of this should show up in the textbook"

fig, ax = plt.subplots()
x = np.random.randn(100)
y = np.random.randn(100)
ax.scatter(x, y, s=np.abs(x*100), c=x, cmap=plt.cm.coolwarm)
ax.text(0, .5, thisvariable, fontsize=20, transform=ax.transAxes)
ax.set_axis_off()
```
</div>
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/features/notebooks_5_0.png)

</div>
</div>
</div>



You can also **remove only the code** so that images and other output still show up.

Below we'll *only* display an image. It was generated with Python code in a cell,
which you can [see in the original notebook](https://github.com/jupyter/jupyter-book/blob/master/jupyter_book/minimal/content/features/notebooks.ipynb)



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# NO CODE
thisvariable = "this plot *will* show up in the textbook."

fig, ax = plt.subplots()
x = np.random.randn(100)
y = np.random.randn(100)
ax.scatter(x, y, s=np.abs(x*100), c=x, cmap=plt.cm.coolwarm)
ax.text(0, .5, thisvariable, fontsize=20, transform=ax.transAxes)
ax.set_axis_off()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/features/notebooks_7_0.png)

</div>
</div>
</div>



And here we'll *only* display a Pandas DataFrame. Again, this was generated with Python code
from [this original notebook](https://github.com/jupyter/jupyter-book/blob/master/jupyter_book/minimal/content/features/notebooks.ipynb).



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# NO CODE
import pandas as pd
pd.DataFrame([['hi', 'there'], ['this', 'is'], ['a', 'DataFrame']], columns=['Word A', 'Word B'])

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
      <th>Word A</th>
      <th>Word B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>hi</td>
      <td>there</td>
    </tr>
    <tr>
      <th>1</th>
      <td>this</td>
      <td>is</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>DataFrame</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



You can configure the text that *Textbooks with Jupyter* uses for this by modifying your site's `_config.yml` file.



## Interactive outputs

We can even do the same for *interactive* material. Below we'll display a map using `ipyleaflet`. When the notebook
is converted to Markdown, the code for creating the interactive map is retained.

**Note that this will only work for some packages.** They need to be able to output standalone HTML/Javascript, and not
depend on an underlying Python kernel to work.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import folium

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
m = folium.Map(
    location=[45.372, -121.6972],
    zoom_start=12,
    tiles='Stamen Terrain'
)

folium.Marker(
    location=[45.3288, -121.6625],
    popup='Mt. Hood Meadows',
    icon=folium.Icon(icon='cloud')
).add_to(m)

folium.Marker(
    location=[45.3311, -121.7113],
    popup='Timberline Lodge',
    icon=folium.Icon(color='green')
).add_to(m)

folium.Marker(
    location=[45.3300, -121.6823],
    popup='Some Other Location',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)


m


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgCiAgICAgICAgPHNjcmlwdD4KICAgICAgICAgICAgTF9OT19UT1VDSCA9IGZhbHNlOwogICAgICAgICAgICBMX0RJU0FCTEVfM0QgPSBmYWxzZTsKICAgICAgICA8L3NjcmlwdD4KICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjQuMC9kaXN0L2xlYWZsZXQuanMiPjwvc2NyaXB0PgogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY29kZS5qcXVlcnkuY29tL2pxdWVyeS0xLjEyLjQubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9qcy9ib290c3RyYXAubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5qcyI+PC9zY3JpcHQ+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjQuMC9kaXN0L2xlYWZsZXQuY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vYm9vdHN0cmFwLzMuMi4wL2Nzcy9ib290c3RyYXAubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9mb250LWF3ZXNvbWUvNC42LjMvY3NzL2ZvbnQtYXdlc29tZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL0xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLzIuMC4yL2xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL3Jhd2Nkbi5naXRoYWNrLmNvbS9weXRob24tdmlzdWFsaXphdGlvbi9mb2xpdW0vbWFzdGVyL2ZvbGl1bS90ZW1wbGF0ZXMvbGVhZmxldC5hd2Vzb21lLnJvdGF0ZS5jc3MiLz4KICAgIDxzdHlsZT5odG1sLCBib2R5IHt3aWR0aDogMTAwJTtoZWlnaHQ6IDEwMCU7bWFyZ2luOiAwO3BhZGRpbmc6IDA7fTwvc3R5bGU+CiAgICA8c3R5bGU+I21hcCB7cG9zaXRpb246YWJzb2x1dGU7dG9wOjA7Ym90dG9tOjA7cmlnaHQ6MDtsZWZ0OjA7fTwvc3R5bGU+CiAgICAKICAgICAgICAgICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwKICAgICAgICAgICAgICAgIGluaXRpYWwtc2NhbGU9MS4wLCBtYXhpbXVtLXNjYWxlPTEuMCwgdXNlci1zY2FsYWJsZT1ubyIgLz4KICAgICAgICAgICAgPHN0eWxlPgogICAgICAgICAgICAgICAgI21hcF83NDI3ODMxZjQ2MGU0ODM1YWUxYzAzODAyZmIyNjUzOCB7CiAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IHJlbGF0aXZlOwogICAgICAgICAgICAgICAgICAgIHdpZHRoOiAxMDAuMCU7CiAgICAgICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICAgICAgbGVmdDogMC4wJTsKICAgICAgICAgICAgICAgICAgICB0b3A6IDAuMCU7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+CiAgICAgICAgCjwvaGVhZD4KPGJvZHk+ICAgIAogICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfNzQyNzgzMWY0NjBlNDgzNWFlMWMwMzgwMmZiMjY1MzgiID48L2Rpdj4KICAgICAgICAKPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFwXzc0Mjc4MzFmNDYwZTQ4MzVhZTFjMDM4MDJmYjI2NTM4ID0gTC5tYXAoCiAgICAgICAgICAgICAgICAibWFwXzc0Mjc4MzFmNDYwZTQ4MzVhZTFjMDM4MDJmYjI2NTM4IiwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBjZW50ZXI6IFs0NS4zNzIsIC0xMjEuNjk3Ml0sCiAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NywKICAgICAgICAgICAgICAgICAgICB6b29tOiAxMiwKICAgICAgICAgICAgICAgICAgICB6b29tQ29udHJvbDogdHJ1ZSwKICAgICAgICAgICAgICAgICAgICBwcmVmZXJDYW52YXM6IGZhbHNlLAogICAgICAgICAgICAgICAgfQogICAgICAgICAgICApOwoKICAgICAgICAgICAgCgogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyX2Q3M2JiNjI3MDEwYzQ1MzRiODBlMjJiYmQ3OGQwODUwID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAiaHR0cHM6Ly9zdGFtZW4tdGlsZXMte3N9LmEuc3NsLmZhc3RseS5uZXQvdGVycmFpbi97en0ve3h9L3t5fS5qcGciLAogICAgICAgICAgICAgICAgeyJhdHRyaWJ1dGlvbiI6ICJNYXAgdGlsZXMgYnkgXHUwMDNjYSBocmVmPVwiaHR0cDovL3N0YW1lbi5jb21cIlx1MDAzZVN0YW1lbiBEZXNpZ25cdTAwM2MvYVx1MDAzZSwgdW5kZXIgXHUwMDNjYSBocmVmPVwiaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbGljZW5zZXMvYnkvMy4wXCJcdTAwM2VDQyBCWSAzLjBcdTAwM2MvYVx1MDAzZS4gRGF0YSBieSBcdTAwMjZjb3B5OyBcdTAwM2NhIGhyZWY9XCJodHRwOi8vb3BlbnN0cmVldG1hcC5vcmdcIlx1MDAzZU9wZW5TdHJlZXRNYXBcdTAwM2MvYVx1MDAzZSwgdW5kZXIgXHUwMDNjYSBocmVmPVwiaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbGljZW5zZXMvYnktc2EvMy4wXCJcdTAwM2VDQyBCWSBTQVx1MDAzYy9hXHUwMDNlLiIsICJkZXRlY3RSZXRpbmEiOiBmYWxzZSwgIm1heE5hdGl2ZVpvb20iOiAxOCwgIm1heFpvb20iOiAxOCwgIm1pblpvb20iOiAwLCAibm9XcmFwIjogZmFsc2UsICJvcGFjaXR5IjogMSwgInN1YmRvbWFpbnMiOiAiYWJjIiwgInRtcyI6IGZhbHNlfQogICAgICAgICAgICApLmFkZFRvKG1hcF83NDI3ODMxZjQ2MGU0ODM1YWUxYzAzODAyZmIyNjUzOCk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl8xNjE2YTRkNzk3NDA0MjM0YjRkMzhhMDY4Y2M0YzljZiA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQ1LjMyODgsIC0xMjEuNjYyNV0sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcF83NDI3ODMxZjQ2MGU0ODM1YWUxYzAzODAyZmIyNjUzOCk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fNzMxNDM3NDQxNjlmNDA4ZmJhZTRkYzU0MWQ2YzIwNWMgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogImNsb3VkIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibHVlIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfMTYxNmE0ZDc5NzQwNDIzNGI0ZDM4YTA2OGNjNGM5Y2Yuc2V0SWNvbihpY29uXzczMTQzNzQ0MTY5ZjQwOGZiYWU0ZGM1NDFkNmMyMDVjKTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF82Mzc0ZmEwN2E2Nzk0NTNmOGE3ZGU4NTlhMjAxZDJlZiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZWVkNjYxYmQwNmY3NDc5OTgxOWJhMmEzZTI3ZjU4OWEgPSAkKGA8ZGl2IGlkPSJodG1sX2VlZDY2MWJkMDZmNzQ3OTk4MTliYTJhM2UyN2Y1ODlhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NdC4gSG9vZCBNZWFkb3dzPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzYzNzRmYTA3YTY3OTQ1M2Y4YTdkZTg1OWEyMDFkMmVmLnNldENvbnRlbnQoaHRtbF9lZWQ2NjFiZDA2Zjc0Nzk5ODE5YmEyYTNlMjdmNTg5YSk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl8xNjE2YTRkNzk3NDA0MjM0YjRkMzhhMDY4Y2M0YzljZi5iaW5kUG9wdXAocG9wdXBfNjM3NGZhMDdhNjc5NDUzZjhhN2RlODU5YTIwMWQyZWYpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfMjU3M2E5Mjc5MjhjNDQyNTk1Yjc0YTgyNjQ0MjFhM2QgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0NS4zMzExLCAtMTIxLjcxMTNdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfNzQyNzgzMWY0NjBlNDgzNWFlMWMwMzgwMmZiMjY1MzgpOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uXzk5MDc2NmMyNDI1NjRjM2ZiYWNmNWQ1NGMwODBmZmQwID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJpbmZvLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogImdyZWVuIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfMjU3M2E5Mjc5MjhjNDQyNTk1Yjc0YTgyNjQ0MjFhM2Quc2V0SWNvbihpY29uXzk5MDc2NmMyNDI1NjRjM2ZiYWNmNWQ1NGMwODBmZmQwKTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8xOTZhNDYyNjBmMDI0ZDhhYWIyODE3ZTkxMWI5MjU2ZCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNjJlYzI0ZTBkNjQyNDU0M2E4NjA4MzFkMWFhOTA5MjMgPSAkKGA8ZGl2IGlkPSJodG1sXzYyZWMyNGUwZDY0MjQ1NDNhODYwODMxZDFhYTkwOTIzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaW1iZXJsaW5lIExvZGdlPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzE5NmE0NjI2MGYwMjRkOGFhYjI4MTdlOTExYjkyNTZkLnNldENvbnRlbnQoaHRtbF82MmVjMjRlMGQ2NDI0NTQzYTg2MDgzMWQxYWE5MDkyMyk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl8yNTczYTkyNzkyOGM0NDI1OTViNzRhODI2NDQyMWEzZC5iaW5kUG9wdXAocG9wdXBfMTk2YTQ2MjYwZjAyNGQ4YWFiMjgxN2U5MTFiOTI1NmQpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfYmU2YjIwNGNmMTRjNGVhMTkwZTNjMDk4NmIzMjRmOTEgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0NS4zMywgLTEyMS42ODIzXSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzc0Mjc4MzFmNDYwZTQ4MzVhZTFjMDM4MDJmYjI2NTM4KTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl8xNTE4MDE2N2ZkNTE0OTllOWQ2NGQ3ZWE4Y2JiYWU2YSA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiaW5mby1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJyZWQiLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl9iZTZiMjA0Y2YxNGM0ZWExOTBlM2MwOTg2YjMyNGY5MS5zZXRJY29uKGljb25fMTUxODAxNjdmZDUxNDk5ZTlkNjRkN2VhOGNiYmFlNmEpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzhmM2RmMmE3ZmU3MTQxYjhhMGFkZWI1OGRjZDYwNzcxID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9hNTNiYzg0NzQzYmI0OTkxOWZmYjczYWU1MWYwZGE0ZiA9ICQoYDxkaXYgaWQ9Imh0bWxfYTUzYmM4NDc0M2JiNDk5MTlmZmI3M2FlNTFmMGRhNGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNvbWUgT3RoZXIgTG9jYXRpb248L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfOGYzZGYyYTdmZTcxNDFiOGEwYWRlYjU4ZGNkNjA3NzEuc2V0Q29udGVudChodG1sX2E1M2JjODQ3NDNiYjQ5OTE5ZmZiNzNhZTUxZjBkYTRmKTsKICAgICAgICAKCiAgICAgICAgbWFya2VyX2JlNmIyMDRjZjE0YzRlYTE5MGUzYzA5ODZiMzI0ZjkxLmJpbmRQb3B1cChwb3B1cF84ZjNkZjJhN2ZlNzE0MWI4YTBhZGViNThkY2Q2MDc3MSkKICAgICAgICA7CgogICAgICAgIAogICAgCjwvc2NyaXB0Pg==" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>
</div>


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Click on the Interactive button at the top to execute and edit this code segment
import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

N = 4000
x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5
colors = ["#%02d%02d%02d" % (r, g, 150) for r, g in zip(np.floor(50+2*x), np.floor(30+2*y))]
output_notebook()
p = figure()
p.circle(x, y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)
show(p)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
<!--
<div markdown="0" class="output output_html">

    <div class="bk-root">
        <a href="https://bokeh.pydata.org" target="_blank" class="bk-logo bk-logo-small bk-logo-notebook"></a>
        <span id="1001"></span>
    </div>
</div>-->

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">






  <div class="bk-root" id="24cc2ff0-8d8e-444e-badd-8ab39e5e7826" data-root-id="1002"></div>

</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

</div>
</div>
</div>

