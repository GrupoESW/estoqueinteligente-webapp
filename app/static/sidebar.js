function openNav() {
    document.getElementById("mySidenav").style.width = "15%";
    document.getElementById("myDash").style.margin = "0 0 0 15%";
  }    

  function closeNav() {
    document.getElementById("mySidenav").style.width = "0%";
    document.getElementById("myDash").style.margin = "0";
  }
  
  $(document).ready(function(){
    $("#apiButton").click(function(){
      $.get("http://dev.apinode.dispensainteligente.com.br/example", function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
      });
    });
  });