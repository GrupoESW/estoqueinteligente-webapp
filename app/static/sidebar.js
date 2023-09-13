function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }
  
  $(document).ready(function(){
    $("#apiButton").click(function(){
      $.get("https://dev.api.dispensainteligente.com.br/example", function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
      });
    });
  });