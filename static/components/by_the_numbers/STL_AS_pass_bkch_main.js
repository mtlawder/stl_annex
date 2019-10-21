
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json ={"cfb9b753-32de-4287-ae0d-ba6e983f77fc":{"roots":{"references":[{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"1995","type":"BoxAnnotation"},{"attributes":{"axis_label":"YEAR","formatter":{"id":"1991","type":"BasicTickFormatter"},"ticker":{"id":"1892","type":"BasicTicker"}},"id":"1891","type":"LinearAxis"},{"attributes":{"callback":null,"data":{"SEA":{"__ndarray__":"PmkAAPx6AQCPiQEAdIABAOSlAQAFAwIAhYACAC8RAgCiXAIA","dtype":"int32","shape":[9]},"YEAR":[2010,2011,2012,2013,2014,2015,2016,2017,2018]},"selected":{"id":"2020","type":"Selection"},"selection_policy":{"id":"2019","type":"UnionRenderers"}},"id":"1877","type":"ColumnDataSource"},{"attributes":{},"id":"1991","type":"BasicTickFormatter"},{"attributes":{},"id":"1905","type":"ResetTool"},{"attributes":{},"id":"1904","type":"SaveTool"},{"attributes":{},"id":"1887","type":"LinearScale"},{"attributes":{"label":{"value":"SEA"},"renderers":[{"id":"1988","type":"GlyphRenderer"}]},"id":"1997","type":"LegendItem"},{"attributes":{"overlay":{"id":"1995","type":"BoxAnnotation"}},"id":"1903","type":"BoxZoomTool"},{"attributes":{"text":"Passengers flying out/in STL"},"id":"1881","type":"Title"},{"attributes":{"glyph_width":6,"items":[{"id":"1997","type":"LegendItem"}],"label_text_font_size":{"value":"9pt"}},"id":"1996","type":"Legend"},{"attributes":{},"id":"1902","type":"WheelZoomTool"},{"attributes":{},"id":"2019","type":"UnionRenderers"},{"attributes":{},"id":"2020","type":"Selection"},{"attributes":{},"id":"1901","type":"PanTool"},{"attributes":{"callback":null,"renderers":[{"id":"1988","type":"GlyphRenderer"}],"tooltips":[["Dest","SEA"],["Passengers","@SEA"]]},"id":"1998","type":"HoverTool"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1901","type":"PanTool"},{"id":"1902","type":"WheelZoomTool"},{"id":"1903","type":"BoxZoomTool"},{"id":"1904","type":"SaveTool"},{"id":"1905","type":"ResetTool"},{"id":"1906","type":"HelpTool"},{"id":"1998","type":"HoverTool"}]},"id":"1907","type":"Toolbar"},{"attributes":{"axis_label":"Passengers","formatter":{"id":"1914","type":"BasicTickFormatter"},"ticker":{"id":"1897","type":"BasicTicker"}},"id":"1896","type":"LinearAxis"},{"attributes":{},"id":"1897","type":"BasicTicker"},{"attributes":{"use_scientific":false},"id":"1914","type":"BasicTickFormatter"},{"attributes":{"dimension":1,"ticker":{"id":"1897","type":"BasicTicker"}},"id":"1900","type":"Grid"},{"attributes":{},"id":"1889","type":"LinearScale"},{"attributes":{"data_source":{"id":"1877","type":"ColumnDataSource"},"glyph":{"id":"1986","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1987","type":"Line"},"selection_glyph":null,"view":{"id":"1989","type":"CDSView"}},"id":"1988","type":"GlyphRenderer"},{"attributes":{"below":[{"id":"1891","type":"LinearAxis"}],"center":[{"id":"1895","type":"Grid"},{"id":"1900","type":"Grid"},{"id":"1996","type":"Legend"}],"left":[{"id":"1896","type":"LinearAxis"}],"plot_height":400,"plot_width":425,"renderers":[{"id":"1988","type":"GlyphRenderer"}],"title":{"id":"1881","type":"Title"},"toolbar":{"id":"1907","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"1883","type":"Range1d"},"x_scale":{"id":"1887","type":"LinearScale"},"y_range":{"id":"1885","type":"Range1d"},"y_scale":{"id":"1889","type":"LinearScale"}},"id":"1880","subtype":"Figure","type":"Plot"},{"attributes":{"source":{"id":"1877","type":"ColumnDataSource"}},"id":"1989","type":"CDSView"},{"attributes":{},"id":"1906","type":"HelpTool"},{"attributes":{"callback":null,"end":2019.98,"start":2010},"id":"1883","type":"Range1d"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"1987","type":"Line"},{"attributes":{},"id":"1892","type":"BasicTicker"},{"attributes":{"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"1986","type":"Line"},{"attributes":{"ticker":{"id":"1892","type":"BasicTicker"}},"id":"1895","type":"Grid"},{"attributes":{"callback":null,"end":168973},"id":"1885","type":"Range1d"}],"root_ids":["1880"]},"title":"Bokeh Application","version":"1.2.0"}}
                  var render_items = [{"docid":"cfb9b753-32de-4287-ae0d-ba6e983f77fc","roots":{"1880":"086bec32-2fc0-4f14-a598-3a6e30ffaf2c"}}];
                  root.Bokeh.embed.embed_items(docs_json, render_items);
                
                  }
                  if (root.Bokeh !== undefined) {
                    embed_document(root);
                  } else {
                    var attempts = 0;
                    var timer = setInterval(function(root) {
                      if (root.Bokeh !== undefined) {
                        embed_document(root);
                        clearInterval(timer);
                      }
                      attempts++;
                      if (attempts > 100) {
                        console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
                        clearInterval(timer);
                      }
                    }, 10, root)
                  }
                })(window);
              });
            };
            if (document.readyState != "loading") fn();
            else document.addEventListener("DOMContentLoaded", fn);
          })();
        