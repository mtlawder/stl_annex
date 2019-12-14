Vue.component('header-bar',{
  data: function() {
    return{
      count:2
    }
  },
  template: '<div class="tophead">\
      <img src="/static/images/stl_map_head.jpeg" style="width:100%;min-height:180px;max-height:300px;"/>\
      <div class="tophead_center d-none d-lg-block">\
        <h1 style="margin-left:4px;margin-right:4px;"> STL Annex: A blog for data analysis</h1>\
        <h4>Matthew T. Lawder</h4>\
        <h5>matt@stlannex.com</h5>\
      </div>\
      <div class="tophead_center d-md-block d-lg-none">\
        <h4> STL Annex</h4>\
        <p style="margin-bottom:0px;">Matthew Lawder</p>\
        <p style="margin-left:4px;margin-right:4px;margin-bottom:4px;">matt@stlannex.com</p>\
      </div>\
    </div>'


}),
new Vue({ el: '#header-vue' })