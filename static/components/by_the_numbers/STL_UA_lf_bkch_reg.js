
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json ={"a0e4ad72-72f6-4223-b89e-7f3e94b468e9":{"roots":{"references":[{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"IAH"}},"id":"2942","type":"Line"},{"attributes":{"data_source":{"id":"2535","type":"ColumnDataSource"},"glyph":{"id":"3005","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"3006","type":"Line"},"selection_glyph":null,"view":{"id":"3008","type":"CDSView"}},"id":"3007","type":"GlyphRenderer"},{"attributes":{"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"LGA"}},"id":"2678","type":"Line"},{"attributes":{"line_color":"#d62728","line_width":3,"x":{"field":"YEAR"},"y":{"field":"PIT"}},"id":"2877","type":"Line"},{"attributes":{"callback":null,"data":{"CLE":{"__ndarray__":"0perLhibVkC/1ChywotVQMNMwN2AOVVA/zNfoCzrVEDeisBXQa9TQKMPS62LUlJA5J3xeO2DUUAAAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"CLT":{"__ndarray__":"L+z7ADRDUkD3S3gGLsBTQE3XZzLkZlNALjLCn/xUVEAAAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"DEN":{"__ndarray__":"U6UsiBCMVUB02dyE/MxVQH9L+7MrCFZAhEZhwiNzVkABkLC5nytWQJ9QbxV4GVZA79GVuQSYVUDtvAiifphVQHrbjE2uO1ZA","dtype":"float64","shape":[9]},"EWR":{"__ndarray__":"AAAAAAAA+H/NoJFtZVBTQAwwj7FCR1RA4j9pZ/u9VECGbog2Dp1VQMZaw+gMVlVA6uPmkPxMVkDcRab9c4BVQB0ln3JaMlVA","dtype":"float64","shape":[9]},"IAD":{"__ndarray__":"wsNsB+GRU0ARCsWXgPBTQA3HBSOKyFRAuZKdcMn7U0BIVZkU7ZxUQGAUqkRcBVVAHhngkgCwVUB7sSXnmZlVQE4dXs62c1VA","dtype":"float64","shape":[9]},"IAH":{"__ndarray__":"AAAAAAAA+H9rJozM3ihVQJheDsGK/1VAeiH0UxMaVkC7qG+OWuNVQBnfn4Su9FVAdvsKMtQuVkDMkcFHrnxVQHAJbt6qf1VA","dtype":"float64","shape":[9]},"LGA":{"__ndarray__":"AAAAAAAA+H8AAAAAAAD4f3zLt3zLd1FAAAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"ORD":{"__ndarray__":"7zUi2JPSU0B4OOgaompUQEVOt7ZK1FRAMm8SZq/lVED1GqlmifdUQPnB1F3MQFVACYg6j6JsVUBM6jVx7f1UQOANreaRZFVA","dtype":"float64","shape":[9]},"PHX":{"__ndarray__":"3eA9EQOFVUAndbkAuz5UQB+JNqM2SVVAsEUavYU2VUAAAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"PIT":{"__ndarray__":"/ewcRNX7UUBm/ruhTWRSQNu+e/qwlFNA63+8F7uBU0AAAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/","dtype":"float64","shape":[9]},"SFO":{"__ndarray__":"AAAAAAAA+H8AAAAAAAD4fwAAAAAAAPh/AAAAAAAA+H9zlxSzZEZVQGJ6mPtcclZALzy+3UhRVUBa/ZVYMRxVQD7veLAVqlVA","dtype":"float64","shape":[9]},"YEAR":[2010,2011,2012,2013,2014,2015,2016,2017,2018]},"selected":{"id":"3198","type":"Selection"},"selection_policy":{"id":"3199","type":"UnionRenderers"}},"id":"2535","type":"ColumnDataSource"},{"attributes":{"data_source":{"id":"2535","type":"ColumnDataSource"},"glyph":{"id":"2941","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2942","type":"Line"},"selection_glyph":null,"view":{"id":"2944","type":"CDSView"}},"id":"2943","type":"GlyphRenderer"},{"attributes":{"line_color":"#2ca02c","line_width":3,"x":{"field":"YEAR"},"y":{"field":"ORD"}},"id":"2813","type":"Line"},{"attributes":{"data_source":{"id":"2535","type":"ColumnDataSource"},"glyph":{"id":"2678","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2679","type":"Line"},"selection_glyph":null,"view":{"id":"2681","type":"CDSView"}},"id":"2680","type":"GlyphRenderer"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"PIT"}},"id":"2878","type":"Line"},{"attributes":{"source":{"id":"2535","type":"ColumnDataSource"}},"id":"3008","type":"CDSView"},{"attributes":{},"id":"3199","type":"UnionRenderers"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"ORD"}},"id":"2814","type":"Line"},{"attributes":{"source":{"id":"2535","type":"ColumnDataSource"}},"id":"2944","type":"CDSView"},{"attributes":{"data_source":{"id":"2535","type":"ColumnDataSource"},"glyph":{"id":"2877","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2878","type":"Line"},"selection_glyph":null,"view":{"id":"2880","type":"CDSView"}},"id":"2879","type":"GlyphRenderer"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"2627","type":"PanTool"},{"id":"2628","type":"WheelZoomTool"},{"id":"2629","type":"BoxZoomTool"},{"id":"2630","type":"SaveTool"},{"id":"2631","type":"ResetTool"},{"id":"2632","type":"HelpTool"},{"id":"2682","type":"HoverTool"},{"id":"2689","type":"HoverTool"},{"id":"2721","type":"HoverTool"},{"id":"2753","type":"HoverTool"},{"id":"2785","type":"HoverTool"},{"id":"2817","type":"HoverTool"},{"id":"2849","type":"HoverTool"},{"id":"2881","type":"HoverTool"},{"id":"2913","type":"HoverTool"},{"id":"2945","type":"HoverTool"},{"id":"2977","type":"HoverTool"},{"id":"3009","type":"HoverTool"}]},"id":"2633","type":"Toolbar"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"3202","type":"BoxAnnotation"},{"attributes":{"callback":null,"renderers":[{"id":"3007","type":"GlyphRenderer"}],"tooltips":[["Dest","CLT"],["Load Factor","@CLT"]]},"id":"3009","type":"HoverTool"},{"attributes":{},"id":"3201","type":"UnionRenderers"},{"attributes":{"data_source":{"id":"2535","type":"ColumnDataSource"},"glyph":{"id":"2813","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2814","type":"Line"},"selection_glyph":null,"view":{"id":"2816","type":"CDSView"}},"id":"2815","type":"GlyphRenderer"},{"attributes":{"source":{"id":"2535","type":"ColumnDataSource"}},"id":"2880","type":"CDSView"},{"attributes":{},"id":"3200","type":"Selection"},{"attributes":{"below":[{"id":"2617","type":"LinearAxis"}],"center":[{"id":"2621","type":"Grid"},{"id":"2626","type":"Grid"}],"left":[{"id":"2622","type":"LinearAxis"}],"plot_height":400,"plot_width":370,"renderers":[{"id":"2680","type":"GlyphRenderer"},{"id":"2687","type":"GlyphRenderer"},{"id":"2719","type":"GlyphRenderer"},{"id":"2751","type":"GlyphRenderer"},{"id":"2783","type":"GlyphRenderer"},{"id":"2815","type":"GlyphRenderer"},{"id":"2847","type":"GlyphRenderer"},{"id":"2879","type":"GlyphRenderer"},{"id":"2911","type":"GlyphRenderer"},{"id":"2943","type":"GlyphRenderer"},{"id":"2975","type":"GlyphRenderer"},{"id":"3007","type":"GlyphRenderer"}],"title":{"id":"2607","type":"Title"},"toolbar":{"id":"2633","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"2609","type":"Range1d"},"x_scale":{"id":"2613","type":"LinearScale"},"y_range":{"id":"2611","type":"Range1d"},"y_scale":{"id":"2615","type":"LinearScale"}},"id":"2606","subtype":"Figure","type":"Plot"},{"attributes":{"callback":null,"renderers":[{"id":"2943","type":"GlyphRenderer"}],"tooltips":[["Dest","IAH"],["Load Factor","@IAH"]]},"id":"2945","type":"HoverTool"},{"attributes":{"callback":null,"renderers":[{"id":"2783","type":"GlyphRenderer"}],"tooltips":[["Dest","CLE"],["Load Factor","@CLE"]]},"id":"2785","type":"HoverTool"},{"attributes":{"source":{"id":"2535","type":"ColumnDataSource"}},"id":"2816","type":"CDSView"},{"attributes":{"callback":null,"renderers":[{"id":"2751","type":"GlyphRenderer"}],"tooltips":[["Dest","DEN"],["Load Factor","@DEN"]]},"id":"2753","type":"HoverTool"},{"attributes":{"callback":null,"renderers":[{"id":"2879","type":"GlyphRenderer"}],"tooltips":[["Dest","PIT"],["Load Factor","@PIT"]]},"id":"2881","type":"HoverTool"},{"attributes":{},"id":"3198","type":"Selection"},{"attributes":{"data_source":{"id":"2535","type":"ColumnDataSource"},"glyph":{"id":"2717","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2718","type":"Line"},"selection_glyph":null,"view":{"id":"2720","type":"CDSView"}},"id":"2719","type":"GlyphRenderer"},{"attributes":{"callback":null,"renderers":[{"id":"2815","type":"GlyphRenderer"}],"tooltips":[["Dest","ORD"],["Load Factor","@ORD"]]},"id":"2817","type":"HoverTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"PHX"}},"id":"2718","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"CLT"}},"id":"3006","type":"Line"},{"attributes":{"data_source":{"id":"2535","type":"ColumnDataSource"},"glyph":{"id":"2749","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2750","type":"Line"},"selection_glyph":null,"view":{"id":"2752","type":"CDSView"}},"id":"2751","type":"GlyphRenderer"},{"attributes":{},"id":"3196","type":"BasicTickFormatter"},{"attributes":{},"id":"2613","type":"LinearScale"},{"attributes":{"use_scientific":false},"id":"2640","type":"BasicTickFormatter"},{"attributes":{"callback":null,"renderers":[{"id":"2687","type":"GlyphRenderer"}],"tooltips":[["Dest","LGA"],["Load Factor","69"]]},"id":"2689","type":"HoverTool"},{"attributes":{"callback":null,"end":100,"start":50},"id":"2611","type":"Range1d"},{"attributes":{},"id":"2615","type":"LinearScale"},{"attributes":{"source":{"id":"2684","type":"ColumnDataSource"}},"id":"2688","type":"CDSView"},{"attributes":{"text":"Load Factor"},"id":"2607","type":"Title"},{"attributes":{"line_color":"#c5b0d5","line_width":3,"x":{"field":"YEAR"},"y":{"field":"EWR"}},"id":"2973","type":"Line"},{"attributes":{"data_source":{"id":"2684","type":"ColumnDataSource"},"glyph":{"id":"2685","type":"Square"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2686","type":"Square"},"selection_glyph":null,"view":{"id":"2688","type":"CDSView"}},"id":"2687","type":"GlyphRenderer"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"EWR"}},"id":"2974","type":"Line"},{"attributes":{"line_color":"#ff9896","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SFO"}},"id":"2909","type":"Line"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"2686","type":"Square"},{"attributes":{"data_source":{"id":"2535","type":"ColumnDataSource"},"glyph":{"id":"2973","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2974","type":"Line"},"selection_glyph":null,"view":{"id":"2976","type":"CDSView"}},"id":"2975","type":"GlyphRenderer"},{"attributes":{"line_color":"#98df8a","line_width":3,"x":{"field":"YEAR"},"y":{"field":"IAD"}},"id":"2845","type":"Line"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"SFO"}},"id":"2910","type":"Line"},{"attributes":{},"id":"2632","type":"HelpTool"},{"attributes":{"source":{"id":"2535","type":"ColumnDataSource"}},"id":"2976","type":"CDSView"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"IAD"}},"id":"2846","type":"Line"},{"attributes":{},"id":"2631","type":"ResetTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"LGA"}},"id":"2679","type":"Line"},{"attributes":{"data_source":{"id":"2535","type":"ColumnDataSource"},"glyph":{"id":"2909","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2910","type":"Line"},"selection_glyph":null,"view":{"id":"2912","type":"CDSView"}},"id":"2911","type":"GlyphRenderer"},{"attributes":{"data_source":{"id":"2535","type":"ColumnDataSource"},"glyph":{"id":"2845","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2846","type":"Line"},"selection_glyph":null,"view":{"id":"2848","type":"CDSView"}},"id":"2847","type":"GlyphRenderer"},{"attributes":{"callback":null,"end":2018.3,"start":2010},"id":"2609","type":"Range1d"},{"attributes":{"source":{"id":"2535","type":"ColumnDataSource"}},"id":"2784","type":"CDSView"},{"attributes":{"callback":null,"renderers":[{"id":"2975","type":"GlyphRenderer"}],"tooltips":[["Dest","EWR"],["Load Factor","@EWR"]]},"id":"2977","type":"HoverTool"},{"attributes":{"source":{"id":"2535","type":"ColumnDataSource"}},"id":"2912","type":"CDSView"},{"attributes":{},"id":"2630","type":"SaveTool"},{"attributes":{"axis_label":"YEAR","formatter":{"id":"3196","type":"BasicTickFormatter"},"ticker":{"id":"2618","type":"BasicTicker"}},"id":"2617","type":"LinearAxis"},{"attributes":{"source":{"id":"2535","type":"ColumnDataSource"}},"id":"2848","type":"CDSView"},{"attributes":{"data_source":{"id":"2535","type":"ColumnDataSource"},"glyph":{"id":"2781","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"2782","type":"Line"},"selection_glyph":null,"view":{"id":"2784","type":"CDSView"}},"id":"2783","type":"GlyphRenderer"},{"attributes":{"overlay":{"id":"3202","type":"BoxAnnotation"}},"id":"2629","type":"BoxZoomTool"},{"attributes":{"callback":null,"renderers":[{"id":"2911","type":"GlyphRenderer"}],"tooltips":[["Dest","SFO"],["Load Factor","@SFO"]]},"id":"2913","type":"HoverTool"},{"attributes":{"fill_color":{"value":"#1f77b4"},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":8},"x":{"field":"x"},"y":{"field":"y"}},"id":"2685","type":"Square"},{"attributes":{},"id":"2628","type":"WheelZoomTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DEN"}},"id":"2750","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"2847","type":"GlyphRenderer"}],"tooltips":[["Dest","IAD"],["Load Factor","@IAD"]]},"id":"2849","type":"HoverTool"},{"attributes":{},"id":"2627","type":"PanTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"YEAR"},"y":{"field":"CLE"}},"id":"2782","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"2719","type":"GlyphRenderer"}],"tooltips":[["Dest","PHX"],["Load Factor","@PHX"]]},"id":"2721","type":"HoverTool"},{"attributes":{"line_color":"#ff7f0e","line_width":3,"x":{"field":"YEAR"},"y":{"field":"DEN"}},"id":"2749","type":"Line"},{"attributes":{"dimension":1,"ticker":{"id":"2623","type":"BasicTicker"}},"id":"2626","type":"Grid"},{"attributes":{"callback":null,"data":{"x":[2012],"y":[69.87179487179486]},"selected":{"id":"3200","type":"Selection"},"selection_policy":{"id":"3201","type":"UnionRenderers"}},"id":"2684","type":"ColumnDataSource"},{"attributes":{"axis_label":"Load Factor","formatter":{"id":"2640","type":"BasicTickFormatter"},"ticker":{"id":"2623","type":"BasicTicker"}},"id":"2622","type":"LinearAxis"},{"attributes":{},"id":"2623","type":"BasicTicker"},{"attributes":{"ticker":{"id":"2618","type":"BasicTicker"}},"id":"2621","type":"Grid"},{"attributes":{},"id":"2618","type":"BasicTicker"},{"attributes":{"line_color":"#ffbb78","line_width":3,"x":{"field":"YEAR"},"y":{"field":"CLE"}},"id":"2781","type":"Line"},{"attributes":{"line_color":"#aec7e8","line_width":3,"x":{"field":"YEAR"},"y":{"field":"PHX"}},"id":"2717","type":"Line"},{"attributes":{"callback":null,"renderers":[{"id":"2680","type":"GlyphRenderer"}],"tooltips":[["Dest","LGA"],["Load Factor","@LGA"]]},"id":"2682","type":"HoverTool"},{"attributes":{"source":{"id":"2535","type":"ColumnDataSource"}},"id":"2720","type":"CDSView"},{"attributes":{"line_color":"#8c564b","line_width":3,"x":{"field":"YEAR"},"y":{"field":"CLT"}},"id":"3005","type":"Line"},{"attributes":{"source":{"id":"2535","type":"ColumnDataSource"}},"id":"2681","type":"CDSView"},{"attributes":{"source":{"id":"2535","type":"ColumnDataSource"}},"id":"2752","type":"CDSView"},{"attributes":{"line_color":"#9467bd","line_width":3,"x":{"field":"YEAR"},"y":{"field":"IAH"}},"id":"2941","type":"Line"}],"root_ids":["2606"]},"title":"Bokeh Application","version":"1.2.0"}}
                  var render_items = [{"docid":"a0e4ad72-72f6-4223-b89e-7f3e94b468e9","roots":{"2606":"99f846f4-67bc-434f-adbe-6787b840579a"}}];
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
        