// const arr1 = ["Cecilie", "Lone"];
// const arr2 = ["Emil", "Tobias", "Linus"];
// const children = arr1.concat(arr2);
// console.log(arr1)

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// let text = fruits.join(" and ");
// console.log(text)


const numbers = [65, 44, 12, 4];
const newArr = numbers.map(myFunction)

function myFunction(num) {
    console.log(num * 10)
}
myFunction()