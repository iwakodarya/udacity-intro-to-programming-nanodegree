/*
 * Programming Quiz: Factorials
 */
/*
 * QUIZ REQUIREMENTS
 * - Your code should use a `for` loop
 * - Your code should produce the expected output
 */

// your code goes here
let value = 6;
let factorial = 1;

for (x=value; value > 0; value--){
    factorial *=value
}

console.log(factorial)