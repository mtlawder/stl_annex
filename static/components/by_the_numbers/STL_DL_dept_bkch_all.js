
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json ={"1d15d098-93b7-4b5a-9e12-24dbd6d49509":{"roots":{"references":[{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MEM"}},"id":"1336","type":"Line"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1398","type":"CDSView"},{"attributes":{"callback":null,"end":2018.3,"start":2010},"id":"1042","type":"Range1d"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1245","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1246","type":"Line"},"selection_glyph":null,"view":{"id":"1248","type":"CDSView"}},"id":"1247","type":"GlyphRenderer"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1335","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1336","type":"Line"},"selection_glyph":null,"view":{"id":"1338","type":"CDSView"}},"id":"1337","type":"GlyphRenderer"},{"attributes":{"callback":null,"renderers":[{"id":"1397","type":"GlyphRenderer"}],"tooltips":[["Dest","ATL"],["Departures","@ATL"]]},"id":"1399","type":"HoverTool"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1248","type":"CDSView"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1338","type":"CDSView"},{"attributes":{"callback":null,"renderers":[{"id":"1247","type":"GlyphRenderer"}],"tooltips":[["Dest","JFK"],["Departures","@JFK"]]},"id":"1249","type":"HoverTool"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1458","type":"CDSView"},{"attributes":{"callback":null,"renderers":[{"id":"1187","type":"GlyphRenderer"}],"tooltips":[["Dest","SEA"],["Departures","@SEA"]]},"id":"1189","type":"HoverTool"},{"attributes":{"callback":null,"renderers":[{"id":"1337","type":"GlyphRenderer"}],"tooltips":[["Dest","MEM"],["Departures","@MEM"]]},"id":"1339","type":"HoverTool"},{"attributes":{"line_color":"#ff9896","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MEM"}},"id":"1335","type":"Line"},{"attributes":{},"id":"1061","type":"WheelZoomTool"},{"attributes":{"callback":null,"renderers":[{"id":"1277","type":"GlyphRenderer"}],"tooltips":[["Dest","LGA"],["Departures","@LGA"]]},"id":"1279","type":"HoverTool"},{"attributes":{},"id":"1048","type":"LinearScale"},{"attributes":{"text":"Departures to/from STL"},"id":"1040","type":"Title"},{"attributes":{},"id":"1051","type":"BasicTicker"},{"attributes":{"overlay":{"id":"1546","type":"BoxAnnotation"}},"id":"1062","type":"BoxZoomTool"},{"attributes":{"callback":null,"data":{"ATL":{"__ndarray__":"AAAAAABMtkAAAAAAAAe1QAAAAAAAoLVAAAAAAADZtUAAAAAAAHC1QAAAAAAAnrVAAAAAAACGtUAAAAAAAB21QAAAAAAARrVA","dtype":"float64","shape":[9]},"CVG":{"__ndarray__":"AAAAAADAh0AAAAAAABCGQAAAAAAAmJRAAAAAAADAmkAAAAAAAAyXQAAAAAAAQJFAAAAAAADEkEAAAAAAACSQQAAAAAAAsJBA","dtype":"float64","shape":[9]},"DCA":{"__ndarray__":"AAAAAACAdEAAAAAAALCaQAAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"DTW":{"__ndarray__":"AAAAAABarEAAAAAAAEKtQAAAAAAASqtAAAAAAAA0rUAAAAAAALCoQAAAAAAAoqlAAAAAAAAoqkAAAAAAAEqsQAAAAAAATqxA","dtype":"float64","shape":[9]},"JFK":{"__ndarray__":"AAAAAACAWUAAAAAAAAA7QAAAAAAAgHlAAAAAAAAghkAAAAAAAOCFQAAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"LGA":{"__ndarray__":"AAAAAADghUAAAAAAAKiCQAAAAAAANqFAAAAAAAD0okAAAAAAAKSiQAAAAAAAiqVAAAAAAAAYqUAAAAAAAJapQAAAAAAA+qlA","dtype":"float64","shape":[9]},"MCO":{"__ndarray__":"AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAABJQAAAAAAAAD1A","dtype":"float64","shape":[9]},"MEM":{"__ndarray__":"AAAAAAB8mUAAAAAAALCbQAAAAAAAyJpAAAAAAAA4gkAAAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"MSP":{"__ndarray__":"AAAAAAD4rEAAAAAAACiuQAAAAAAAFbBAAAAAAAAnsEAAAAAAAEauQAAAAAAAsK5AAAAAAADwrUAAAAAAAKitQAAAAAAAqq1A","dtype":"float64","shape":[9]},"RDU":{"__ndarray__":"AAAAAABAWEAAAAAAAFBzQAAAAAAA0IBAAAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"SEA":{"__ndarray__":"AAAAAAAAJkAAAAAAAAAyQAAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"SLC":{"__ndarray__":"AAAAAAAMm0AAAAAAAKCgQAAAAAAAKJ9AAAAAAABknkAAAAAAAPiVQAAAAAAAUJZAAAAAAACglUAAAAAAAOyUQAAAAAAAHJpA","dtype":"float64","shape":[9]},"YEAR":[2010,2011,2012,2013,2014,2015,2016,2017,2018]},"selected":{"id":"1547","type":"Selection"},"selection_policy":{"id":"1548","type":"UnionRenderers"}},"id":"1002","type":"ColumnDataSource"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1455","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1456","type":"Line"},"selection_glyph":null,"view":{"id":"1458","type":"CDSView"}},"id":"1457","type":"GlyphRenderer"},{"attributes":{},"id":"1056","type":"BasicTicker"},{"attributes":{},"id":"1063","type":"SaveTool"},{"attributes":{},"id":"1547","type":"Selection"},{"attributes":{"axis_label":"YEAR","formatter":{"id":"1543","type":"BasicTickFormatter"},"ticker":{"id":"1051","type":"BasicTicker"}},"id":"1050","type":"LinearAxis"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"1546","type":"BoxAnnotation"},{"attributes":{"line_color":"#aec7e8","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SLC"}},"id":"1155","type":"Line"},{"attributes":{"line_color":"#ffbb78","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DTW"}},"id":"1215","type":"Line"},{"attributes":{"below":[{"id":"1050","type":"LinearAxis"}],"center":[{"id":"1054","type":"Grid"},{"id":"1059","type":"Grid"}],"left":[{"id":"1055","type":"LinearAxis"}],"plot_height":400,"plot_width":370,"renderers":[{"id":"1127","type":"GlyphRenderer"},{"id":"1157","type":"GlyphRenderer"},{"id":"1187","type":"GlyphRenderer"},{"id":"1217","type":"GlyphRenderer"},{"id":"1247","type":"GlyphRenderer"},{"id":"1277","type":"GlyphRenderer"},{"id":"1307","type":"GlyphRenderer"},{"id":"1337","type":"GlyphRenderer"},{"id":"1367","type":"GlyphRenderer"},{"id":"1397","type":"GlyphRenderer"},{"id":"1427","type":"GlyphRenderer"},{"id":"1457","type":"GlyphRenderer"}],"title":{"id":"1040","type":"Title"},"toolbar":{"id":"1066","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"1042","type":"Range1d"},"x_scale":{"id":"1046","type":"LinearScale"},"y_range":{"id":"1044","type":"Range1d"},"y_scale":{"id":"1048","type":"LinearScale"}},"id":"1039","subtype":"Figure","type":"Plot"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SLC"}},"id":"1156","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DTW"}},"id":"1216","type":"Line"},{"attributes":{},"id":"1543","type":"BasicTickFormatter"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1155","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1156","type":"Line"},"selection_glyph":null,"view":{"id":"1158","type":"CDSView"}},"id":"1157","type":"GlyphRenderer"},{"attributes":{},"id":"1548","type":"UnionRenderers"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1215","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1216","type":"Line"},"selection_glyph":null,"view":{"id":"1218","type":"CDSView"}},"id":"1217","type":"GlyphRenderer"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DCA"}},"id":"1456","type":"Line"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1158","type":"CDSView"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1218","type":"CDSView"},{"attributes":{"line_color":"#8c564b","line_width":3,"x":{"field":"YEAR"},"y":{"field":"CVG"}},"id":"1425","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"1157","type":"GlyphRenderer"}],"tooltips":[["Dest","SLC"],["Departures","@SLC"]]},"id":"1159","type":"HoverTool"},{"attributes":{"callback":null,"renderers":[{"id":"1217","type":"GlyphRenderer"}],"tooltips":[["Dest","DTW"],["Departures","@DTW"]]},"id":"1219","type":"HoverTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"CVG"}},"id":"1426","type":"Line"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1425","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1426","type":"Line"},"selection_glyph":null,"view":{"id":"1428","type":"CDSView"}},"id":"1427","type":"GlyphRenderer"},{"attributes":{"line_color":"#9467bd","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MSP"}},"id":"1365","type":"Line"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1188","type":"CDSView"},{"attributes":{"line_color":"#d62728","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MCO"}},"id":"1305","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MSP"}},"id":"1366","type":"Line"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1428","type":"CDSView"},{"attributes":{},"id":"1046","type":"LinearScale"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1365","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1366","type":"Line"},"selection_glyph":null,"view":{"id":"1368","type":"CDSView"}},"id":"1367","type":"GlyphRenderer"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MCO"}},"id":"1306","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"1427","type":"GlyphRenderer"}],"tooltips":[["Dest","CVG"],["Departures","@CVG"]]},"id":"1429","type":"HoverTool"},{"attributes":{"ticker":{"id":"1051","type":"BasicTicker"}},"id":"1054","type":"Grid"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1305","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1306","type":"Line"},"selection_glyph":null,"view":{"id":"1308","type":"CDSView"}},"id":"1307","type":"GlyphRenderer"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1368","type":"CDSView"},{"attributes":{"axis_label":"Departures","formatter":{"id":"1073","type":"BasicTickFormatter"},"ticker":{"id":"1056","type":"BasicTicker"}},"id":"1055","type":"LinearAxis"},{"attributes":{},"id":"1065","type":"HelpTool"},{"attributes":{"line_color":"#c49c94","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DCA"}},"id":"1455","type":"Line"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1308","type":"CDSView"},{"attributes":{"callback":null,"renderers":[{"id":"1367","type":"GlyphRenderer"}],"tooltips":[["Dest","MSP"],["Departures","@MSP"]]},"id":"1369","type":"HoverTool"},{"attributes":{"callback":null,"renderers":[{"id":"1307","type":"GlyphRenderer"}],"tooltips":[["Dest","MCO"],["Departures","@MCO"]]},"id":"1309","type":"HoverTool"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1185","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1186","type":"Line"},"selection_glyph":null,"view":{"id":"1188","type":"CDSView"}},"id":"1187","type":"GlyphRenderer"},{"attributes":{},"id":"1064","type":"ResetTool"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1278","type":"CDSView"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"JFK"}},"id":"1246","type":"Line"},{"attributes":{"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"RDU"}},"id":"1125","type":"Line"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1060","type":"PanTool"},{"id":"1061","type":"WheelZoomTool"},{"id":"1062","type":"BoxZoomTool"},{"id":"1063","type":"SaveTool"},{"id":"1064","type":"ResetTool"},{"id":"1065","type":"HelpTool"},{"id":"1129","type":"HoverTool"},{"id":"1159","type":"HoverTool"},{"id":"1189","type":"HoverTool"},{"id":"1219","type":"HoverTool"},{"id":"1249","type":"HoverTool"},{"id":"1279","type":"HoverTool"},{"id":"1309","type":"HoverTool"},{"id":"1339","type":"HoverTool"},{"id":"1369","type":"HoverTool"},{"id":"1399","type":"HoverTool"},{"id":"1429","type":"HoverTool"},{"id":"1459","type":"HoverTool"}]},"id":"1066","type":"Toolbar"},{"attributes":{"dimension":1,"ticker":{"id":"1056","type":"BasicTicker"}},"id":"1059","type":"Grid"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"RDU"}},"id":"1126","type":"Line"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1395","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1396","type":"Line"},"selection_glyph":null,"view":{"id":"1398","type":"CDSView"}},"id":"1397","type":"GlyphRenderer"},{"attributes":{"callback":null,"end":5808.0},"id":"1044","type":"Range1d"},{"attributes":{"line_color":"#98df8a","line_width":3,"x":{"field":"YEAR"},"y":{"field":"LGA"}},"id":"1275","type":"Line"},{"attributes":{},"id":"1060","type":"PanTool"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1125","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1126","type":"Line"},"selection_glyph":null,"view":{"id":"1128","type":"CDSView"}},"id":"1127","type":"GlyphRenderer"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"LGA"}},"id":"1276","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"1457","type":"GlyphRenderer"}],"tooltips":[["Dest","DCA"],["Departures","@DCA"]]},"id":"1459","type":"HoverTool"},{"attributes":{"source":{"id":"1002","type":"ColumnDataSource"}},"id":"1128","type":"CDSView"},{"attributes":{"line_color":"#c5b0d5","line_width":3,"x":{"field":"YEAR"},"y":{"field":"ATL"}},"id":"1395","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"1127","type":"GlyphRenderer"}],"tooltips":[["Dest","RDU"],["Departures","@RDU"]]},"id":"1129","type":"HoverTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"ATL"}},"id":"1396","type":"Line"},{"attributes":{"use_scientific":false},"id":"1073","type":"BasicTickFormatter"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"1186","type":"Line"},{"attributes":{"line_color":"#2ca02c","line_width":3,"x":{"field":"YEAR"},"y":{"field":"JFK"}},"id":"1245","type":"Line"},{"attributes":{"line_color":"#ff7f0e","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"1185","type":"Line"},{"attributes":{"data_source":{"id":"1002","type":"ColumnDataSource"},"glyph":{"id":"1275","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1276","type":"Line"},"selection_glyph":null,"view":{"id":"1278","type":"CDSView"}},"id":"1277","type":"GlyphRenderer"}],"root_ids":["1039"]},"title":"Bokeh Application","version":"1.2.0"}}
                  var render_items = [{"docid":"1d15d098-93b7-4b5a-9e12-24dbd6d49509","roots":{"1039":"9667a624-486d-4642-aa7f-23647db63ef3"}}];
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
        