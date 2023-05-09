console.log('sanity check!)')
//functions is a reusable block of code written
//to perform a single purpose.

//Functions are one of the fundamental
//building blocks in JavaScript.
function functionName(parameter){
    //code block
}
//Invoke it.
functionName(argument);
let height = 5
let width = 10
function getArea(w, h){
    console.log(w * h);
}
//invoking the method.
getArea(width, height);


let people = ['Jacky', 'Mariam', 'Michael'];
function findIndividual(person){
    for (let i = 0; i < people.length; i++){
        if (people[i] === person){
            return 'person found';
        }
    }
    people.push(person);
    return 'person added.';   
}
console.log((findIndividual('mariam')));

//an array object.
// const nums = [1,2,3,4,5];
// for(let n of nums){
//     console.log(n);
// }
const person = {name: 'janice', location: 'ca'}; // <= object literal
for(let value of person){
    console.log(value);
}
//for ... in loop
//loops over keys in an object
// for(let key in nums){
//     console.log(key);
// }