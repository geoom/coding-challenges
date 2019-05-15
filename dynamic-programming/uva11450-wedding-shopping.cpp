#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

int M, C, K, price[25][25]; // price[garment_id (<= 20)][model (<= 20)]
int memo[210][25]; // dp table memo[money_left (<= 200)][garment_id (<= 20)]

int shop(int money_left, int garment_int){
    if (money_left < 0)
        return -100000000000;  // fail, return a large negative number
    if (garment_id == C) // we have bought last garment
        return M - money_left;
    if (memo[money_left][garment_id] != -1) // if this state has been visited before
        return memo[money_left][garment_id];
    
    int max_value = -100000000000;
    
    for (int model = 1; model <= price[garment_id][0]; model++)
        max_value = max(max_value, shop(money_left - price[garment_id][model], garment_id + 1));
    
    return memo[money_left][garment_id] = max_value;
}

int main(){
    int i, j, TC, score;

    scanf("%d", &TC);
    while (TC--){
        scanf("%d %d", &M, &C);
        for ( i = 0; i < C; i++){
            scanf("%d", &K);
            price[i][0] = K; // store K in price[i][0]
            for(j = 1; j <= K; j++){
                scanf("&d", &price[i][j]);
            }
        }

        memset(memo, -1, sizeof memo); // init DP memo table
        score = shop(M, 0); // start the top-down dp
        if(score < 0)
            printf("no solution \n");
        else
            printf("&d\n", score);
    }
} // return 0