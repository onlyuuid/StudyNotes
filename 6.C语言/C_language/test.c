#include <stdio.h>

void main(){
    int x=90;
    int y=100;
    while(y>0){
        if(x>100){
            x=x-10;
            y--;
        }else{
            x++;
        }
    }
}