//this is for the autocomplete function in the form
window.onload = function () {
  const foodType = document.getElementById("foodType");
  const addItem = document.getElementById("addItem");
  const foodList = document.getElementById("foodList");

  foodType.addEventListener("change", function () {
    console.log("working");
  })

  // * Efficient way to build App with 1 input field *
  // addItem.addEventListener("click", function () {
  //   let list = document.createElement("li");
  //   console.log("working22")
  //   const type = document.getElementById("foodType");
  //   const foodName = type.value;
  //   console.log(foodName);
  //   const text = document.createTextNode(foodName);
  //   list.appendChild(text);
  //   foodList.appendChild(list);
  // })


  addItem.addEventListener("click", function () {
    let formdata = new FormData();
    var foodtype = document.getElementById("foodType");
    var value = foodtype.value;
    formdata.append('food', value);
    fetch("/", { method: "POST", body: formdata }).then(function (res) {
      if (res.status === 200) {
        console.log(res);
        window.location.href = '/';
      }
    });
  })
}