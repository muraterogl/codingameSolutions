#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define CARD_LENGTH 16
#define CARD_STRING_LENGTH 19

void verifier(char*);

int main()
{
    int n;
    scanf("%d", &n); fgetc(stdin);
    for (int i = 0; i < n; i++) {
        char card[21];
        scanf("%[^\n]", card); fgetc(stdin);
        verifier(card);
    }
    return 0;
}

void verifier(char* cardString){
    int card[CARD_LENGTH];
    int iterator = 0;
    for(int i = 0; i < CARD_STRING_LENGTH; i++){
        if (i != 4 && i!= 9 && i!=14){
            card[iterator] = cardString[i] - '0';
            iterator++;
        }
    }
    int sum = 0;
    for(int i = 0; i < CARD_LENGTH; i++){
        if (i%2>0){
            sum += card[i];
        }
        else{
            int factor = card[i] * 2;
            sum += factor < 10 ? factor : factor - 9;
        }
    }
    
    printf(sum % 10 == 0 ? "YES\n" : "NO\n");
}