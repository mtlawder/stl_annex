
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json ={"e31efaeb-f4ea-45b8-9275-1c9030b5c969":{"roots":{"references":[{"attributes":{},"id":"1927","type":"BasicTicker"},{"attributes":{},"id":"2093","type":"Selection"},{"attributes":{"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"2001","type":"Line"},{"attributes":{"below":[{"id":"1926","type":"LinearAxis"}],"center":[{"id":"1930","type":"Grid"},{"id":"1935","type":"Grid"}],"left":[{"id":"1931","type":"LinearAxis"}],"plot_height":400,"plot_width":370,"renderers":[{"id":"2003","type":"GlyphRenderer"}],"title":{"id":"1916","type":"Title"},"toolbar":{"id":"1942","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"1918","type":"Range1d"},"x_scale":{"id":"1922","type":"LinearScale"},"y_range":{"id":"1920","type":"Range1d"},"y_scale":{"id":"1924","type":"LinearScale"}},"id":"1915","subtype":"Figure","type":"Plot"},{"attributes":{"axis_label":"YEAR","formatter":{"id":"2088","type":"BasicTickFormatter"},"ticker":{"id":"1927","type":"BasicTicker"}},"id":"1926","type":"LinearAxis"},{"attributes":{"text":"Departures to/from STL"},"id":"1916","type":"Title"},{"attributes":{},"id":"2088","type":"BasicTickFormatter"},{"attributes":{},"id":"1936","type":"PanTool"},{"attributes":{},"id":"1924","type":"LinearScale"},{"attributes":{"dimension":1,"ticker":{"id":"1932","type":"BasicTicker"}},"id":"1935","type":"Grid"},{"attributes":{"source":{"id":"1878","type":"ColumnDataSource"}},"id":"2004","type":"CDSView"},{"attributes":{"callback":null,"renderers":[{"id":"2003","type":"GlyphRenderer"}],"tooltips":[["Dest","SEA"],["Departures","@SEA"]]},"id":"2005","type":"HoverTool"},{"attributes":{"callback":null,"end":2018.3,"start":2010},"id":"1918","type":"Range1d"},{"attributes":{},"id":"1937","type":"WheelZoomTool"},{"attributes":{},"id":"1922","type":"LinearScale"},{"attributes":{"callback":null,"data":{"SEA":{"__ndarray__":"tQAAAMQCAADWAgAAwwIAAM8CAABTAwAAeAQAALYDAAASBAAA","dtype":"int32","shape":[9]},"YEAR":[2010,2011,2012,2013,2014,2015,2016,2017,2018]},"selected":{"id":"2093","type":"Selection"},"selection_policy":{"id":"2092","type":"UnionRenderers"}},"id":"1878","type":"ColumnDataSource"},{"attributes":{"overlay":{"id":"2094","type":"BoxAnnotation"}},"id":"1938","type":"BoxZoomTool"},{"attributes":{},"id":"1932","type":"BasicTicker"},{"attributes":{"callback":null,"end":1244},"id":"1920","type":"Range1d"},{"attributes":{},"id":"1939","type":"SaveTool"},{"attributes":{"ticker":{"id":"1927","type":"BasicTicker"}},"id":"1930","type":"Grid"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"2094","type":"BoxAnnotation"},{"attributes":{},"id":"1940","type":"ResetTool"},{"attributes":{"axis_label":"Departures","formatter":{"id":"1949","type":"BasicTickFormatter"},"ticker":{"id":"1932","type":"BasicTicker"}},"id":"1931","type":"LinearAxis"},{"attributes":{},"id":"2092","type":"UnionRenderers"},{"attributes":{},"id":"1941","type":"HelpTool"},{"attributes":{"data_source":{"id":"1878","type":"ColumnDataSource"},"glyph":{"id":"2001","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2002","type":"Line"},"selection_glyph":null,"view":{"id":"2004","type":"CDSView"}},"id":"2003","type":"GlyphRenderer"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1936","type":"PanTool"},{"id":"1937","type":"WheelZoomTool"},{"id":"1938","type":"BoxZoomTool"},{"id":"1939","type":"SaveTool"},{"id":"1940","type":"ResetTool"},{"id":"1941","type":"HelpTool"},{"id":"2005","type":"HoverTool"}]},"id":"1942","type":"Toolbar"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"2002","type":"Line"},{"attributes":{"use_scientific":false},"id":"1949","type":"BasicTickFormatter"}],"root_ids":["1915"]},"title":"Bokeh Application","version":"1.2.0"}}
                  var render_items = [{"docid":"e31efaeb-f4ea-45b8-9275-1c9030b5c969","roots":{"1915":"c51d9ae1-7930-4930-9486-28c42df78bb0"}}];
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
        