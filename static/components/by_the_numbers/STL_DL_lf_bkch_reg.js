
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json ={"d74e9340-99cc-43c0-9b5a-76057956e1f2":{"roots":{"references":[{"attributes":{"data_source":{"id":"2244","type":"ColumnDataSource"},"glyph":{"id":"2646","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2647","type":"Line"},"selection_glyph":null,"view":{"id":"2649","type":"CDSView"}},"id":"2648","type":"GlyphRenderer"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"RDU"}},"id":"2374","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"2520","type":"GlyphRenderer"}],"tooltips":[["Dest","JFK"],["Load Factor","@JFK"]]},"id":"2522","type":"HoverTool"},{"attributes":{"callback":null,"renderers":[{"id":"2552","type":"GlyphRenderer"}],"tooltips":[["Dest","LGA"],["Load Factor","@LGA"]]},"id":"2554","type":"HoverTool"},{"attributes":{},"id":"2324","type":"LinearScale"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MSP"}},"id":"2647","type":"Line"},{"attributes":{},"id":"2322","type":"LinearScale"},{"attributes":{"data_source":{"id":"2244","type":"ColumnDataSource"},"glyph":{"id":"2550","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2551","type":"Line"},"selection_glyph":null,"view":{"id":"2553","type":"CDSView"}},"id":"2552","type":"GlyphRenderer"},{"attributes":{},"id":"2939","type":"UnionRenderers"},{"attributes":{"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"RDU"}},"id":"2373","type":"Line"},{"attributes":{"data_source":{"id":"2244","type":"ColumnDataSource"},"glyph":{"id":"2373","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2374","type":"Line"},"selection_glyph":null,"view":{"id":"2376","type":"CDSView"}},"id":"2375","type":"GlyphRenderer"},{"attributes":{"axis_label":"Load Factor","formatter":{"id":"2349","type":"BasicTickFormatter"},"ticker":{"id":"2332","type":"BasicTicker"}},"id":"2331","type":"LinearAxis"},{"attributes":{"source":{"id":"2244","type":"ColumnDataSource"}},"id":"2376","type":"CDSView"},{"attributes":{"line_color":"#c5b0d5","line_width":3,"x":{"field":"YEAR"},"y":{"field":"ATL"}},"id":"2678","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"ATL"}},"id":"2679","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"2375","type":"GlyphRenderer"}],"tooltips":[["Dest","RDU"],["Load Factor","@RDU"]]},"id":"2377","type":"HoverTool"},{"attributes":{"data_source":{"id":"2244","type":"ColumnDataSource"},"glyph":{"id":"2678","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2679","type":"Line"},"selection_glyph":null,"view":{"id":"2681","type":"CDSView"}},"id":"2680","type":"GlyphRenderer"},{"attributes":{"callback":null,"data":{"ATL":{"__ndarray__":"sBxKI/DTVUDOwnCHuthRQNiB8E7PZVVAAAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"CVG":{"__ndarray__":"HiY7yGe7VEC9xmh5VWJVQLit7Dak3FRAVW5XrbogUkCDgAmk0ddSQB6F3o+Pz1BA7Kz7hQ3lTUD0AEJRio5NQMixv2NplU1A","dtype":"float64","shape":[9]},"DCA":{"__ndarray__":"54sgc70mQUAeZfLQtGJLQAAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"DTW":{"__ndarray__":"jhd1uxHiVEDrwIYPnJFUQDIF3P2GhFVAaP3hc8/pVEAHtL9G6CNVQHzB7JOCh1RAp8F3Ykk5VUBUYIFLsKdUQEnbDAGWElVA","dtype":"float64","shape":[9]},"JFK":{"__ndarray__":"ZFgSbpR6UUBRXkN5DSVSQNKIaD9kH1NA2S38aky8UUDErGyGswlRQAAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"LGA":{"__ndarray__":"+cBz84feRkDhTSa2mnxGQDiddbILqk1ANS75CRmWUkD9lmgsiIVRQDt72ctFGlJAgiDK4u6aUkBWLB8DAehSQLezosi9UFJA","dtype":"float64","shape":[9]},"MCO":{"__ndarray__":"AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H9RQCbuoedUQJOpaUSiDVVA","dtype":"float64","shape":[9]},"MEM":{"__ndarray__":"Xp/ABp4cVkCdylvja7lVQOvkesW5R1VAL7KaW2DzUkAAAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"MSP":{"__ndarray__":"0PxNvT/YVEAi7HoHXgRVQPfbIf8BfVVADRaxc7yCVEB3pGNQSo5VQNYc5KS/YlZAiSsZPxGaVUADzOsSZi5UQGZ4fTq1J1VA","dtype":"float64","shape":[9]},"RDU":{"__ndarray__":"u2kgqDJ/UkBrn4USTM9SQBXGbOQSjlFAAAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"SEA":{"__ndarray__":"AAAAAAAA+H8zfufx9ZFUQAAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"SLC":{"__ndarray__":"3YP5NKjvVUBSIoGOuU9WQB7ROy3KDVZAexWTpJu/VUCwNjs4f+FVQN9eXwXHx1VA6pftBYnhVUD9SZpXFIhVQN4HdSww8VVA","dtype":"float64","shape":[9]},"YEAR":[2010,2011,2012,2013,2014,2015,2016,2017,2018]},"selected":{"id":"2936","type":"Selection"},"selection_policy":{"id":"2937","type":"UnionRenderers"}},"id":"2244","type":"ColumnDataSource"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"LGA"}},"id":"2551","type":"Line"},{"attributes":{"line_color":"#ffbb78","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DTW"}},"id":"2486","type":"Line"},{"attributes":{"source":{"id":"2244","type":"ColumnDataSource"}},"id":"2681","type":"CDSView"},{"attributes":{"source":{"id":"2244","type":"ColumnDataSource"}},"id":"2553","type":"CDSView"},{"attributes":{"axis_label":"YEAR","formatter":{"id":"2932","type":"BasicTickFormatter"},"ticker":{"id":"2327","type":"BasicTicker"}},"id":"2326","type":"LinearAxis"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DTW"}},"id":"2487","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"2680","type":"GlyphRenderer"}],"tooltips":[["Dest","ATL"],["Load Factor","@ATL"]]},"id":"2682","type":"HoverTool"},{"attributes":{"data_source":{"id":"2244","type":"ColumnDataSource"},"glyph":{"id":"2486","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2487","type":"Line"},"selection_glyph":null,"view":{"id":"2489","type":"CDSView"}},"id":"2488","type":"GlyphRenderer"},{"attributes":{"line_color":"#c49c94","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DCA"}},"id":"2742","type":"Line"},{"attributes":{"line_color":"#ff9896","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MEM"}},"id":"2614","type":"Line"},{"attributes":{"ticker":{"id":"2327","type":"BasicTicker"}},"id":"2330","type":"Grid"},{"attributes":{"source":{"id":"2244","type":"ColumnDataSource"}},"id":"2489","type":"CDSView"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DCA"}},"id":"2743","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MEM"}},"id":"2615","type":"Line"},{"attributes":{"use_scientific":false},"id":"2349","type":"BasicTickFormatter"},{"attributes":{"data_source":{"id":"2244","type":"ColumnDataSource"},"glyph":{"id":"2742","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2743","type":"Line"},"selection_glyph":null,"view":{"id":"2745","type":"CDSView"}},"id":"2744","type":"GlyphRenderer"},{"attributes":{"callback":null,"renderers":[{"id":"2488","type":"GlyphRenderer"}],"tooltips":[["Dest","DTW"],["Load Factor","@DTW"]]},"id":"2490","type":"HoverTool"},{"attributes":{"data_source":{"id":"2244","type":"ColumnDataSource"},"glyph":{"id":"2614","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2615","type":"Line"},"selection_glyph":null,"view":{"id":"2617","type":"CDSView"}},"id":"2616","type":"GlyphRenderer"},{"attributes":{"source":{"id":"2244","type":"ColumnDataSource"}},"id":"2745","type":"CDSView"},{"attributes":{"source":{"id":"2244","type":"ColumnDataSource"}},"id":"2617","type":"CDSView"},{"attributes":{},"id":"2327","type":"BasicTicker"},{"attributes":{"line_color":"#98df8a","line_width":3,"x":{"field":"YEAR"},"y":{"field":"LGA"}},"id":"2550","type":"Line"},{"attributes":{"dimension":1,"ticker":{"id":"2332","type":"BasicTicker"}},"id":"2335","type":"Grid"},{"attributes":{"callback":null,"renderers":[{"id":"2744","type":"GlyphRenderer"}],"tooltips":[["Dest","DCA"],["Load Factor","@DCA"]]},"id":"2746","type":"HoverTool"},{"attributes":{"callback":null,"renderers":[{"id":"2616","type":"GlyphRenderer"}],"tooltips":[["Dest","MEM"],["Load Factor","@MEM"]]},"id":"2618","type":"HoverTool"},{"attributes":{},"id":"2332","type":"BasicTicker"},{"attributes":{"source":{"id":"2453","type":"ColumnDataSource"}},"id":"2457","type":"CDSView"},{"attributes":{},"id":"2937","type":"UnionRenderers"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"2336","type":"PanTool"},{"id":"2337","type":"WheelZoomTool"},{"id":"2338","type":"BoxZoomTool"},{"id":"2339","type":"SaveTool"},{"id":"2340","type":"ResetTool"},{"id":"2341","type":"HelpTool"},{"id":"2377","type":"HoverTool"},{"id":"2407","type":"HoverTool"},{"id":"2451","type":"HoverTool"},{"id":"2458","type":"HoverTool"},{"id":"2490","type":"HoverTool"},{"id":"2522","type":"HoverTool"},{"id":"2554","type":"HoverTool"},{"id":"2586","type":"HoverTool"},{"id":"2618","type":"HoverTool"},{"id":"2650","type":"HoverTool"},{"id":"2682","type":"HoverTool"},{"id":"2714","type":"HoverTool"},{"id":"2746","type":"HoverTool"}]},"id":"2342","type":"Toolbar"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"2935","type":"BoxAnnotation"},{"attributes":{},"id":"2932","type":"BasicTickFormatter"},{"attributes":{},"id":"2336","type":"PanTool"},{"attributes":{},"id":"2938","type":"Selection"},{"attributes":{"callback":null,"end":2018.3,"start":2010},"id":"2318","type":"Range1d"},{"attributes":{"overlay":{"id":"2935","type":"BoxAnnotation"}},"id":"2338","type":"BoxZoomTool"},{"attributes":{"callback":null,"renderers":[{"id":"2456","type":"GlyphRenderer"}],"tooltips":[["Dest","SEA"],["Load Factor","82"]]},"id":"2458","type":"HoverTool"},{"attributes":{},"id":"2337","type":"WheelZoomTool"},{"attributes":{"line_color":"#ff7f0e","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"2447","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"2448","type":"Line"},{"attributes":{},"id":"2339","type":"SaveTool"},{"attributes":{"callback":null,"renderers":[{"id":"2648","type":"GlyphRenderer"}],"tooltips":[["Dest","MSP"],["Load Factor","@MSP"]]},"id":"2650","type":"HoverTool"},{"attributes":{},"id":"2340","type":"ResetTool"},{"attributes":{"data_source":{"id":"2244","type":"ColumnDataSource"},"glyph":{"id":"2447","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2448","type":"Line"},"selection_glyph":null,"view":{"id":"2450","type":"CDSView"}},"id":"2449","type":"GlyphRenderer"},{"attributes":{"line_color":"#aec7e8","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SLC"}},"id":"2403","type":"Line"},{"attributes":{},"id":"2341","type":"HelpTool"},{"attributes":{"source":{"id":"2244","type":"ColumnDataSource"}},"id":"2450","type":"CDSView"},{"attributes":{"callback":null,"end":100,"start":50},"id":"2320","type":"Range1d"},{"attributes":{"line_color":"#8c564b","line_width":3,"x":{"field":"YEAR"},"y":{"field":"CVG"}},"id":"2710","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SLC"}},"id":"2404","type":"Line"},{"attributes":{"line_color":"#d62728","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MCO"}},"id":"2582","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"CVG"}},"id":"2711","type":"Line"},{"attributes":{"data_source":{"id":"2244","type":"ColumnDataSource"},"glyph":{"id":"2403","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2404","type":"Line"},"selection_glyph":null,"view":{"id":"2406","type":"CDSView"}},"id":"2405","type":"GlyphRenderer"},{"attributes":{"callback":null,"renderers":[{"id":"2449","type":"GlyphRenderer"}],"tooltips":[["Dest","SEA"],["Load Factor","@SEA"]]},"id":"2451","type":"HoverTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MCO"}},"id":"2583","type":"Line"},{"attributes":{"data_source":{"id":"2244","type":"ColumnDataSource"},"glyph":{"id":"2582","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2583","type":"Line"},"selection_glyph":null,"view":{"id":"2585","type":"CDSView"}},"id":"2584","type":"GlyphRenderer"},{"attributes":{"data_source":{"id":"2244","type":"ColumnDataSource"},"glyph":{"id":"2710","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2711","type":"Line"},"selection_glyph":null,"view":{"id":"2713","type":"CDSView"}},"id":"2712","type":"GlyphRenderer"},{"attributes":{"source":{"id":"2244","type":"ColumnDataSource"}},"id":"2406","type":"CDSView"},{"attributes":{"callback":null,"data":{"x":[2011],"y":[82.28063628775344]},"selected":{"id":"2938","type":"Selection"},"selection_policy":{"id":"2939","type":"UnionRenderers"}},"id":"2453","type":"ColumnDataSource"},{"attributes":{"line_color":"#2ca02c","line_width":3,"x":{"field":"YEAR"},"y":{"field":"JFK"}},"id":"2518","type":"Line"},{"attributes":{"source":{"id":"2244","type":"ColumnDataSource"}},"id":"2713","type":"CDSView"},{"attributes":{"text":"Load Factor"},"id":"2316","type":"Title"},{"attributes":{"source":{"id":"2244","type":"ColumnDataSource"}},"id":"2585","type":"CDSView"},{"attributes":{"below":[{"id":"2326","type":"LinearAxis"}],"center":[{"id":"2330","type":"Grid"},{"id":"2335","type":"Grid"}],"left":[{"id":"2331","type":"LinearAxis"}],"plot_height":400,"plot_width":370,"renderers":[{"id":"2375","type":"GlyphRenderer"},{"id":"2405","type":"GlyphRenderer"},{"id":"2449","type":"GlyphRenderer"},{"id":"2456","type":"GlyphRenderer"},{"id":"2488","type":"GlyphRenderer"},{"id":"2520","type":"GlyphRenderer"},{"id":"2552","type":"GlyphRenderer"},{"id":"2584","type":"GlyphRenderer"},{"id":"2616","type":"GlyphRenderer"},{"id":"2648","type":"GlyphRenderer"},{"id":"2680","type":"GlyphRenderer"},{"id":"2712","type":"GlyphRenderer"},{"id":"2744","type":"GlyphRenderer"}],"title":{"id":"2316","type":"Title"},"toolbar":{"id":"2342","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"2318","type":"Range1d"},"x_scale":{"id":"2322","type":"LinearScale"},"y_range":{"id":"2320","type":"Range1d"},"y_scale":{"id":"2324","type":"LinearScale"}},"id":"2315","subtype":"Figure","type":"Plot"},{"attributes":{"callback":null,"renderers":[{"id":"2405","type":"GlyphRenderer"}],"tooltips":[["Dest","SLC"],["Load Factor","@SLC"]]},"id":"2407","type":"HoverTool"},{"attributes":{"fill_color":{"value":"#ff7f0e"},"line_color":{"value":"#ff7f0e"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"2454","type":"Square"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"JFK"}},"id":"2519","type":"Line"},{"attributes":{"source":{"id":"2244","type":"ColumnDataSource"}},"id":"2649","type":"CDSView"},{"attributes":{"callback":null,"renderers":[{"id":"2584","type":"GlyphRenderer"}],"tooltips":[["Dest","MCO"],["Load Factor","@MCO"]]},"id":"2586","type":"HoverTool"},{"attributes":{"callback":null,"renderers":[{"id":"2712","type":"GlyphRenderer"}],"tooltips":[["Dest","CVG"],["Load Factor","@CVG"]]},"id":"2714","type":"HoverTool"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"2455","type":"Square"},{"attributes":{"data_source":{"id":"2244","type":"ColumnDataSource"},"glyph":{"id":"2518","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2519","type":"Line"},"selection_glyph":null,"view":{"id":"2521","type":"CDSView"}},"id":"2520","type":"GlyphRenderer"},{"attributes":{"line_color":"#9467bd","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MSP"}},"id":"2646","type":"Line"},{"attributes":{"data_source":{"id":"2453","type":"ColumnDataSource"},"glyph":{"id":"2454","type":"Square"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2455","type":"Square"},"selection_glyph":null,"view":{"id":"2457","type":"CDSView"}},"id":"2456","type":"GlyphRenderer"},{"attributes":{"source":{"id":"2244","type":"ColumnDataSource"}},"id":"2521","type":"CDSView"},{"attributes":{},"id":"2936","type":"Selection"}],"root_ids":["2315"]},"title":"Bokeh Application","version":"1.2.0"}}
                  var render_items = [{"docid":"d74e9340-99cc-43c0-9b5a-76057956e1f2","roots":{"2315":"8dd858c3-21cb-460c-a733-dd89cf86eb8f"}}];
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
        