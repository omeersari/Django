$(document).ready(function(){
  
  $('.slider').slider({
    fullWidth : true
  });
  $('.sidenav').sidenav();
  $('.collapsible').collapsible();
  

  $("input[type='submit']").click(function(){
    var radioValue = $("input[name='{{c.cevap_soru}}']:checked").val();
              console.log(radioValue);
      
  });
});


