Django Chartflo
===============

Charts for the lazy ones in Django

Install
--------------

Clone and add `'chartflo',` to INSTALLED_APPS


Usage
--------------

  ```python
from myapp.models import MyModelToChart

class MyChartsView(TemplateView):
    template_name = 'mytemplate.html'

    def get_context_data(self, **kwargs):
        context = super(MyChartsView, self).get_context_data(**kwargs)
        datapack = {
        		# required
        		'chart_id': 'chart_mymodeltochart',
        		'data_label': data_label, 
        		'dataset': dataset, 
        		# optional
        		'legend':True
        		}
        context['datapack'] = datapack
        return context
  ```
In the template

   ```django
{% include "chartflo/charts/pie.html" %}
<div id="{{ datapack.chart_id }}" class="gds-xl" style="width: 100%; height: 600px; background-color: #FFFFFF;" ></div>
   ```
Available charts: `pie.html`, `bar.html`, `pyramid.html`, `timeline.html`

