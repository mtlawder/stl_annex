Vue.component('menu-bar',{
  data: function() {
    return{
      count:2
    }
  },
  template: '<nav class="navbar fixed-top navbar-expand-lg navbar-light bg-light">\
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\
    <span class="navbar-toggler-icon"></span>\
  </button>\
  <div class="collapse navbar-collapse" id="navbarSupportedContent">\
    <ul class="navbar-nav mr-auto">\
      <li class="nav-item">\
        <a class="nav-link" href="../index_Main"> STLAnnex Home </a>\
      </li>\
      <li class="nav-item">\
        <a class="nav-link" href="../all_airlines#page-start">Airline Project </a>\
      </li>\
      <li class="nav-item">\
        <a class="nav-link" href="http://miso-epat.herokuapp.com">Wind Energy Project</a>\
      </li>\
      <li class="nav-item">\
        <a class="nav-link" href="../stl_pop">STL Census</a>\
      </li>\
      <li class="nav-item">\
        <a class="nav-link" href="../all_blogs">Blog Posts</a>\
      </li>\
      <li class="nav-item">\
        <a class="nav-link" href="../about">About</a>\
      </li>\
    </ul>\
  </div>\
</nav>'


}),
new Vue({ el: '#menu-vue' })