#include <stdio.h>
#include <stdbool.h>

/**
 * isPalindrome - checks if an integer is a palindrome without any string conversions
 * @x: the integer to check
 * Return: 1 if the number is a palindrome
 *         0 otherwise
 */

bool isPalindrome(int x){
    int i, j, digits = 0, copy = x, end, div;
    if (x < 0)
        return 0; //Problem statement mandates a negative number is not a palindrome
    while (copy)
    {
            copy /= 10;
            digits++;
    }
    copy = x;
    end = digits/2;
    for (i = 0; i < end; i++) //loop through only half the digits. Ignores middle digit digits is odd
    {
        div = 1;
        for (j = 1; j < digits; j++)
            div *= 10;
        if (copy/div != copy%10) //check first digit against final digit
            return 0;
        copy -= (copy%10*(div + 1)); //remove first and last digits
        copy /= 10;
        digits -= 2;
    }
    return 1;
}

/**
 * main - entry point
 * Return: always 0
 */

int main(){
    bool x;
    x = isPalindrome(99999);
    return 0;
}