
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json ={"4598d19f-d9ed-4096-8f8e-1ccb97514fb8":{"roots":{"references":[{"attributes":{"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"RDU"}},"id":"2366","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"RDU"}},"id":"2367","type":"Line"},{"attributes":{"line_color":"#c5b0d5","line_width":3,"x":{"field":"YEAR"},"y":{"field":"ATL"}},"id":"2671","type":"Line"},{"attributes":{"data_source":{"id":"2243","type":"ColumnDataSource"},"glyph":{"id":"2366","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2367","type":"Line"},"selection_glyph":null,"view":{"id":"2369","type":"CDSView"}},"id":"2368","type":"GlyphRenderer"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"ATL"}},"id":"2672","type":"Line"},{"attributes":{"data_source":{"id":"2243","type":"ColumnDataSource"},"glyph":{"id":"2671","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2672","type":"Line"},"selection_glyph":null,"view":{"id":"2674","type":"CDSView"}},"id":"2673","type":"GlyphRenderer"},{"attributes":{"source":{"id":"2243","type":"ColumnDataSource"}},"id":"2369","type":"CDSView"},{"attributes":{"line_color":"#ffbb78","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DTW"}},"id":"2479","type":"Line"},{"attributes":{"source":{"id":"2243","type":"ColumnDataSource"}},"id":"2674","type":"CDSView"},{"attributes":{},"id":"2306","type":"HelpTool"},{"attributes":{"callback":null,"renderers":[{"id":"2368","type":"GlyphRenderer"}],"tooltips":[["Dest","RDU"],["Departures","@RDU"]]},"id":"2370","type":"HoverTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DTW"}},"id":"2480","type":"Line"},{"attributes":{},"id":"2304","type":"SaveTool"},{"attributes":{},"id":"2841","type":"BasicTickFormatter"},{"attributes":{"callback":null,"renderers":[{"id":"2673","type":"GlyphRenderer"}],"tooltips":[["Dest","ATL"],["Departures","@ATL"]]},"id":"2675","type":"HoverTool"},{"attributes":{"data_source":{"id":"2243","type":"ColumnDataSource"},"glyph":{"id":"2479","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2480","type":"Line"},"selection_glyph":null,"view":{"id":"2482","type":"CDSView"}},"id":"2481","type":"GlyphRenderer"},{"attributes":{"callback":null,"data":{"ATL":{"__ndarray__":"AAAAAAB8kUAAAAAAAIBXQAAAAAAAgE1AAAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"CVG":{"__ndarray__":"AAAAAACQh0AAAAAAANCFQAAAAAAAjJRAAAAAAAComkAAAAAAAPCWQAAAAAAAMJFAAAAAAAC4kEAAAAAAACSQQAAAAAAArJBA","dtype":"float64","shape":[9]},"DCA":{"__ndarray__":"AAAAAACAdEAAAAAAAKyaQAAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"DTW":{"__ndarray__":"AAAAAADYk0AAAAAAAEScQAAAAAAAgKJAAAAAAADGokAAAAAAAICbQAAAAAAAxJtAAAAAAABMnUAAAAAAAMKjQAAAAAAAEKZA","dtype":"float64","shape":[9]},"JFK":{"__ndarray__":"AAAAAABAWUAAAAAAAAA5QAAAAAAAYHlAAAAAAAAYhkAAAAAAANCFQAAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"LGA":{"__ndarray__":"AAAAAADQhUAAAAAAAGCCQAAAAAAAMqFAAAAAAADyokAAAAAAAJ6iQAAAAAAAgqVAAAAAAAAYqUAAAAAAAJKpQAAAAAAA+KlA","dtype":"float64","shape":[9]},"MCO":{"__ndarray__":"AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAABJQAAAAAAAADxA","dtype":"float64","shape":[9]},"MEM":{"__ndarray__":"AAAAAABkmUAAAAAAAASZQAAAAAAAuJpAAAAAAAA4gkAAAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"MSP":{"__ndarray__":"AAAAAAC0mUAAAAAAACCeQAAAAAAA/qFAAAAAAAAyoEAAAAAAADyTQAAAAAAAtJNAAAAAAAAAkEAAAAAAALyQQAAAAAAA8JRA","dtype":"float64","shape":[9]},"RDU":{"__ndarray__":"AAAAAABAWEAAAAAAAFBzQAAAAAAAwIBAAAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"SEA":{"__ndarray__":"AAAAAAAA+H8AAAAAAAAqQAAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"SLC":{"__ndarray__":"AAAAAAD4iUAAAAAAADSYQAAAAAAAxJNAAAAAAAAEkUAAAAAAAMB7QAAAAAAAiIdAAAAAAADog0AAAAAAACiFQAAAAAAAiJNA","dtype":"float64","shape":[9]},"YEAR":[2010,2011,2012,2013,2014,2015,2016,2017,2018]},"selected":{"id":"2845","type":"Selection"},"selection_policy":{"id":"2846","type":"UnionRenderers"}},"id":"2243","type":"ColumnDataSource"},{"attributes":{"line_color":"#c49c94","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DCA"}},"id":"2735","type":"Line"},{"attributes":{"line_color":"#ff9896","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MEM"}},"id":"2607","type":"Line"},{"attributes":{"callback":null,"end":2018.3,"start":2010},"id":"2283","type":"Range1d"},{"attributes":{"axis_label":"YEAR","formatter":{"id":"2841","type":"BasicTickFormatter"},"ticker":{"id":"2292","type":"BasicTicker"}},"id":"2291","type":"LinearAxis"},{"attributes":{"source":{"id":"2243","type":"ColumnDataSource"}},"id":"2482","type":"CDSView"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DCA"}},"id":"2736","type":"Line"},{"attributes":{"axis_label":"Departures","formatter":{"id":"2314","type":"BasicTickFormatter"},"ticker":{"id":"2297","type":"BasicTicker"}},"id":"2296","type":"LinearAxis"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MEM"}},"id":"2608","type":"Line"},{"attributes":{"data_source":{"id":"2243","type":"ColumnDataSource"},"glyph":{"id":"2735","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2736","type":"Line"},"selection_glyph":null,"view":{"id":"2738","type":"CDSView"}},"id":"2737","type":"GlyphRenderer"},{"attributes":{"callback":null,"renderers":[{"id":"2481","type":"GlyphRenderer"}],"tooltips":[["Dest","DTW"],["Departures","@DTW"]]},"id":"2483","type":"HoverTool"},{"attributes":{"data_source":{"id":"2243","type":"ColumnDataSource"},"glyph":{"id":"2607","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2608","type":"Line"},"selection_glyph":null,"view":{"id":"2610","type":"CDSView"}},"id":"2609","type":"GlyphRenderer"},{"attributes":{},"id":"2297","type":"BasicTicker"},{"attributes":{},"id":"2292","type":"BasicTicker"},{"attributes":{"source":{"id":"2243","type":"ColumnDataSource"}},"id":"2738","type":"CDSView"},{"attributes":{"line_color":"#98df8a","line_width":3,"x":{"field":"YEAR"},"y":{"field":"LGA"}},"id":"2543","type":"Line"},{"attributes":{"source":{"id":"2243","type":"ColumnDataSource"}},"id":"2610","type":"CDSView"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"LGA"}},"id":"2544","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"2737","type":"GlyphRenderer"}],"tooltips":[["Dest","DCA"],["Departures","@DCA"]]},"id":"2739","type":"HoverTool"},{"attributes":{"callback":null,"renderers":[{"id":"2609","type":"GlyphRenderer"}],"tooltips":[["Dest","MEM"],["Departures","@MEM"]]},"id":"2611","type":"HoverTool"},{"attributes":{"data_source":{"id":"2243","type":"ColumnDataSource"},"glyph":{"id":"2543","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2544","type":"Line"},"selection_glyph":null,"view":{"id":"2546","type":"CDSView"}},"id":"2545","type":"GlyphRenderer"},{"attributes":{},"id":"2845","type":"Selection"},{"attributes":{},"id":"2305","type":"ResetTool"},{"attributes":{"line_color":"#ff7f0e","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"2433","type":"Line"},{"attributes":{"source":{"id":"2243","type":"ColumnDataSource"}},"id":"2546","type":"CDSView"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"2434","type":"Line"},{"attributes":{"data_source":{"id":"2243","type":"ColumnDataSource"},"glyph":{"id":"2433","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2434","type":"Line"},"selection_glyph":null,"view":{"id":"2436","type":"CDSView"}},"id":"2435","type":"GlyphRenderer"},{"attributes":{"callback":null,"end":3424.0},"id":"2285","type":"Range1d"},{"attributes":{"source":{"id":"2243","type":"ColumnDataSource"}},"id":"2436","type":"CDSView"},{"attributes":{"callback":null,"renderers":[{"id":"2435","type":"GlyphRenderer"}],"tooltips":[["Dest","SEA"],["Departures","@SEA"]]},"id":"2437","type":"HoverTool"},{"attributes":{"dimension":1,"ticker":{"id":"2297","type":"BasicTicker"}},"id":"2300","type":"Grid"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"2301","type":"PanTool"},{"id":"2302","type":"WheelZoomTool"},{"id":"2303","type":"BoxZoomTool"},{"id":"2304","type":"SaveTool"},{"id":"2305","type":"ResetTool"},{"id":"2306","type":"HelpTool"},{"id":"2370","type":"HoverTool"},{"id":"2400","type":"HoverTool"},{"id":"2437","type":"HoverTool"},{"id":"2444","type":"HoverTool"},{"id":"2483","type":"HoverTool"},{"id":"2515","type":"HoverTool"},{"id":"2547","type":"HoverTool"},{"id":"2579","type":"HoverTool"},{"id":"2611","type":"HoverTool"},{"id":"2643","type":"HoverTool"},{"id":"2675","type":"HoverTool"},{"id":"2707","type":"HoverTool"},{"id":"2739","type":"HoverTool"}]},"id":"2307","type":"Toolbar"},{"attributes":{"callback":null,"data":{"x":[2011],"y":[13.0]},"selected":{"id":"2847","type":"Selection"},"selection_policy":{"id":"2848","type":"UnionRenderers"}},"id":"2439","type":"ColumnDataSource"},{"attributes":{"below":[{"id":"2291","type":"LinearAxis"}],"center":[{"id":"2295","type":"Grid"},{"id":"2300","type":"Grid"}],"left":[{"id":"2296","type":"LinearAxis"}],"plot_height":400,"plot_width":370,"renderers":[{"id":"2368","type":"GlyphRenderer"},{"id":"2398","type":"GlyphRenderer"},{"id":"2435","type":"GlyphRenderer"},{"id":"2442","type":"GlyphRenderer"},{"id":"2481","type":"GlyphRenderer"},{"id":"2513","type":"GlyphRenderer"},{"id":"2545","type":"GlyphRenderer"},{"id":"2577","type":"GlyphRenderer"},{"id":"2609","type":"GlyphRenderer"},{"id":"2641","type":"GlyphRenderer"},{"id":"2673","type":"GlyphRenderer"},{"id":"2705","type":"GlyphRenderer"},{"id":"2737","type":"GlyphRenderer"}],"title":{"id":"2281","type":"Title"},"toolbar":{"id":"2307","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"2283","type":"Range1d"},"x_scale":{"id":"2287","type":"LinearScale"},"y_range":{"id":"2285","type":"Range1d"},"y_scale":{"id":"2289","type":"LinearScale"}},"id":"2280","subtype":"Figure","type":"Plot"},{"attributes":{"fill_color":{"value":"#ff7f0e"},"line_color":{"value":"#ff7f0e"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"2440","type":"Square"},{"attributes":{},"id":"2302","type":"WheelZoomTool"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"2441","type":"Square"},{"attributes":{"data_source":{"id":"2439","type":"ColumnDataSource"},"glyph":{"id":"2440","type":"Square"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2441","type":"Square"},"selection_glyph":null,"view":{"id":"2443","type":"CDSView"}},"id":"2442","type":"GlyphRenderer"},{"attributes":{"line_color":"#aec7e8","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SLC"}},"id":"2396","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SLC"}},"id":"2397","type":"Line"},{"attributes":{"source":{"id":"2439","type":"ColumnDataSource"}},"id":"2443","type":"CDSView"},{"attributes":{"line_color":"#d62728","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MCO"}},"id":"2575","type":"Line"},{"attributes":{"text":"Departures to/from STL"},"id":"2281","type":"Title"},{"attributes":{"line_color":"#8c564b","line_width":3,"x":{"field":"YEAR"},"y":{"field":"CVG"}},"id":"2703","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"CVG"}},"id":"2704","type":"Line"},{"attributes":{"data_source":{"id":"2243","type":"ColumnDataSource"},"glyph":{"id":"2396","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2397","type":"Line"},"selection_glyph":null,"view":{"id":"2399","type":"CDSView"}},"id":"2398","type":"GlyphRenderer"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MCO"}},"id":"2576","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"2442","type":"GlyphRenderer"}],"tooltips":[["Dest","SEA"],["Departures","13"]]},"id":"2444","type":"HoverTool"},{"attributes":{"data_source":{"id":"2243","type":"ColumnDataSource"},"glyph":{"id":"2575","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2576","type":"Line"},"selection_glyph":null,"view":{"id":"2578","type":"CDSView"}},"id":"2577","type":"GlyphRenderer"},{"attributes":{"data_source":{"id":"2243","type":"ColumnDataSource"},"glyph":{"id":"2703","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2704","type":"Line"},"selection_glyph":null,"view":{"id":"2706","type":"CDSView"}},"id":"2705","type":"GlyphRenderer"},{"attributes":{"source":{"id":"2243","type":"ColumnDataSource"}},"id":"2399","type":"CDSView"},{"attributes":{},"id":"2846","type":"UnionRenderers"},{"attributes":{"line_color":"#2ca02c","line_width":3,"x":{"field":"YEAR"},"y":{"field":"JFK"}},"id":"2511","type":"Line"},{"attributes":{"source":{"id":"2243","type":"ColumnDataSource"}},"id":"2578","type":"CDSView"},{"attributes":{"source":{"id":"2243","type":"ColumnDataSource"}},"id":"2706","type":"CDSView"},{"attributes":{"ticker":{"id":"2292","type":"BasicTicker"}},"id":"2295","type":"Grid"},{"attributes":{},"id":"2847","type":"Selection"},{"attributes":{"callback":null,"renderers":[{"id":"2398","type":"GlyphRenderer"}],"tooltips":[["Dest","SLC"],["Departures","@SLC"]]},"id":"2400","type":"HoverTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"JFK"}},"id":"2512","type":"Line"},{"attributes":{"use_scientific":false},"id":"2314","type":"BasicTickFormatter"},{"attributes":{"callback":null,"renderers":[{"id":"2577","type":"GlyphRenderer"}],"tooltips":[["Dest","MCO"],["Departures","@MCO"]]},"id":"2579","type":"HoverTool"},{"attributes":{"callback":null,"renderers":[{"id":"2705","type":"GlyphRenderer"}],"tooltips":[["Dest","CVG"],["Departures","@CVG"]]},"id":"2707","type":"HoverTool"},{"attributes":{"data_source":{"id":"2243","type":"ColumnDataSource"},"glyph":{"id":"2511","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2512","type":"Line"},"selection_glyph":null,"view":{"id":"2514","type":"CDSView"}},"id":"2513","type":"GlyphRenderer"},{"attributes":{},"id":"2848","type":"UnionRenderers"},{"attributes":{},"id":"2301","type":"PanTool"},{"attributes":{"line_color":"#9467bd","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MSP"}},"id":"2639","type":"Line"},{"attributes":{"source":{"id":"2243","type":"ColumnDataSource"}},"id":"2514","type":"CDSView"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MSP"}},"id":"2640","type":"Line"},{"attributes":{},"id":"2289","type":"LinearScale"},{"attributes":{"data_source":{"id":"2243","type":"ColumnDataSource"},"glyph":{"id":"2639","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2640","type":"Line"},"selection_glyph":null,"view":{"id":"2642","type":"CDSView"}},"id":"2641","type":"GlyphRenderer"},{"attributes":{"callback":null,"renderers":[{"id":"2513","type":"GlyphRenderer"}],"tooltips":[["Dest","JFK"],["Departures","@JFK"]]},"id":"2515","type":"HoverTool"},{"attributes":{"source":{"id":"2243","type":"ColumnDataSource"}},"id":"2642","type":"CDSView"},{"attributes":{},"id":"2287","type":"LinearScale"},{"attributes":{"callback":null,"renderers":[{"id":"2545","type":"GlyphRenderer"}],"tooltips":[["Dest","LGA"],["Departures","@LGA"]]},"id":"2547","type":"HoverTool"},{"attributes":{"callback":null,"renderers":[{"id":"2641","type":"GlyphRenderer"}],"tooltips":[["Dest","MSP"],["Departures","@MSP"]]},"id":"2643","type":"HoverTool"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"2844","type":"BoxAnnotation"},{"attributes":{"overlay":{"id":"2844","type":"BoxAnnotation"}},"id":"2303","type":"BoxZoomTool"}],"root_ids":["2280"]},"title":"Bokeh Application","version":"1.2.0"}}
                  var render_items = [{"docid":"4598d19f-d9ed-4096-8f8e-1ccb97514fb8","roots":{"2280":"bdfb24e9-5786-4948-9e58-1d1dae7c3df1"}}];
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
        