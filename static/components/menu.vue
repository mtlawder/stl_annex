Vue.component('menu-bar',{
  data: function() {
    return{
      count:2
    }
  },
  template: '<nav class="navbar navbar-default">\
    	<div class="container-fluid">\
        <!-- Brand and toggle get grouped for better mobile display -->\
        <div class="navbar-header">\
          <!-- Collect the nav links, forms, and other content for toggling -->\
          <div class="" id="navbarSupportedContent">\
            <ul class="nav navbar-nav">\
              <li>\
                <a href="\index_Main"> STLAnnex Home </a>\
              </li>\
              <li>\
                <a href="\all_airlines#">Airline Project </a>\
              </li>\
              <li>\
                <a href="http://miso-epat.herokuapp.com">Wind Energy Project</a>\
              </li>\
              <li>\
                <a href="\stl_pop">STL Census</a>\
              </li>\
              <li>\
                <a href="\index_Main#blog_head">Blog Posts</a>\
              </li>\
            </ul>\
          </div>\
        <!-- /.navbar-collapse -->\
        </div>\
      <!-- /.container-fluid -->\
      </div>\
    </nav>'


}),
new Vue({ el: '#menu-vue' })