
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json ={"ae73ee33-8880-4651-82fb-8bec0656bf4b":{"roots":{"references":[{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"2411","type":"Line"},{"attributes":{},"id":"2266","type":"PanTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DCA"}},"id":"2718","type":"Line"},{"attributes":{},"id":"2474","type":"UnionRenderers"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"2266","type":"PanTool"},{"id":"2267","type":"WheelZoomTool"},{"id":"2268","type":"BoxZoomTool"},{"id":"2269","type":"SaveTool"},{"id":"2270","type":"ResetTool"},{"id":"2271","type":"HelpTool"},{"id":"2363","type":"HoverTool"},{"id":"2393","type":"HoverTool"},{"id":"2423","type":"HoverTool"},{"id":"2430","type":"HoverTool"},{"id":"2476","type":"HoverTool"},{"id":"2508","type":"HoverTool"},{"id":"2540","type":"HoverTool"},{"id":"2572","type":"HoverTool"},{"id":"2604","type":"HoverTool"},{"id":"2636","type":"HoverTool"},{"id":"2668","type":"HoverTool"},{"id":"2700","type":"HoverTool"},{"id":"2732","type":"HoverTool"}]},"id":"2272","type":"Toolbar"},{"attributes":{"data_source":{"id":"2242","type":"ColumnDataSource"},"glyph":{"id":"2410","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2411","type":"Line"},"selection_glyph":null,"view":{"id":"2413","type":"CDSView"}},"id":"2412","type":"GlyphRenderer"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MEM"}},"id":"2590","type":"Line"},{"attributes":{"below":[{"id":"2256","type":"LinearAxis"}],"center":[{"id":"2260","type":"Grid"},{"id":"2265","type":"Grid"},{"id":"2361","type":"Legend"}],"left":[{"id":"2261","type":"LinearAxis"}],"plot_height":400,"plot_width":425,"renderers":[{"id":"2353","type":"GlyphRenderer"},{"id":"2382","type":"GlyphRenderer"},{"id":"2412","type":"GlyphRenderer"},{"id":"2428","type":"GlyphRenderer"},{"id":"2463","type":"GlyphRenderer"},{"id":"2495","type":"GlyphRenderer"},{"id":"2527","type":"GlyphRenderer"},{"id":"2559","type":"GlyphRenderer"},{"id":"2591","type":"GlyphRenderer"},{"id":"2623","type":"GlyphRenderer"},{"id":"2655","type":"GlyphRenderer"},{"id":"2687","type":"GlyphRenderer"},{"id":"2719","type":"GlyphRenderer"}],"title":{"id":"2246","type":"Title"},"toolbar":{"id":"2272","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"2248","type":"Range1d"},"x_scale":{"id":"2252","type":"LinearScale"},"y_range":{"id":"2250","type":"Range1d"},"y_scale":{"id":"2254","type":"LinearScale"}},"id":"2245","subtype":"Figure","type":"Plot"},{"attributes":{"data_source":{"id":"2242","type":"ColumnDataSource"},"glyph":{"id":"2717","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2718","type":"Line"},"selection_glyph":null,"view":{"id":"2720","type":"CDSView"}},"id":"2719","type":"GlyphRenderer"},{"attributes":{"label":{"value":"DTW"},"renderers":[{"id":"2463","type":"GlyphRenderer"}]},"id":"2475","type":"LegendItem"},{"attributes":{"data_source":{"id":"2242","type":"ColumnDataSource"},"glyph":{"id":"2589","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2590","type":"Line"},"selection_glyph":null,"view":{"id":"2592","type":"CDSView"}},"id":"2591","type":"GlyphRenderer"},{"attributes":{"dimension":1,"ticker":{"id":"2262","type":"BasicTicker"}},"id":"2265","type":"Grid"},{"attributes":{"source":{"id":"2242","type":"ColumnDataSource"}},"id":"2413","type":"CDSView"},{"attributes":{"callback":null,"data":{"ATL":{"__ndarray__":"AAAAAJDS8UAAAAAAAPGxQAAAAAAAhqlAAAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"CVG":{"__ndarray__":"AAAAAMAs4UAAAAAA4PHgQAAAAADA2u1AAAAAADAr8UAAAAAAYIbvQAAAAABgv+dAAAAAAECj5UAAAAAAYLjjQAAAAABg4eJA","dtype":"float64","shape":[9]},"DCA":{"__ndarray__":"AAAAAAA/vEAAAAAAgM/tQAAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"DTW":{"__ndarray__":"AAAAANDT8kAAAAAAQP35QAAAAAC41gBBAAAAACAAAUEAAAAAwHH5QAAAAADgL/pAAAAAANBR/EAAAAAASJcCQQAAAACAXgVB","dtype":"float64","shape":[9]},"JFK":{"__ndarray__":"AAAAAAD2tEAAAAAAAIyVQAAAAACAadVAAAAAAOAU4UAAAAAAQILgQAAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"LGA":{"__ndarray__":"AAAAAICx10AAAAAAwPTSQAAAAACwR/VAAAAAALAN/UAAAAAA8Jr8QAAAAACgMQFBAAAAAIjJBEEAAAAAsGYFQQAAAABofgZB","dtype":"float64","shape":[9]},"MCO":{"__ndarray__":"AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAJynQAAAAAAArJtA","dtype":"float64","shape":[9]},"MEM":{"__ndarray__":"AAAAAHBF8kAAAAAAADryQAAAAAAARPJAAAAAAMCl1UAAAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"MSP":{"__ndarray__":"AAAAAIAc+UAAAAAAUGf9QAAAAADIlgFBAAAAALDe/kAAAAAA0BbzQAAAAAAgvPNAAAAAAADg7kAAAAAAYLLuQAAAAAAgIvRA","dtype":"float64","shape":[9]},"RDU":{"__ndarray__":"AAAAAAA6rEAAAAAAgL/GQAAAAAAAZtJAAAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"SEA":{"__ndarray__":"AAAAAAAA+H8AAAAAACycQAAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"SLC":{"__ndarray__":"AAAAAID16kAAAAAAgAb5QAAAAABwe/NAAAAAAFAx8EAAAAAAAFLcQAAAAAAA5udAAAAAAOAK5EAAAAAAAADlQAAAAABgPPRA","dtype":"float64","shape":[9]},"YEAR":[2010,2011,2012,2013,2014,2015,2016,2017,2018]},"selected":{"id":"2390","type":"Selection"},"selection_policy":{"id":"2391","type":"UnionRenderers"}},"id":"2242","type":"ColumnDataSource"},{"attributes":{"callback":null,"renderers":[{"id":"2463","type":"GlyphRenderer"}],"tooltips":[["Dest","DTW"],["Passengers","@DTW"]]},"id":"2476","type":"HoverTool"},{"attributes":{"source":{"id":"2242","type":"ColumnDataSource"}},"id":"2720","type":"CDSView"},{"attributes":{"label":{"value":"SEA"},"renderers":[{"id":"2412","type":"GlyphRenderer"}]},"id":"2422","type":"LegendItem"},{"attributes":{"line_color":"#98df8a","line_width":3,"x":{"field":"YEAR"},"y":{"field":"LGA"}},"id":"2525","type":"Line"},{"attributes":{"source":{"id":"2242","type":"ColumnDataSource"}},"id":"2592","type":"CDSView"},{"attributes":{},"id":"2252","type":"LinearScale"},{"attributes":{"label":{"value":"DCA"},"renderers":[{"id":"2719","type":"GlyphRenderer"}]},"id":"2731","type":"LegendItem"},{"attributes":{"label":{"value":"MEM"},"renderers":[{"id":"2591","type":"GlyphRenderer"}]},"id":"2603","type":"LegendItem"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"LGA"}},"id":"2526","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"2412","type":"GlyphRenderer"}],"tooltips":[["Dest","SEA"],["Passengers","@SEA"]]},"id":"2423","type":"HoverTool"},{"attributes":{"data_source":{"id":"2242","type":"ColumnDataSource"},"glyph":{"id":"2525","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2526","type":"Line"},"selection_glyph":null,"view":{"id":"2528","type":"CDSView"}},"id":"2527","type":"GlyphRenderer"},{"attributes":{"callback":null,"renderers":[{"id":"2719","type":"GlyphRenderer"}],"tooltips":[["Dest","DCA"],["Passengers","@DCA"]]},"id":"2732","type":"HoverTool"},{"attributes":{"callback":null,"renderers":[{"id":"2591","type":"GlyphRenderer"}],"tooltips":[["Dest","MEM"],["Passengers","@MEM"]]},"id":"2604","type":"HoverTool"},{"attributes":{"callback":null,"data":{"x":[2011],"y":[1803.0]},"selected":{"id":"2473","type":"Selection"},"selection_policy":{"id":"2474","type":"UnionRenderers"}},"id":"2425","type":"ColumnDataSource"},{"attributes":{},"id":"2254","type":"LinearScale"},{"attributes":{"source":{"id":"2242","type":"ColumnDataSource"}},"id":"2528","type":"CDSView"},{"attributes":{"callback":null,"renderers":[{"id":"2353","type":"GlyphRenderer"}],"tooltips":[["Dest","RDU"],["Passengers","@RDU"]]},"id":"2363","type":"HoverTool"},{"attributes":{"label":{"value":"LGA"},"renderers":[{"id":"2527","type":"GlyphRenderer"}]},"id":"2539","type":"LegendItem"},{"attributes":{"fill_color":{"value":"#ff7f0e"},"line_color":{"value":"#ff7f0e"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"2426","type":"Square"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"ATL"}},"id":"2654","type":"Line"},{"attributes":{},"id":"2271","type":"HelpTool"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"2427","type":"Square"},{"attributes":{"callback":null,"renderers":[{"id":"2527","type":"GlyphRenderer"}],"tooltips":[["Dest","LGA"],["Passengers","@LGA"]]},"id":"2540","type":"HoverTool"},{"attributes":{"data_source":{"id":"2425","type":"ColumnDataSource"},"glyph":{"id":"2426","type":"Square"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2427","type":"Square"},"selection_glyph":null,"view":{"id":"2429","type":"CDSView"}},"id":"2428","type":"GlyphRenderer"},{"attributes":{"use_scientific":false},"id":"2279","type":"BasicTickFormatter"},{"attributes":{"ticker":{"id":"2257","type":"BasicTicker"}},"id":"2260","type":"Grid"},{"attributes":{"source":{"id":"2425","type":"ColumnDataSource"}},"id":"2429","type":"CDSView"},{"attributes":{},"id":"2267","type":"WheelZoomTool"},{"attributes":{"overlay":{"id":"2360","type":"BoxAnnotation"}},"id":"2268","type":"BoxZoomTool"},{"attributes":{"callback":null,"renderers":[{"id":"2428","type":"GlyphRenderer"}],"tooltips":[["Dest","SEA"],["Passengers","1803"]]},"id":"2430","type":"HoverTool"},{"attributes":{"source":{"id":"2242","type":"ColumnDataSource"}},"id":"2464","type":"CDSView"},{"attributes":{"callback":null,"end":189269.0},"id":"2250","type":"Range1d"},{"attributes":{"text":"Passengers flying out/in STL"},"id":"2246","type":"Title"},{"attributes":{"line_color":"#aec7e8","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SLC"}},"id":"2380","type":"Line"},{"attributes":{},"id":"2269","type":"SaveTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SLC"}},"id":"2381","type":"Line"},{"attributes":{"line_color":"#c5b0d5","line_width":3,"x":{"field":"YEAR"},"y":{"field":"ATL"}},"id":"2653","type":"Line"},{"attributes":{},"id":"2270","type":"ResetTool"},{"attributes":{"data_source":{"id":"2242","type":"ColumnDataSource"},"glyph":{"id":"2380","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2381","type":"Line"},"selection_glyph":null,"view":{"id":"2383","type":"CDSView"}},"id":"2382","type":"GlyphRenderer"},{"attributes":{"source":{"id":"2242","type":"ColumnDataSource"}},"id":"2383","type":"CDSView"},{"attributes":{"line_color":"#d62728","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MCO"}},"id":"2557","type":"Line"},{"attributes":{"line_color":"#8c564b","line_width":3,"x":{"field":"YEAR"},"y":{"field":"CVG"}},"id":"2685","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MCO"}},"id":"2558","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"CVG"}},"id":"2686","type":"Line"},{"attributes":{},"id":"2390","type":"Selection"},{"attributes":{"data_source":{"id":"2242","type":"ColumnDataSource"},"glyph":{"id":"2685","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2686","type":"Line"},"selection_glyph":null,"view":{"id":"2688","type":"CDSView"}},"id":"2687","type":"GlyphRenderer"},{"attributes":{"data_source":{"id":"2242","type":"ColumnDataSource"},"glyph":{"id":"2557","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2558","type":"Line"},"selection_glyph":null,"view":{"id":"2560","type":"CDSView"}},"id":"2559","type":"GlyphRenderer"},{"attributes":{},"id":"2391","type":"UnionRenderers"},{"attributes":{"callback":null,"end":2019.98,"start":2010},"id":"2248","type":"Range1d"},{"attributes":{"line_color":"#2ca02c","line_width":3,"x":{"field":"YEAR"},"y":{"field":"JFK"}},"id":"2493","type":"Line"},{"attributes":{"label":{"value":"SLC"},"renderers":[{"id":"2382","type":"GlyphRenderer"}]},"id":"2392","type":"LegendItem"},{"attributes":{"source":{"id":"2242","type":"ColumnDataSource"}},"id":"2560","type":"CDSView"},{"attributes":{"source":{"id":"2242","type":"ColumnDataSource"}},"id":"2688","type":"CDSView"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"JFK"}},"id":"2494","type":"Line"},{"attributes":{"label":{"value":"MCO"},"renderers":[{"id":"2559","type":"GlyphRenderer"}]},"id":"2571","type":"LegendItem"},{"attributes":{"label":{"value":"CVG"},"renderers":[{"id":"2687","type":"GlyphRenderer"}]},"id":"2699","type":"LegendItem"},{"attributes":{},"id":"2473","type":"Selection"},{"attributes":{"callback":null,"renderers":[{"id":"2382","type":"GlyphRenderer"}],"tooltips":[["Dest","SLC"],["Passengers","@SLC"]]},"id":"2393","type":"HoverTool"},{"attributes":{"axis_label":"YEAR","formatter":{"id":"2357","type":"BasicTickFormatter"},"ticker":{"id":"2257","type":"BasicTicker"}},"id":"2256","type":"LinearAxis"},{"attributes":{"data_source":{"id":"2242","type":"ColumnDataSource"},"glyph":{"id":"2493","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2494","type":"Line"},"selection_glyph":null,"view":{"id":"2496","type":"CDSView"}},"id":"2495","type":"GlyphRenderer"},{"attributes":{"line_color":"#9467bd","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MSP"}},"id":"2621","type":"Line"},{"attributes":{},"id":"2262","type":"BasicTicker"},{"attributes":{"data_source":{"id":"2242","type":"ColumnDataSource"},"glyph":{"id":"2461","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2462","type":"Line"},"selection_glyph":null,"view":{"id":"2464","type":"CDSView"}},"id":"2463","type":"GlyphRenderer"},{"attributes":{"callback":null,"renderers":[{"id":"2559","type":"GlyphRenderer"}],"tooltips":[["Dest","MCO"],["Passengers","@MCO"]]},"id":"2572","type":"HoverTool"},{"attributes":{"source":{"id":"2242","type":"ColumnDataSource"}},"id":"2496","type":"CDSView"},{"attributes":{"callback":null,"renderers":[{"id":"2687","type":"GlyphRenderer"}],"tooltips":[["Dest","CVG"],["Passengers","@CVG"]]},"id":"2700","type":"HoverTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MSP"}},"id":"2622","type":"Line"},{"attributes":{"label":{"value":"JFK"},"renderers":[{"id":"2495","type":"GlyphRenderer"}]},"id":"2507","type":"LegendItem"},{"attributes":{"data_source":{"id":"2242","type":"ColumnDataSource"},"glyph":{"id":"2621","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2622","type":"Line"},"selection_glyph":null,"view":{"id":"2624","type":"CDSView"}},"id":"2623","type":"GlyphRenderer"},{"attributes":{"label":{"value":"ATL"},"renderers":[{"id":"2655","type":"GlyphRenderer"}]},"id":"2667","type":"LegendItem"},{"attributes":{"callback":null,"renderers":[{"id":"2495","type":"GlyphRenderer"}],"tooltips":[["Dest","JFK"],["Passengers","@JFK"]]},"id":"2508","type":"HoverTool"},{"attributes":{"source":{"id":"2242","type":"ColumnDataSource"}},"id":"2354","type":"CDSView"},{"attributes":{"source":{"id":"2242","type":"ColumnDataSource"}},"id":"2624","type":"CDSView"},{"attributes":{"label":{"value":"MSP"},"renderers":[{"id":"2623","type":"GlyphRenderer"}]},"id":"2635","type":"LegendItem"},{"attributes":{"line_color":"#ff9896","line_width":3,"x":{"field":"YEAR"},"y":{"field":"MEM"}},"id":"2589","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"2655","type":"GlyphRenderer"}],"tooltips":[["Dest","ATL"],["Passengers","@ATL"]]},"id":"2668","type":"HoverTool"},{"attributes":{"callback":null,"renderers":[{"id":"2623","type":"GlyphRenderer"}],"tooltips":[["Dest","MSP"],["Passengers","@MSP"]]},"id":"2636","type":"HoverTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"RDU"}},"id":"2352","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DTW"}},"id":"2462","type":"Line"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"2360","type":"BoxAnnotation"},{"attributes":{"source":{"id":"2242","type":"ColumnDataSource"}},"id":"2656","type":"CDSView"},{"attributes":{"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"RDU"}},"id":"2351","type":"Line"},{"attributes":{"label":{"value":"RDU"},"renderers":[{"id":"2353","type":"GlyphRenderer"}]},"id":"2362","type":"LegendItem"},{"attributes":{},"id":"2257","type":"BasicTicker"},{"attributes":{"data_source":{"id":"2242","type":"ColumnDataSource"},"glyph":{"id":"2351","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2352","type":"Line"},"selection_glyph":null,"view":{"id":"2354","type":"CDSView"}},"id":"2353","type":"GlyphRenderer"},{"attributes":{"axis_label":"Passengers","formatter":{"id":"2279","type":"BasicTickFormatter"},"ticker":{"id":"2262","type":"BasicTicker"}},"id":"2261","type":"LinearAxis"},{"attributes":{"glyph_width":6,"items":[{"id":"2362","type":"LegendItem"},{"id":"2392","type":"LegendItem"},{"id":"2422","type":"LegendItem"},{"id":"2475","type":"LegendItem"},{"id":"2507","type":"LegendItem"},{"id":"2539","type":"LegendItem"},{"id":"2571","type":"LegendItem"},{"id":"2603","type":"LegendItem"},{"id":"2635","type":"LegendItem"},{"id":"2667","type":"LegendItem"},{"id":"2699","type":"LegendItem"},{"id":"2731","type":"LegendItem"}],"label_text_font_size":{"value":"9pt"}},"id":"2361","type":"Legend"},{"attributes":{"line_color":"#ffbb78","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DTW"}},"id":"2461","type":"Line"},{"attributes":{},"id":"2357","type":"BasicTickFormatter"},{"attributes":{"line_color":"#ff7f0e","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SEA"}},"id":"2410","type":"Line"},{"attributes":{"data_source":{"id":"2242","type":"ColumnDataSource"},"glyph":{"id":"2653","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2654","type":"Line"},"selection_glyph":null,"view":{"id":"2656","type":"CDSView"}},"id":"2655","type":"GlyphRenderer"},{"attributes":{"line_color":"#c49c94","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DCA"}},"id":"2717","type":"Line"}],"root_ids":["2245"]},"title":"Bokeh Application","version":"1.2.0"}}
                  var render_items = [{"docid":"ae73ee33-8880-4651-82fb-8bec0656bf4b","roots":{"2245":"7836798d-6f3b-4452-a533-ecf0f84074fa"}}];
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
        