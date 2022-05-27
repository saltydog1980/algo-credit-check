exports.creditCheck = function(str) {
    //splitting the input string number
    let baseArr = str.split('')
    //looping over the array by 2
    for (let i = 0; i < baseArr.length; i = i + 2) {
        //if num * 2 is over 9 (over single digit) I am creating variable num by doubling the num
        if (baseArr[i]*2 > 9){
            num = baseArr[i]*2
            //I am re-assigning the value at index i to the double digit num spilt (takes to string) running map to 
            //convert back to int and then reducing the values to a single value that gets assined to the index in basearr
            baseArr[i] = num.toString().split('').map(Number).reduce((a,b) => a+b)
        } else {
            //so all single digits I am just doubling and reassigning to their original index
            baseArr[i] = baseArr[i]*2
        }
    }
    //return statement. Take baseArr to map to convert indexes we did not double into ints then reducing the entire array
    //if the reduce % 10 is zer then it returns valid else invalid
    return baseArr.map(Number).reduce((a, b) => a + b) % 10 === 0 ? 'The number is valid!' : 'The number is invalid!'
}