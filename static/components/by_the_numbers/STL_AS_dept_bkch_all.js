
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json ={"191b529a-434f-4d71-9319-b70aa2d5f6fd":{"roots":{"references":[{"attributes":{"callback":null,"renderers":[{"id":"1155","type":"GlyphRenderer"}],"tooltips":[["Dest","ORD"],["Departures","13"]]},"id":"1157","type":"HoverTool"},{"attributes":{},"id":"1046","type":"LinearScale"},{"attributes":{"line_color":"#ff7f0e","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SAN"}},"id":"1258","type":"Line"},{"attributes":{},"id":"1048","type":"LinearScale"},{"attributes":{"below":[{"id":"1050","type":"LinearAxis"}],"center":[{"id":"1054","type":"Grid"},{"id":"1059","type":"Grid"}],"left":[{"id":"1055","type":"LinearAxis"}],"plot_height":400,"plot_width":370,"renderers":[{"id":"1141","type":"GlyphRenderer"},{"id":"1148","type":"GlyphRenderer"},{"id":"1155","type":"GlyphRenderer"},{"id":"1210","type":"GlyphRenderer"},{"id":"1217","type":"GlyphRenderer"},{"id":"1260","type":"GlyphRenderer"},{"id":"1303","type":"GlyphRenderer"},{"id":"1310","type":"GlyphRenderer"},{"id":"1355","type":"GlyphRenderer"},{"id":"1393","type":"GlyphRenderer"},{"id":"1431","type":"GlyphRenderer"}],"title":{"id":"1040","type":"Title"},"toolbar":{"id":"1066","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"1042","type":"Range1d"},"x_scale":{"id":"1046","type":"LinearScale"},"y_range":{"id":"1044","type":"Range1d"},"y_scale":{"id":"1048","type":"LinearScale"}},"id":"1039","subtype":"Figure","type":"Plot"},{"attributes":{"line_color":"#aec7e8","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MIA"}},"id":"1208","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"LAX"}},"id":"1354","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SAN"}},"id":"1259","type":"Line"},{"attributes":{"axis_label":"YEAR","formatter":{"id":"1588","type":"BasicTickFormatter"},"ticker":{"id":"1051","type":"BasicTicker"}},"id":"1050","type":"LinearAxis"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MIA"}},"id":"1209","type":"Line"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1258","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1259","type":"Line"},"selection_glyph":null,"view":{"id":"1261","type":"CDSView"}},"id":"1260","type":"GlyphRenderer"},{"attributes":{},"id":"1051","type":"BasicTicker"},{"attributes":{"callback":null,"renderers":[{"id":"1431","type":"GlyphRenderer"}],"tooltips":[["Dest","SEA"],["Departures","@SEA"]]},"id":"1433","type":"HoverTool"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1208","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1209","type":"Line"},"selection_glyph":null,"view":{"id":"1211","type":"CDSView"}},"id":"1210","type":"GlyphRenderer"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1261","type":"CDSView"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1060","type":"PanTool"},{"id":"1061","type":"WheelZoomTool"},{"id":"1062","type":"BoxZoomTool"},{"id":"1063","type":"SaveTool"},{"id":"1064","type":"ResetTool"},{"id":"1065","type":"HelpTool"},{"id":"1143","type":"HoverTool"},{"id":"1150","type":"HoverTool"},{"id":"1157","type":"HoverTool"},{"id":"1212","type":"HoverTool"},{"id":"1219","type":"HoverTool"},{"id":"1262","type":"HoverTool"},{"id":"1305","type":"HoverTool"},{"id":"1312","type":"HoverTool"},{"id":"1357","type":"HoverTool"},{"id":"1395","type":"HoverTool"},{"id":"1433","type":"HoverTool"}]},"id":"1066","type":"Toolbar"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1211","type":"CDSView"},{"attributes":{},"id":"1060","type":"PanTool"},{"attributes":{"callback":null,"renderers":[{"id":"1260","type":"GlyphRenderer"}],"tooltips":[["Dest","SAN"],["Departures","@SAN"]]},"id":"1262","type":"HoverTool"},{"attributes":{},"id":"1061","type":"WheelZoomTool"},{"attributes":{"callback":null,"renderers":[{"id":"1210","type":"GlyphRenderer"}],"tooltips":[["Dest","MIA"],["Departures","@MIA"]]},"id":"1212","type":"HoverTool"},{"attributes":{"overlay":{"id":"1602","type":"BoxAnnotation"}},"id":"1062","type":"BoxZoomTool"},{"attributes":{"callback":null,"data":{"x":[2017],"y":[14.0]},"selected":{"id":"1599","type":"Selection"},"selection_policy":{"id":"1598","type":"UnionRenderers"}},"id":"1214","type":"ColumnDataSource"},{"attributes":{},"id":"1063","type":"SaveTool"},{"attributes":{"axis_label":"Departures","formatter":{"id":"1073","type":"BasicTickFormatter"},"ticker":{"id":"1056","type":"BasicTicker"}},"id":"1055","type":"LinearAxis"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1353","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1354","type":"Line"},"selection_glyph":null,"view":{"id":"1356","type":"CDSView"}},"id":"1355","type":"GlyphRenderer"},{"attributes":{"fill_color":{"value":"#aec7e8"},"line_color":{"value":"#aec7e8"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"1215","type":"Square"},{"attributes":{},"id":"1064","type":"ResetTool"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1432","type":"CDSView"},{"attributes":{"text":"Departures to/from STL"},"id":"1040","type":"Title"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"1216","type":"Square"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1356","type":"CDSView"},{"attributes":{"ticker":{"id":"1051","type":"BasicTicker"}},"id":"1054","type":"Grid"},{"attributes":{},"id":"1065","type":"HelpTool"},{"attributes":{"data_source":{"id":"1214","type":"ColumnDataSource"},"glyph":{"id":"1215","type":"Square"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1216","type":"Square"},"selection_glyph":null,"view":{"id":"1218","type":"CDSView"}},"id":"1217","type":"GlyphRenderer"},{"attributes":{},"id":"1601","type":"Selection"},{"attributes":{"callback":null,"renderers":[{"id":"1355","type":"GlyphRenderer"}],"tooltips":[["Dest","LAX"],["Departures","@LAX"]]},"id":"1357","type":"HoverTool"},{"attributes":{"source":{"id":"1214","type":"ColumnDataSource"}},"id":"1218","type":"CDSView"},{"attributes":{"line_color":"#ffbb78","line_width":3,"x":{"field":"YEAR"},"y":{"field":"LGA"}},"id":"1301","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"1430","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"1217","type":"GlyphRenderer"}],"tooltips":[["Dest","MIA"],["Departures","14"]]},"id":"1219","type":"HoverTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"LGA"}},"id":"1302","type":"Line"},{"attributes":{"callback":null,"end":2018.3,"start":2010},"id":"1042","type":"Range1d"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1301","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1302","type":"Line"},"selection_glyph":null,"view":{"id":"1304","type":"CDSView"}},"id":"1303","type":"GlyphRenderer"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1304","type":"CDSView"},{"attributes":{"callback":null,"renderers":[{"id":"1303","type":"GlyphRenderer"}],"tooltips":[["Dest","LGA"],["Departures","@LGA"]]},"id":"1305","type":"HoverTool"},{"attributes":{"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"ORD"}},"id":"1139","type":"Line"},{"attributes":{"callback":null,"data":{"x":[2017],"y":[14.0]},"selected":{"id":"1601","type":"Selection"},"selection_policy":{"id":"1600","type":"UnionRenderers"}},"id":"1307","type":"ColumnDataSource"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"ORD"}},"id":"1140","type":"Line"},{"attributes":{"fill_color":{"value":"#ffbb78"},"line_color":{"value":"#ffbb78"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"1308","type":"Square"},{"attributes":{"line_color":"#d62728","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"1429","type":"Line"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1139","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1140","type":"Line"},"selection_glyph":null,"view":{"id":"1142","type":"CDSView"}},"id":"1141","type":"GlyphRenderer"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"1309","type":"Square"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1142","type":"CDSView"},{"attributes":{},"id":"1594","type":"UnionRenderers"},{"attributes":{"data_source":{"id":"1307","type":"ColumnDataSource"},"glyph":{"id":"1308","type":"Square"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1309","type":"Square"},"selection_glyph":null,"view":{"id":"1311","type":"CDSView"}},"id":"1310","type":"GlyphRenderer"},{"attributes":{"callback":null,"data":{"LAX":{"__ndarray__":"AAAAAACAV0AAAAAAAIBJQAAAAAAAwFBAAAAAAABAUkAAAAAAAABQQAAAAAAAADhAAAAAAAAAOkAAAAAAAAAyQAAAAAAAACZA","dtype":"float64","shape":[9]},"LGA":{"__ndarray__":"AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAAsQAAAAAAAAPh/","dtype":"float64","shape":[9]},"MIA":{"__ndarray__":"AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAAsQAAAAAAAAPh/","dtype":"float64","shape":[9]},"ORD":{"__ndarray__":"AAAAAACAQEAAAAAAAAD4fwAAAAAAACpAAAAAAAAALEAAAAAAAAAzQAAAAAAAADNAAAAAAAAA+H8AAAAAAAAqQAAAAAAAAPh/","dtype":"float64","shape":[9]},"PDX":{"__ndarray__":"AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAA0HZAAAAAAAB4hkAAAAAAAICDQAAAAAAAgGFA","dtype":"float64","shape":[9]},"SAN":{"__ndarray__":"AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAA+QAAAAAAAGIZA","dtype":"float64","shape":[9]},"SEA":{"__ndarray__":"AAAAAADgbkAAAAAAACCGQAAAAAAAsIZAAAAAAAAYhkAAAAAAAHiGQAAAAAAAmIpAAAAAAADgkUAAAAAAAICTQAAAAAAAZJJA","dtype":"float64","shape":[9]},"YEAR":[2010,2011,2012,2013,2014,2015,2016,2017,2018]},"selected":{"id":"1593","type":"Selection"},"selection_policy":{"id":"1592","type":"UnionRenderers"}},"id":"1002","type":"ColumnDataSource"},{"attributes":{"source":{"id":"1307","type":"ColumnDataSource"}},"id":"1311","type":"CDSView"},{"attributes":{"callback":null,"renderers":[{"id":"1141","type":"GlyphRenderer"}],"tooltips":[["Dest","ORD"],["Departures","@ORD"]]},"id":"1143","type":"HoverTool"},{"attributes":{},"id":"1056","type":"BasicTicker"},{"attributes":{},"id":"1588","type":"BasicTickFormatter"},{"attributes":{"callback":null,"data":{"x":[2010],"y":[33.0]},"selected":{"id":"1595","type":"Selection"},"selection_policy":{"id":"1594","type":"UnionRenderers"}},"id":"1145","type":"ColumnDataSource"},{"attributes":{"callback":null,"renderers":[{"id":"1310","type":"GlyphRenderer"}],"tooltips":[["Dest","LGA"],["Departures","14"]]},"id":"1312","type":"HoverTool"},{"attributes":{"fill_color":{"value":"#1f77b4"},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"1146","type":"Square"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"1602","type":"BoxAnnotation"},{"attributes":{"dimension":1,"ticker":{"id":"1056","type":"BasicTicker"}},"id":"1059","type":"Grid"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"1147","type":"Square"},{"attributes":{},"id":"1593","type":"Selection"},{"attributes":{"data_source":{"id":"1145","type":"ColumnDataSource"},"glyph":{"id":"1146","type":"Square"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1147","type":"Square"},"selection_glyph":null,"view":{"id":"1149","type":"CDSView"}},"id":"1148","type":"GlyphRenderer"},{"attributes":{},"id":"1592","type":"UnionRenderers"},{"attributes":{"line_color":"#98df8a","line_width":3,"x":{"field":"YEAR"},"y":{"field":"PDX"}},"id":"1391","type":"Line"},{"attributes":{"source":{"id":"1145","type":"ColumnDataSource"}},"id":"1149","type":"CDSView"},{"attributes":{},"id":"1596","type":"UnionRenderers"},{"attributes":{},"id":"1595","type":"Selection"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"PDX"}},"id":"1392","type":"Line"},{"attributes":{"callback":null,"end":1348.0},"id":"1044","type":"Range1d"},{"attributes":{"callback":null,"renderers":[{"id":"1148","type":"GlyphRenderer"}],"tooltips":[["Dest","ORD"],["Departures","33"]]},"id":"1150","type":"HoverTool"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1391","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1392","type":"Line"},"selection_glyph":null,"view":{"id":"1394","type":"CDSView"}},"id":"1393","type":"GlyphRenderer"},{"attributes":{"callback":null,"data":{"x":[2017],"y":[13.0]},"selected":{"id":"1597","type":"Selection"},"selection_policy":{"id":"1596","type":"UnionRenderers"}},"id":"1152","type":"ColumnDataSource"},{"attributes":{},"id":"1598","type":"UnionRenderers"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1394","type":"CDSView"},{"attributes":{"line_color":"#2ca02c","line_width":3,"x":{"field":"YEAR"},"y":{"field":"LAX"}},"id":"1353","type":"Line"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1429","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1430","type":"Line"},"selection_glyph":null,"view":{"id":"1432","type":"CDSView"}},"id":"1431","type":"GlyphRenderer"},{"attributes":{"use_scientific":false},"id":"1073","type":"BasicTickFormatter"},{"attributes":{"fill_color":{"value":"#1f77b4"},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"1153","type":"Square"},{"attributes":{},"id":"1599","type":"Selection"},{"attributes":{},"id":"1600","type":"UnionRenderers"},{"attributes":{"callback":null,"renderers":[{"id":"1393","type":"GlyphRenderer"}],"tooltips":[["Dest","PDX"],["Departures","@PDX"]]},"id":"1395","type":"HoverTool"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"1154","type":"Square"},{"attributes":{},"id":"1597","type":"Selection"},{"attributes":{"data_source":{"id":"1152","type":"ColumnDataSource"},"glyph":{"id":"1153","type":"Square"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1154","type":"Square"},"selection_glyph":null,"view":{"id":"1156","type":"CDSView"}},"id":"1155","type":"GlyphRenderer"},{"attributes":{"source":{"id":"1152","type":"ColumnDataSource"}},"id":"1156","type":"CDSView"}],"root_ids":["1039"]},"title":"Bokeh Application","version":"1.2.0"}}
                  var render_items = [{"docid":"191b529a-434f-4d71-9319-b70aa2d5f6fd","roots":{"1039":"1942ac2e-a2bd-4ff0-b5c5-770dee40c584"}}];
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
        