
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json ={"824cefa0-caf3-42d4-b011-d4280b35f199":{"roots":{"references":[{"attributes":{},"id":"2166","type":"Selection"},{"attributes":{},"id":"1967","type":"BasicTicker"},{"attributes":{"callback":null,"end":2018.3,"start":2010},"id":"1953","type":"Range1d"},{"attributes":{"callback":null,"renderers":[{"id":"2010","type":"GlyphRenderer"}],"tooltips":[["Dest","SEA"],["Load Factor","@SEA"]]},"id":"2012","type":"HoverTool"},{"attributes":{"callback":null,"data":{"SEA":{"__ndarray__":"h4akLAQYVkBngPs11YVVQJzMqetPv1VAZMNTqJvWVUCAGqDAxpxWQNwInmhuW1ZA2CBtuR1jVECKCJdx7lFUQDHB5vc9G1VA","dtype":"float64","shape":[9]},"YEAR":[2010,2011,2012,2013,2014,2015,2016,2017,2018]},"selected":{"id":"2166","type":"Selection"},"selection_policy":{"id":"2165","type":"UnionRenderers"}},"id":"1879","type":"ColumnDataSource"},{"attributes":{"text":"Load Factor"},"id":"1951","type":"Title"},{"attributes":{"dimension":1,"ticker":{"id":"1967","type":"BasicTicker"}},"id":"1970","type":"Grid"},{"attributes":{"axis_label":"YEAR","formatter":{"id":"2161","type":"BasicTickFormatter"},"ticker":{"id":"1962","type":"BasicTicker"}},"id":"1961","type":"LinearAxis"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1971","type":"PanTool"},{"id":"1972","type":"WheelZoomTool"},{"id":"1973","type":"BoxZoomTool"},{"id":"1974","type":"SaveTool"},{"id":"1975","type":"ResetTool"},{"id":"1976","type":"HelpTool"},{"id":"2012","type":"HoverTool"}]},"id":"1977","type":"Toolbar"},{"attributes":{},"id":"1959","type":"LinearScale"},{"attributes":{},"id":"2161","type":"BasicTickFormatter"},{"attributes":{"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"2008","type":"Line"},{"attributes":{},"id":"1957","type":"LinearScale"},{"attributes":{},"id":"1971","type":"PanTool"},{"attributes":{"below":[{"id":"1961","type":"LinearAxis"}],"center":[{"id":"1965","type":"Grid"},{"id":"1970","type":"Grid"}],"left":[{"id":"1966","type":"LinearAxis"}],"plot_height":400,"plot_width":370,"renderers":[{"id":"2010","type":"GlyphRenderer"}],"title":{"id":"1951","type":"Title"},"toolbar":{"id":"1977","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"1953","type":"Range1d"},"x_scale":{"id":"1957","type":"LinearScale"},"y_range":{"id":"1955","type":"Range1d"},"y_scale":{"id":"1959","type":"LinearScale"}},"id":"1950","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"1975","type":"ResetTool"},{"attributes":{"callback":null,"end":100,"start":50},"id":"1955","type":"Range1d"},{"attributes":{},"id":"2165","type":"UnionRenderers"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"2167","type":"BoxAnnotation"},{"attributes":{},"id":"1974","type":"SaveTool"},{"attributes":{},"id":"1962","type":"BasicTicker"},{"attributes":{},"id":"1976","type":"HelpTool"},{"attributes":{"source":{"id":"1879","type":"ColumnDataSource"}},"id":"2011","type":"CDSView"},{"attributes":{"overlay":{"id":"2167","type":"BoxAnnotation"}},"id":"1973","type":"BoxZoomTool"},{"attributes":{"ticker":{"id":"1962","type":"BasicTicker"}},"id":"1965","type":"Grid"},{"attributes":{"data_source":{"id":"1879","type":"ColumnDataSource"},"glyph":{"id":"2008","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2009","type":"Line"},"selection_glyph":null,"view":{"id":"2011","type":"CDSView"}},"id":"2010","type":"GlyphRenderer"},{"attributes":{},"id":"1972","type":"WheelZoomTool"},{"attributes":{"axis_label":"Load Factor","formatter":{"id":"1984","type":"BasicTickFormatter"},"ticker":{"id":"1967","type":"BasicTicker"}},"id":"1966","type":"LinearAxis"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"2009","type":"Line"},{"attributes":{"use_scientific":false},"id":"1984","type":"BasicTickFormatter"}],"root_ids":["1950"]},"title":"Bokeh Application","version":"1.2.0"}}
                  var render_items = [{"docid":"824cefa0-caf3-42d4-b011-d4280b35f199","roots":{"1950":"f95b5c56-6a06-4ca6-9ab6-142a84d94f23"}}];
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
        