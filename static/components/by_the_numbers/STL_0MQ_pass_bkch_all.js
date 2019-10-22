
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json ={"a5954d6e-54a9-44f0-b726-7a0f3edf32da":{"roots":{"references":[{"attributes":{"callback":null,"renderers":[{"id":"1279","type":"GlyphRenderer"}],"tooltips":[["Dest","MKL"],["Passengers","@MKL"]]},"id":"1294","type":"HoverTool"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"1119","type":"BoxAnnotation"},{"attributes":{"glyph_width":6,"items":[{"id":"1121","type":"LegendItem"},{"id":"1151","type":"LegendItem"},{"id":"1204","type":"LegendItem"},{"id":"1259","type":"LegendItem"},{"id":"1293","type":"LegendItem"},{"id":"1327","type":"LegendItem"},{"id":"1361","type":"LegendItem"}],"label_text_font_size":{"value":"9pt"}},"id":"1120","type":"Legend"},{"attributes":{"label":{"value":"FOD"},"renderers":[{"id":"1112","type":"GlyphRenderer"}]},"id":"1121","type":"LegendItem"},{"attributes":{},"id":"1028","type":"SaveTool"},{"attributes":{"callback":null,"data":{"x":[2011],"y":[28.0]},"selected":{"id":"1257","type":"Selection"},"selection_policy":{"id":"1258","type":"UnionRenderers"}},"id":"1207","type":"ColumnDataSource"},{"attributes":{"use_scientific":false},"id":"1038","type":"BasicTickFormatter"},{"attributes":{"callback":null,"renderers":[{"id":"1112","type":"GlyphRenderer"}],"tooltips":[["Dest","FOD"],["Passengers","@FOD"]]},"id":"1122","type":"HoverTool"},{"attributes":{"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"FOD"}},"id":"1110","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MKL"}},"id":"1278","type":"Line"},{"attributes":{"below":[{"id":"1015","type":"LinearAxis"}],"center":[{"id":"1019","type":"Grid"},{"id":"1024","type":"Grid"},{"id":"1120","type":"Legend"}],"left":[{"id":"1020","type":"LinearAxis"}],"plot_height":400,"plot_width":425,"renderers":[{"id":"1112","type":"GlyphRenderer"},{"id":"1141","type":"GlyphRenderer"},{"id":"1157","type":"GlyphRenderer"},{"id":"1192","type":"GlyphRenderer"},{"id":"1210","type":"GlyphRenderer"},{"id":"1245","type":"GlyphRenderer"},{"id":"1279","type":"GlyphRenderer"},{"id":"1313","type":"GlyphRenderer"},{"id":"1347","type":"GlyphRenderer"}],"title":{"id":"1005","type":"Title"},"toolbar":{"id":"1031","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"1007","type":"Range1d"},"x_scale":{"id":"1011","type":"LinearScale"},"y_range":{"id":"1009","type":"Range1d"},"y_scale":{"id":"1013","type":"LinearScale"}},"id":"1004","subtype":"Figure","type":"Plot"},{"attributes":{"data_source":{"id":"1001","type":"ColumnDataSource"},"glyph":{"id":"1110","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1111","type":"Line"},"selection_glyph":null,"view":{"id":"1113","type":"CDSView"}},"id":"1112","type":"GlyphRenderer"},{"attributes":{"label":{"value":"TBN"},"renderers":[{"id":"1192","type":"GlyphRenderer"}]},"id":"1204","type":"LegendItem"},{"attributes":{"dimension":1,"ticker":{"id":"1021","type":"BasicTicker"}},"id":"1024","type":"Grid"},{"attributes":{"overlay":{"id":"1119","type":"BoxAnnotation"}},"id":"1027","type":"BoxZoomTool"},{"attributes":{"callback":null,"data":{"BRL":{"__ndarray__":"AAAAAACkoUAAAAAAAGC3QAAAAAAAx7tAAAAAAADPtUAAAAAAAFO3QAAAAAAAo7ZAAAAAAACbtEAAAAAAAI61QAAAAAAAm7dA","dtype":"float64","shape":[9]},"DEC":{"__ndarray__":"AAAAAAA8nkAAAAAAACe1QAAAAAAANbNAAAAAAABGsEAAAAAAACyyQAAAAAAAI7hAAAAAAADms0AAAAAAAKuyQAAAAAAAEHZA","dtype":"float64","shape":[9]},"FOD":{"__ndarray__":"AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAA/MBAAAAAAAD5xUAAAAAAAATAQAAAAAAATMVA","dtype":"float64","shape":[9]},"IRK":{"__ndarray__":"AAAAAAAwnUAAAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"JBR":{"__ndarray__":"AAAAAAAA+H8AAAAAAAD4fwAAAACAn8FAAAAAAIADwkAAAAAAgIrCQAAAAACAHsJAAAAAAIBxwkAAAAAAgHXCQAAAAAAA68VA","dtype":"float64","shape":[9]},"MKL":{"__ndarray__":"AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAGKZAAAAAAAB0vUAAAAAAAOi+QAAAAAAArLtA","dtype":"float64","shape":[9]},"TBN":{"__ndarray__":"AAAAAAAA+H8AAAAAAAA8QAAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"YEAR":[2010,2011,2012,2013,2014,2015,2016,2017,2018]},"selected":{"id":"1149","type":"Selection"},"selection_policy":{"id":"1150","type":"UnionRenderers"}},"id":"1001","type":"ColumnDataSource"},{"attributes":{},"id":"1025","type":"PanTool"},{"attributes":{},"id":"1021","type":"BasicTicker"},{"attributes":{"ticker":{"id":"1016","type":"BasicTicker"}},"id":"1019","type":"Grid"},{"attributes":{"axis_label":"Passengers","formatter":{"id":"1038","type":"BasicTickFormatter"},"ticker":{"id":"1021","type":"BasicTicker"}},"id":"1020","type":"LinearAxis"},{"attributes":{},"id":"1030","type":"HelpTool"},{"attributes":{"callback":null,"end":16250.0},"id":"1009","type":"Range1d"},{"attributes":{},"id":"1029","type":"ResetTool"},{"attributes":{"callback":null,"renderers":[{"id":"1192","type":"GlyphRenderer"}],"tooltips":[["Dest","TBN"],["Passengers","@TBN"]]},"id":"1205","type":"HoverTool"},{"attributes":{"line_color":"#98df8a","line_width":3,"x":{"field":"YEAR"},"y":{"field":"BRL"}},"id":"1311","type":"Line"},{"attributes":{},"id":"1203","type":"UnionRenderers"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"BRL"}},"id":"1312","type":"Line"},{"attributes":{"line_color":"#2ca02c","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MKL"}},"id":"1277","type":"Line"},{"attributes":{"line_color":"#aec7e8","line_width":3,"x":{"field":"YEAR"},"y":{"field":"IRK"}},"id":"1139","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"IRK"}},"id":"1140","type":"Line"},{"attributes":{"data_source":{"id":"1001","type":"ColumnDataSource"},"glyph":{"id":"1311","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1312","type":"Line"},"selection_glyph":null,"view":{"id":"1314","type":"CDSView"}},"id":"1313","type":"GlyphRenderer"},{"attributes":{"data_source":{"id":"1001","type":"ColumnDataSource"},"glyph":{"id":"1139","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1140","type":"Line"},"selection_glyph":null,"view":{"id":"1142","type":"CDSView"}},"id":"1141","type":"GlyphRenderer"},{"attributes":{},"id":"1013","type":"LinearScale"},{"attributes":{"source":{"id":"1001","type":"ColumnDataSource"}},"id":"1314","type":"CDSView"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"FOD"}},"id":"1111","type":"Line"},{"attributes":{"label":{"value":"BRL"},"renderers":[{"id":"1313","type":"GlyphRenderer"}]},"id":"1327","type":"LegendItem"},{"attributes":{"source":{"id":"1001","type":"ColumnDataSource"}},"id":"1142","type":"CDSView"},{"attributes":{},"id":"1016","type":"BasicTicker"},{"attributes":{},"id":"1149","type":"Selection"},{"attributes":{"callback":null,"renderers":[{"id":"1313","type":"GlyphRenderer"}],"tooltips":[["Dest","BRL"],["Passengers","@BRL"]]},"id":"1328","type":"HoverTool"},{"attributes":{},"id":"1150","type":"UnionRenderers"},{"attributes":{"axis_label":"YEAR","formatter":{"id":"1117","type":"BasicTickFormatter"},"ticker":{"id":"1016","type":"BasicTicker"}},"id":"1015","type":"LinearAxis"},{"attributes":{"label":{"value":"IRK"},"renderers":[{"id":"1141","type":"GlyphRenderer"}]},"id":"1151","type":"LegendItem"},{"attributes":{"line_color":"#ff7f0e","line_width":3,"x":{"field":"YEAR"},"y":{"field":"TBN"}},"id":"1190","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"TBN"}},"id":"1191","type":"Line"},{"attributes":{"line_color":"#ffbb78","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DEC"}},"id":"1243","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"1141","type":"GlyphRenderer"}],"tooltips":[["Dest","IRK"],["Passengers","@IRK"]]},"id":"1152","type":"HoverTool"},{"attributes":{"data_source":{"id":"1001","type":"ColumnDataSource"},"glyph":{"id":"1190","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1191","type":"Line"},"selection_glyph":null,"view":{"id":"1193","type":"CDSView"}},"id":"1192","type":"GlyphRenderer"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DEC"}},"id":"1244","type":"Line"},{"attributes":{},"id":"1011","type":"LinearScale"},{"attributes":{"callback":null,"data":{"x":[2010],"y":[1868.0]},"selected":{"id":"1202","type":"Selection"},"selection_policy":{"id":"1203","type":"UnionRenderers"}},"id":"1154","type":"ColumnDataSource"},{"attributes":{"data_source":{"id":"1001","type":"ColumnDataSource"},"glyph":{"id":"1243","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1244","type":"Line"},"selection_glyph":null,"view":{"id":"1246","type":"CDSView"}},"id":"1245","type":"GlyphRenderer"},{"attributes":{"source":{"id":"1001","type":"ColumnDataSource"}},"id":"1193","type":"CDSView"},{"attributes":{},"id":"1202","type":"Selection"},{"attributes":{"callback":null,"end":2019.98,"start":2010},"id":"1007","type":"Range1d"},{"attributes":{"fill_color":{"value":"#aec7e8"},"line_color":{"value":"#aec7e8"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"1155","type":"Square"},{"attributes":{"source":{"id":"1001","type":"ColumnDataSource"}},"id":"1246","type":"CDSView"},{"attributes":{"text":"Passengers flying out/in STL"},"id":"1005","type":"Title"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"1156","type":"Square"},{"attributes":{"fill_color":{"value":"#ff7f0e"},"line_color":{"value":"#ff7f0e"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"1208","type":"Square"},{"attributes":{},"id":"1257","type":"Selection"},{"attributes":{"data_source":{"id":"1154","type":"ColumnDataSource"},"glyph":{"id":"1155","type":"Square"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1156","type":"Square"},"selection_glyph":null,"view":{"id":"1158","type":"CDSView"}},"id":"1157","type":"GlyphRenderer"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"1209","type":"Square"},{"attributes":{},"id":"1258","type":"UnionRenderers"},{"attributes":{"label":{"value":"MKL"},"renderers":[{"id":"1279","type":"GlyphRenderer"}]},"id":"1293","type":"LegendItem"},{"attributes":{"data_source":{"id":"1207","type":"ColumnDataSource"},"glyph":{"id":"1208","type":"Square"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1209","type":"Square"},"selection_glyph":null,"view":{"id":"1211","type":"CDSView"}},"id":"1210","type":"GlyphRenderer"},{"attributes":{"label":{"value":"DEC"},"renderers":[{"id":"1245","type":"GlyphRenderer"}]},"id":"1259","type":"LegendItem"},{"attributes":{"source":{"id":"1154","type":"ColumnDataSource"}},"id":"1158","type":"CDSView"},{"attributes":{"line_color":"#d62728","line_width":3,"x":{"field":"YEAR"},"y":{"field":"JBR"}},"id":"1345","type":"Line"},{"attributes":{"source":{"id":"1207","type":"ColumnDataSource"}},"id":"1211","type":"CDSView"},{"attributes":{"callback":null,"renderers":[{"id":"1157","type":"GlyphRenderer"}],"tooltips":[["Dest","IRK"],["Passengers","1868"]]},"id":"1159","type":"HoverTool"},{"attributes":{"callback":null,"renderers":[{"id":"1245","type":"GlyphRenderer"}],"tooltips":[["Dest","DEC"],["Passengers","@DEC"]]},"id":"1260","type":"HoverTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"JBR"}},"id":"1346","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"1210","type":"GlyphRenderer"}],"tooltips":[["Dest","TBN"],["Passengers","28"]]},"id":"1212","type":"HoverTool"},{"attributes":{"data_source":{"id":"1001","type":"ColumnDataSource"},"glyph":{"id":"1345","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1346","type":"Line"},"selection_glyph":null,"view":{"id":"1348","type":"CDSView"}},"id":"1347","type":"GlyphRenderer"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1025","type":"PanTool"},{"id":"1026","type":"WheelZoomTool"},{"id":"1027","type":"BoxZoomTool"},{"id":"1028","type":"SaveTool"},{"id":"1029","type":"ResetTool"},{"id":"1030","type":"HelpTool"},{"id":"1122","type":"HoverTool"},{"id":"1152","type":"HoverTool"},{"id":"1159","type":"HoverTool"},{"id":"1205","type":"HoverTool"},{"id":"1212","type":"HoverTool"},{"id":"1260","type":"HoverTool"},{"id":"1294","type":"HoverTool"},{"id":"1328","type":"HoverTool"},{"id":"1362","type":"HoverTool"}]},"id":"1031","type":"Toolbar"},{"attributes":{"data_source":{"id":"1001","type":"ColumnDataSource"},"glyph":{"id":"1277","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1278","type":"Line"},"selection_glyph":null,"view":{"id":"1280","type":"CDSView"}},"id":"1279","type":"GlyphRenderer"},{"attributes":{"source":{"id":"1001","type":"ColumnDataSource"}},"id":"1348","type":"CDSView"},{"attributes":{"label":{"value":"JBR"},"renderers":[{"id":"1347","type":"GlyphRenderer"}]},"id":"1361","type":"LegendItem"},{"attributes":{},"id":"1026","type":"WheelZoomTool"},{"attributes":{"source":{"id":"1001","type":"ColumnDataSource"}},"id":"1113","type":"CDSView"},{"attributes":{"source":{"id":"1001","type":"ColumnDataSource"}},"id":"1280","type":"CDSView"},{"attributes":{},"id":"1117","type":"BasicTickFormatter"},{"attributes":{"callback":null,"renderers":[{"id":"1347","type":"GlyphRenderer"}],"tooltips":[["Dest","JBR"],["Passengers","@JBR"]]},"id":"1362","type":"HoverTool"}],"root_ids":["1004"]},"title":"Bokeh Application","version":"1.2.0"}}
                  var render_items = [{"docid":"a5954d6e-54a9-44f0-b726-7a0f3edf32da","roots":{"1004":"eb845f6c-7cc8-4fba-ad85-e36b6ea8caba"}}];
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
        