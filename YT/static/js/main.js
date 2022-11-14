var input = document.getElementById("l")
var title = document.getElementById("title")
input.addEventListener("keypress",function(event){
    if(event.key == "Enter"){
        event.preventDefault();
        document.getElementById("bt").click();
        document.getElementById("search").style.display = "none";
        document.getElementById("ld").style.display = "grid";

    }
});
function myfun(){
    if(title.innerHTML.length!=0){
        document.getElementById("details").style.display="flex";
        document.getElementById("search").style.display = "none";
        document.getElementById("ld").style.display = "none";
    }
}
