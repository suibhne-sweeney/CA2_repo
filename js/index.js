var slider = document.getElementById("slideshow");
var count = 0;
function ExpandMenu(){
    document.getElementById("sidebar").classList.toggle("active")
    console.log("idk")
}
setInterval(function(){
 
    if(count === 0 ){
        console.log(count)
        slider.style.transform = "translateX(0)";
        count++
    }else if(count === 1){
        console.log(count)
        slider.style.transform = "translateX(-51cm)";
        count++
    }else if(count === 2){
        console.log(count)
        slider.style.transform = "translateX(-110cm)";
        count++
    }else if(count === 3){
        console.log(count)
        slider.style.transform = "translateX(-51cm)";
        count = 0
    }
}, 20000)

