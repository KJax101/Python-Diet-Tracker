//this is for the autocomplete function in the form
console.log(fetch)
window.onload = function () {
  const foodType = document.getElementById("foodType");
  const addItem = document.getElementById("addItem");
  const foodList = document.getElementById("foodList");

  foodType.addEventListener("change", function () {
    console.log("working");
  })
  addItem.addEventListener("click", function () {
    let list = document.createElement("li");
    console.log("working22")
    const type = document.getElementById("foodType");
    const foodName = type.innerHTML;
    console.log(foodname);
    list.createTextNode(foodName);
    foodList.appendChild(list);
  })


}