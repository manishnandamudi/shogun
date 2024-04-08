class Test {
    constructor() {
        this.name = "Test";
    }
    isPalindrome(str) {
        const len = str.length;
        for (let i = 0; i < len / 2; i++) {
            if (str[i] !== str[len - 1 - i]) {
                return false;
            }
        }
        return true;
    }
}




function main() {
    let obj = new Test();
    obj.isPalindrome("madam0") ? console.log("Yes") : console.log("No");
}

main(); // call main function