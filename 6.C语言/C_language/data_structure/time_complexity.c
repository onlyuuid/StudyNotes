#include <stdio.h>
// 执行过程
void process(int x,int y){
    if(x>=y){
        //交换x,y的位置
        int tmp=x^y; 
        y=tmp^y;    
        x=tmp^y;
        printf("x,y的值分别为: %d %d",x,y);
    }else{
        printf("x,y的值分别为: %d %d",x,y);
    }
}
// 主函数
void main(){
    int x;
    int y;
    printf("请输入两个整数:\n");
    scanf("%d%d",&x,&y);
    process(x,y);
}


