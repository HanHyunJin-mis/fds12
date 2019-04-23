// 절대 비교 기법 --> 함수
// function is_equal(a, b) {
//     return Math.abs(a - b) <= 1e-10;
// }
// 수가 고정되어 있어서 추상화가 깨짐

// function main() {
//     var a = 0.3;
//     var b = 0.1 * 3;

//     if (a == b) {
//         console.log("THE SAME");
//     } else {
//         console.log("NOT THE SAME");
//     }
// }

// 불리언 값이 나와야 함 

// 절대 비교 기법 --> 함수
function is_equal1(a, b) {
    return Math.abs(a - b) <= 1e-4;
}
// 수가 고정되어 있어서 추상화가 깨짐

function is_equal2(a, b, allowed = 0) {
    var ep = Number.EPSILON;
    var diff = Math.abs(a - b); // 절댓값

    return diff <= Math.max(Math.abs(a), Math.abs(b)) * ep * Math.pow(2, allowed);
}

function main() {
    var sum = 0;
    for (var i = 0; i < 100; i++) {
        sum += 0.01;
    }

    // if (sum == 1.0)
    if (is_equal2(sum, 1.0, 2)) {
        console.log("THE SAME");
    } else {
        console.log("NOT THE SAME");
    }
}



// 불리언 값이 나와야 함 