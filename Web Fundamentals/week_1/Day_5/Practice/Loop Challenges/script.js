for (let i = 1; i <= 20; i++) {
    if (i % 2 !== 0) {
        console.log(i);
    }
}

for (let i = 100; i >= 0; i--) {
    if (i % 3 === 0) {
        console.log(i);
    }
}

let sequence = [4, 2.5, 1, -0.5, -2, -3.5];
for (let num of sequence) {
    console.log(num);
}


let sum = 0;
for (let i = 1; i <= 100; i++) {
    sum += i;
}
console.log(sum);


let product = 1;
for (let i = 1; i <= 12; i++) {
    product *= i;
}
console.log(product);
