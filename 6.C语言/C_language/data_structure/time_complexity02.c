#include <stdio.h>
#include <time.h>

// 入口函数
void main(){
    int type = 0;           // 执行方式0或1
    int n = 100000000;      // 定义n的规模
    int result = 0;         // 计算结果
    clock_t start_time = clock();
    if(type == 0){
       for(int i=0;i<=n;i++){
            result+=i; 
        }
    }else{
        result = n*(n+1)/2;
    }
    clock_t end_time = clock();
    double excuteTime = (double)(end_time - start_time) / CLOCKS_PER_SEC; // 单位秒钟 s
    printf("程序执行时间: %f \n",excuteTime);
    printf("计算结果: %d \n",result);
}