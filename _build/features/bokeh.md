---
interact_link: content/features/bokeh.ipynb
kernel_name: python3
has_widgets: false
title: 'Bokeh'
prev_page:
  url: /features/notebooks
  title: 'Notebooks'
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

<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import numpy as np
import sys
!{sys.executable} -m pip install bokeh
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

<div markdown="0" class="output output_html">

    <div class="bk-root">
        <a href="https://bokeh.pydata.org" target="_blank" class="bk-logo bk-logo-small bk-logo-notebook"></a>
    </div>
</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">






  <div class="bk-root" id="275ce6f9-3b57-42aa-a155-ab232ffb66e6" data-root-id="1755"></div>

</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

</div>
</div>
</div>

