$(document).ready(function(){
  
  $('.slider').slider({
    fullWidth : true
  });
  $('.sidenav').sidenav();
  $('.collapsible').collapsible();
  

  $("#test").on("submit", function(e){
    var $form = $(this)
    var soru_cevap = {}; 
    var skor = 0;
    e.preventDefault();
    $form.find('input[type="radio"]:checked').each(function(index, elem){
      soru_cevap[elem.name] = elem.value;
    })
    
    for (key in soru_cevap) {
      if (soru_cevap[key] == "True") {
        skor += 1;
      }
    };

    console.log(soru_cevap);
    console.log(skor)
  });
});

