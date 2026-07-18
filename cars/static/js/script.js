function changeColor(color){

let car = document.getElementById("carImage");

if(color==="red"){
car.src="images/v8-red.png";
}

if(color==="black"){
car.src="images/v8-black.png";
}

if(color==="silver"){
car.src="images/v8-silver.png";
}

}

function openModal(){
document.getElementById("modal").style.display="block";
}

function closeModal(){
document.getElementById("modal").style.display="none";
}



fetch("http://127.0.0.1:8000/cars/")
  .then(res => res.json())
  .then(data => {
      console.log(data);
  });