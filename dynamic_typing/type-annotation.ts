function addTwo(x: number, y: number): string {
    return String(x) + String(y);
}

let msg = addTwo("Hello", " World");  // Type error
console.log(msg);
