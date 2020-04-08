var countElements = function(arr) {    
    let d = {}
    for (let i=0; i < arr.length; i++){
        if (arr[i] in d){
            d[arr[i]] += 1;
        }
        else {
            d[arr[i]] = 1;
        }
    }
    
    let res = 0
    for (let key in d){
        // if ((key+1) in d){
        if (parseFloat(key)+1 in d){
            res += d[key];
        }
    }
    return res;
};

console.log(countElements([1,2,3]));