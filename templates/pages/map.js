          function myMap() {
            var myCenter = new google.maps.LatLng(51.650,14.709);
            var mapCanvas = document.getElementById("map");
            var mapOptions = {center: myCenter, zoom: 4};
            var map = new google.maps.Map(mapCanvas, mapOptions);
            var image = '../../../static/dot9.png'
            var image2 = '../../../static/dot10.png'
            var marker1 = new google.maps.Marker({position:{lat: 51.27159, lng: -0.20443}, icon:image});
              marker1.setMap(map);
            google.maps.event.addListener(marker1, 'click', function() {
              $('#LHR_modal').modal('toggle')
              });
              $('#LHR').on({ 
              'click': function(){ 
              marker1.setIcon("../../../static/dot10.png");}
            });
              $('#LHR_cancel').on({ 
              'click': function(){ 
              marker1.setIcon("../../../static/dot9.png");}
            });
            var marker2 = new google.maps.Marker({position:{lat: 48.646, lng: 2.330},
                          icon:image});
              marker2.setMap(map);
            google.maps.event.addListener(marker2, 'click', function() {
              $('#CDG_modal').modal('toggle')
              });
              $('#CDG').on({ 
              'click': function(){ 
              marker2.setIcon("../../../static/dot10.png");}
            });
              $('#CDG_cancel').on({ 
              'click': function(){ 
              marker2.setIcon("../../../static/dot9.png");}
            });
            var marker3 = new google.maps.Marker({position:{lat: 41.8, lng: 12.25},
                          icon:image});
              marker3.setMap(map);
            google.maps.event.addListener(marker3, 'click', function() {
              $('#FCO_modal').modal('toggle')
              });
              $('#FCO').on({ 
              'click': function(){리 
              marker3.setIcon("../../../static/dot10.png");}
            });
              $('#FCO_cancel').on({ 
              'click': function(){ 
              marker3.setIcon("../../../static/dot9.png");}
            });
            var marker4 = new google.maps.Marker({position:{lat: 40.5, lng: -3.567},
                          icon:image});
              marker4.setMap(map);
            google.maps.event.addListener(marker4, 'click', function() {
              $('#MAD_modal').modal('toggle')
              });
              $('#MAD').on({ 
              'click': function(){ 
              marker4.setIcon("../../../static/dot10.png");}
            });
              $('#MAD_cancel').on({ 
              'click': function(){ 
              marker4.setIcon("../../../static/dot9.png");}
            });
                var marker5 = new google.maps.Marker({position:{lat: 52.56, lng: 13.29},
                          icon:image});
              marker5.setMap(map);
            google.maps.event.addListener(marker5, 'click', function() {
              $('#SXF_modal').modal('toggle')
              });
              $('#SXF').on({ 
              'click': function(){ 
              marker5.setIcon("../../../static/dot10.png");}
            });
              $('#SXF_cancel').on({ 
              'click': function(){ 
              marker5.setIcon("../../../static/dot9.png");}
            });
          }


