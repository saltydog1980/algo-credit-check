exports.creditCheck = function(str) {
    let baseArr = str.split('')
    for (let i = 0; i < baseArr.length; i = i + 2) {
        if (baseArr[i]*2 > 9){
            num = baseArr[i]*2
            baseArr[i] = num.toString().split('').map(Number).reduce((a,b) => a+b)
        } else {
            baseArr[i] = baseArr[i]*2
        }
    }
    return baseArr.map(Number).reduce((a, b) => a + b) % 10 === 0 ? 'The number is valid!' : 'The number is invalid!'
}