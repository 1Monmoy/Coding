#include<stdio.h>

int main(){
    int n;
    int D_count = 0;
    int A_count = 0;
    scanf("%d", &n);
    char a[n];
    scanf("%s", a);
    for(int i = 0; i < n; i++){
        if(a[i]=='D') D_count++;
        else if(a[i]=='A') A_count++;
        
    }
    if(A_count>D_count) printf("Anton\n");
    else if (D_count>A_count)
    {
        printf("Danik\n");
    }
    if(D_count==A_count) printf("Friendship\n");

    return 0;
}