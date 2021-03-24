Vue.component('btn-links',{
  data: function() {
    return{
      count:2
    }
  },
  template: '<div>\
          <u>Other By the Numbers posts</u><br>\
          <a href="\delta_stl_by_the_numbers">Delta at St. Louis-Lambert</a>\
          <br>\
          <a href="\\frontier_stl_by_the_numbers">Frontier at St. Louis-Lambert</a>\
          <br>\
          <a href="\\united_stl_by_the_numbers">United at St. Louis-Lambert</a>\
          <br>\
          <a href="\allegiant_blv_by_the_numbers">Allegiant at MidAmerica-St. Louis</a>\
          <br>\
          <a href="\american_stl_by_the_numbers">American at St. Louis-Lambert</a>\
          <br>\
          <a href="\airchoiceone_stl_by_the_numbers">Air Choice One at St. Louis-Lambert</a>\
          <br>\
          <a href="\alaska_stl_by_the_numbers">Alaska at St. Louis-Lambert</a>\
          <br>\
          <a href="\\btn_methodology">Methodology for By the Numbers Posts</a>\
          <hr>\
        </div>\
  </div>'
}),
new Vue({ el: '#btn-links-vue' })