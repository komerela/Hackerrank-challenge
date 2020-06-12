#include <stdio.h>
#include <string.h>

/**
 * toLowerCase - takes in a string and returns the same string with all characters lowercase
 * @str: the string to convert
 * Return: the converted string
 */

char * toLowerCase(char * str){
    int i;
    for (i = 0; i < strlen(str); i++)
        if (str[i] >= 'A' && str[i] <= 'Z')
            str[i] += ('a' - 'A');
    return (str);
}

/**
 * main - entry point
 * Return: always 0
 */

int main(){
    char string[] = "UPPERCASElowercaseUPPERCASE";
    printf("%s\n", string);
    printf("%s\n", toLowerCase(string));
    return 0;
}