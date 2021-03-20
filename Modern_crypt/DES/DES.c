// Done
#include <stdio.h>
#include <string.h>
#define buffer 10000
int sbox1[4][16] = {{14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7},
                    {0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8},
                    {4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0},
                    {15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13}};
int sbox2[4][16] = {{15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10},
                    {3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5},
                    {0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15},
                    {13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9}};
int sbox3[4][16] = {{10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8},
                    {13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1},
                    {13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7},
                    {1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12}};
int sbox4[4][16] = {{7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15},
                    {13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9},
                    {10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4},
                    {3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14}};
int sbox5[4][16] = {{2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9},
                    {14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6},
                    {4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14},
                    {11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3}};
int sbox6[4][16] = {{12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11},
                    {10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8},
                    {9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6},
                    {4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13}};
int sbox7[4][16] = {{4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1},
                    {13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6},
                    {1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2},
                    {6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12}};
int sbox8[4][16] = {{13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7},
                    {1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2},
                    {7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8},
                    {2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11}};
int IP[8][8] = {{58, 50, 42, 34, 26, 18, 10, 2},
                {60, 52, 44, 36, 28, 20, 12, 4},
                {62, 54, 46, 38, 30, 22, 14, 6},
                {64, 56, 48, 40, 32, 24, 16, 8},
                {57, 49, 41, 33, 25, 17, 9, 1},
                {59, 51, 43, 35, 27, 19, 11, 3},
                {61, 53, 45, 37, 29, 21, 13, 5},
                {63, 55, 47, 39, 31, 23, 15, 7}};
int IPInverse[8][8] = {{40,8,48,16,56,24,64,32},
                       {39,7,47,15,55,23,63,31},
                       {38,6,46,14,54,22,62,30},
                       {37,5,45,13,53,21,61,29},
                       {36,4,44,12,52,20,60,28},
                       {35,3,43,11,51,19,59,27},
                       {34,2,42,10,50,18,58,26},
                       {33,1,41,9,49,17,57,25}};
int Etable[8][6] = {{32, 1, 2, 3, 4, 5},
                    {4, 5, 6, 7, 8, 9},
                    {8, 9, 10, 11, 12, 13},
                    {12, 13, 14, 15, 16, 17},
                    {16, 17, 18, 19, 20, 21},
                    {20, 21, 22, 23, 24, 25},
                    {24, 25, 26, 27, 28, 29},
                    {28, 29, 30, 31, 32, 1}};
int P[8][4] = {{16, 7, 20, 21},
               {29, 12, 28, 17},
               {1, 15, 23, 26},
               {5, 18, 31, 10},
               {2, 8, 24, 14},
               {32, 27, 3, 9},
               {19, 13, 30, 6},
               {22, 11, 4, 25}};
void tobits(char *message, int fill[][8])
{
    int i = 0;
    int ans, k = 0;
    while (message[i] != '\0')
    {
        ans = message[i];
        printf("--%d--", ans);
        int bits[8] = {};
        k = 0;
        while (k != 8)
        {
            bits[k] = ans % 2;
            fill[i][k] = ans % 2;
            ans /= 2;
            k++;
        }
        i++;
    }
}

void GetRandomKey(int key[8][8], int num)
{
    int i = 0, j = 0;
    int ans;
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 8; j++)
        {
            ans = j * i + j * 24 + 11 * num + 111 + i;
            key[i][j] = ans % 2;
        }
    }
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 8; j++)
        {
            printf("%d", key[i][j]);
        }
        printf(" ");
    }
    printf("\n");
}

void PC1(int modified_key[8][7], int size)
{
    int key[8][8] = {{0,0,0,1,0,0,1,1},
                     {0,0,1,1,0,1,0,0},
                     {0,1,0,1,0,1,1,1},
                     {0,1,1,1,1,0,0,1},
                     {1,1,0,1,1,0,1,1},
                     {1,0,1,1,1,1,0,0},
                     {1,1,0,1,1,1,1,1},
                     {1,1,1,1,0,0,0,1}};
    int i = 0, j = 0;
    int mapper[56] = {57, 49, 41, 33, 25, 17, 9,
                        1, 58, 50, 42, 34, 26, 18,
                        10, 2, 59, 51, 43, 35, 27,
                        19, 11, 3, 60, 52, 44, 36,
                        63, 55, 47, 39, 31, 23, 15,
                        7, 62, 54, 46, 38, 30, 22,
                        14, 6, 61, 53, 45, 37, 29,
                        21, 13, 5, 28, 20, 12, 4};
    int straight[64];
    for(i = 0; i <64;i++)
        straight[i] = key[i/8][i % 8];

    int index;
    for (i = 0; i < 56; i++){
        index = mapper[i] - 1;
        modified_key[i / 7][i % 7] = straight[index];
    }

    for(i=0;i<8;i++){
        for(j=0;j<7;j++){
            printf("%d",modified_key[i][j]);
        }
        printf(" ");
    }

}

void C0_D0(int key[8][7], int C0[4][7], int D0[4][7])
{
    int i, j;
    for (i = 0; i < 4; i++)
        for (j = 0; j < 7; j++)
            C0[i][j] = key[i][j];

    for (i = 4; i < 8; i++)
        for (j = 0; j < 7; j++)
            D0[i - 4][j] = key[i][j];
}

void convert_to_sixtyfour_bits(int message[][8], int size, int back[][8])
{
    int i, j;
    int extra = 64 - (size % 64);
    for (i = 0; i < (size / 8); i++)
    {
        for (j = 0; j < 8; j++)
        {
            back[i][j] = message[i][j];
        }
    }
    if (extra == 64)
        return;
    for (i = 0; i < (extra / 8); i++)
    {
        for (j = 0; j < 8; j++)
        {
            back[i + (size / 8)][j] = 0;
        }
    }
}

void DoIP(int message[][8], int encoded[][8], int size)
{
    int times = size / 64;
    int i, j, k, index, rem;
    for (i = 0; i < times; i++)
    {
        for (j = 0; j < 8; j++)
        {
            for (k = 0; k < 8; k++)
            {
                index = IP[j][k] - 1;
                rem = index % 8;
                index /= 8;
                encoded[j + i * 8][k] = message[index + i * 8][rem];
            }
        }
    }
}

void PC2(int key[8][7], int modified_key[8][6])
{
    int i, j, index, rem;
    int mapper[8][6] = {{14, 17, 11, 24, 1,5},
                        {3, 28, 15, 6, 21, 10},
                        {23, 19, 12, 4, 26, 8},
                        {16, 7, 27, 20, 13, 2},
                        {41, 52, 31, 37, 47, 55},
                        {30, 40, 51, 45, 33, 48},
                        {44, 49, 39, 56, 34, 53},
                        {46, 42, 50, 36, 29, 32}};
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 6; j++)
        {
            index = mapper[i][j] - 1;
            rem = index % 7;
            index /= 7;
            modified_key[i][j] = key[index][rem];
        }
    }
    printf("\n==== AFTER PC2 =====\n");
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 6; j++)
        {
            printf("%d", modified_key[i][j]);
        }
        printf(" ");
    }
    printf("\n");
}

void Halfsies(int message[][8], int L0[][8], int R0[][8], int start)
{
    int i, j;
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < 8; j++)
        {
            L0[i][j] = message[(start * 8) + i][j];
        }
    }
    for (i = 4; i < 8; i++)
    {
        for (j = 0; j < 8; j++)
        {
            R0[i - 4][j] = message[(start * 8) + i][j];
        }
    }
}

void Rights_to_Etable(int R0[4][8], int R0_dash[8][6])
{
    int i, j, index, rem,k=0;
    int straight[48];
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 6; j++)
        {
            index = Etable[i][j] - 1;
            rem = index % 8;
            index /= 8;
            R0_dash[i][j] = R0[index][rem];
        }
    }
    printf("\n=== R Dash ====\n");
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 6; j++)
        {
            printf("%d", R0_dash[i][j]);
        }
        printf(" ");
    }
    printf("\n");
}

void Revive_key(int C0[4][7], int D0[4][7], int revkey[8][7])
{
    int p, j;
    for (p = 0; p < 4; p++)
        for (j = 0; j < 7; j++)
            revkey[p][j] = C0[p][j];
    for (p = 0; p < 4; p++)
        for (j = 0; j < 7; j++)
            revkey[p + 4][j] = D0[p][j];
}

void Shift_left(int C0[4][7], int D0[4][7])
{
    int straight[28];
    int straight2[28];
    int i, j, k = 0;
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < 7; j++)
        {
            straight[k] = C0[i][j];
            straight2[k] = D0[i][j];
            k++;
        }
    }
    int shifted[28];
    int shifted2[28];
    for (i = 27; i >= 1; i--)
    {
        shifted[i - 1] = straight[i];
        shifted2[i - 1] = straight2[i];
    }
    shifted[27] = straight[0];
    shifted2[27] = straight2[0];
    k = 0;
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < 7; j++)
        {
            C0[i][j] = shifted[k];
            D0[i][j] = shifted2[k];
            k++;
        }
    }
}

void get_For_Sbox(int res[8][6], int ans[8][4])
{
    int i, start = 8, col = 0, row = 0, mid;
    row = (2 * res[0][0]) + res[0][5];
    for (i = 1; i < 5; i++)
    {
        col += res[0][i] * start;
        start /= 2;
    }
    mid = sbox1[row][col];
    for (i = 3; i >= 0; i--)
    {
        ans[0][i] = mid % 2;
        mid /= 2;
    }
    start = 8;
    col = 0;
    row = 2 * res[1][0] + res[1][5];
    for (i = 1; i < 5; i++)
    {
        col += (res[1][i] * start);
        start /= 2;
    }
    mid = sbox2[row][col];
    for (i = 3; i >= 0; i--)
    {
        ans[1][i] = mid % 2;
        mid /= 2;
    }
    row = 2 * res[2][0] + res[2][5];
    start = 8;
    col = 0;
    for (i = 1; i < 5; i++)
    {
        col += res[2][i] * start;
        start /= 2;
    }
    mid = sbox3[row][col];
    for (i = 3; i >= 0; i--)
    {
        ans[2][i] = mid % 2;
        mid /= 2;
    }
    row = 2 * res[3][0] + res[3][5];
    col = 0;
    start = 8;
    for (i = 1; i < 5; i++)
    {
        col += res[3][i] * start;
        start /= 2;
    }
    mid = sbox4[row][col];
    for (i = 3; i >= 0; i--)
    {
        ans[3][i] = mid % 2;
        mid /= 2;
    }
    row = 2 * res[4][0] + res[4][5];
    col = 0;
    start = 8;
    for (i = 1; i < 5; i++)
    {
        col += res[4][i] * start;
        start /= 2;
    }
    mid = sbox5[row][col];
    for (i = 3; i >= 0; i--)
    {
        ans[4][i] = mid % 2;
        mid /= 2;
    }
    row = 2 * res[5][0] + res[5][5];
    col = 0;
    start = 8;
    for (i = 1; i < 5; i++)
    {
        col += res[5][i] * start;
        start /= 2;
    }
    mid = sbox6[row][col];
    for (i = 3; i >= 0; i--)
    {
        ans[5][i] = mid % 2;
        mid /= 2;
    }
    row = 2 * res[6][0] + res[6][5];
    col = 0;
    start = 8;
    for (i = 1; i < 5; i++)
    {
        col += res[6][i] * start;
        start /= 2;
    }
    mid = sbox7[row][col];
    for (i = 3; i >= 0; i--)
    {
        ans[6][i] = mid % 2;
        mid /= 2;
    }
    row = 2 * res[7][0] + res[7][5];
    col = 0;
    start = 8;
    for (i = 1; i < 5; i++)
    {
        col += res[7][i] * start;
        start /= 2;
    }
    mid = sbox8[row][col];
    for (i = 3; i >= 0; i--)
    {
        ans[7][i] = mid % 2;
        mid /= 2;
    }
    printf("\n===AFTER SBOX===\n");
    int j;
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 4; j++)
        {
            printf("%d", ans[i][j]);
        }
        printf(" ");
    }
}

void Apply_IP_inverse(int encoded_message[8][8],int ans[8][8]){
    int index,rem,i,j;
    for(i=0; i <8;i++){
        for(j=0; j < 8; j++){
            index = IPInverse[i][j] - 1;
            rem = index % 8;
            index/=8;
            ans[i][j] = encoded_message[index][rem];
        }
    }
    printf("\n=== LAST IP TABLE ====\n");
    for(i=0; i < 8; i++){
        for(j=0; j < 8;j++){
            printf("%d",ans[i][j]);
        }
        printf(" ");
    }
    printf("\n");
}

void Permute(int one[8][4], int res[8][4])
{
    int i, j, index, rem;
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 4; j++)
        {
            index = P[i][j] - 1;
            rem = index % 4;
            index /= 4;
            res[i][j] = one[index][rem];
        }
    }
    printf("\n=== PERMUTED ===\n");
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 4; j++)
        {
            printf("%d", res[i][j]);
        }
        printf(" ");
    }
}

void Adjust_for_Sbox(int ans[6][8], int res[8][6])
{
    int i, rem1, rem2, index1, index2;
    for (i = 0; i < 48; i++)
    {
        rem1 = i % 6;
        rem2 = i % 8;
        index1 = i / 8;
        index2 = i / 6;
        // index1 range 0-7-->so for res
        // rem1 range 0-7-->for ans
        // index2 range 0-5-->for ans
        // rem2 range 0-5--> so for res
        res[index2][rem1] = ans[index1][rem2];
    }
    int j;
    printf("\n=== SBOX ADJUSTED===\n");
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 6; j++)
        {
            printf("%d", res[i][j]);
        }
        printf(" ");
    }
}

void get_Lnext(int L0[4][8], int R0[4][8])
{
    int i, j;
    for (i = 0; i < 4; i++)
        for (j = 0; j < 8; j++)
            L0[i][j] = R0[i][j];
}

void get_next(int one[4][8], int two[8][4]){
    int i;
    for(i=0;i<32;i++)
        one[i/8][i % 8] = two[i/4][i % 4];
}

void get_Rnext(int one[8][4], int two[4][8])
{
    int i, j;
    int mid[8][4];
    for(i=0; i<32;i++)
        mid[i/4][i % 4] = two[i/8][i % 8];
    for (i = 0; i < 8; i++)
        for (j = 0; j < 4; j++)
            one[i][j] ^= mid[i][j];
    printf("\n===FINAL XOR===\n");
    for(i=0; i < 8; i++){
        for (j = 0; j < 4; j++){
            printf("%d",one[i][j]);
        }
        printf(" ");
    }
}

void DoXor(int one[8][6], int two[8][6], int res[8][6])
{
    int i, j;
    printf("\n=== XORED ===\n");
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 6; j++)
        {
            res[i][j] = one[i][j] ^ two[i][j];
            printf("%d", res[i][j]);
        }
        printf(" ");
    }
}
void Show_l0_r0(int L0[4][8], int R0[4][8], int call)
{
    printf("\n====L%d is=====\n", call);
    int i, j;
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < 8; j++)
        {
            printf("%d", L0[i][j]);
        }
        printf(" ");
    }
    printf("\n====R%d is=====\n", call);
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < 8; j++)
        {
            printf("%d", R0[i][j]);
        }
        printf(" ");
    }
}

void Reconstruct_final(int L0[4][8], int R0[0][8], int res[8][8])
{
    int i, j;
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < 8; j++)
        {
            res[i][j] = L0[i][j];
        }
    }
    for (i = 4; i < 8; i++)
    {
        for (j = 0; j < 8; j++)
        {
            res[i][j] = R0[i - 4][j];
        }
    }

    printf("\n===FINAL MESSAGE IN BITS IS====\n");
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 8; j++)
        {
            printf("%d", res[i][j]);
        }
        printf(" ");
    }
}

void Toplain_English(int x[8][8], int y[8])
{
    int i, j;
    int start = 128;
    int ans = 0;
    printf("\n");
    for (i = 0; i < 8; i++)
    {
        start = 128;
        ans = 0;
        for (j = 0; j < 8; j++)
        {
            ans += (x[i][j] * start);
            start /= 2;
        }
        printf("  %02X  ", ans);
        y[i] = ans;
    }
    printf("\n-----ENGLISH IS HARD----\n");
    for (i = 0; i < 8; i++)
        printf("%02X", y[i]);
}

void Store_key(int keyarr[8][6], int key[8][6]){
    int i,j;
    for(i = 0; i <8;i++)
        for(j=0; j < 6; j++)
            keyarr[i][j] = key[i][j];
}

void Show_key(int keyarr[8][6]){
    int i,j;
    for(i = 0; i <8;i++){
        for(j=0; j < 6; j++){
            printf("%d",keyarr[i][j]);
        }
        printf(" ");
    }
}

void LookAtParts(int C0[4][7], int D0[4][7],int size){
    int j,i;
    printf("\n----C%d----\n",size);
    for(i = 0; i <4;i++){
        for(j=0; j < 7; j++){
            printf("%d",C0[i][j]);
        }
        printf(" ");
    }
    printf("\n----D%d----\n",size);
    for(i = 0; i <4;i++){
        for(j=0; j < 7; j++){
            printf("%d",D0[i][j]);
        }
        printf(" ");
    }
}

void LookAtRevivedKey(int revkey[8][7],int size){
    int i,j;
    printf("\n---KEY %d---\n",size);
    for(i=0; i <8;i++){
        for(j=0; j < 7; j++){
            printf("%d",revkey[i][j]);
        }
        printf(" ");
    }
}

void main()
{
    printf("-----Enter the text to encode-----\n");
    char ch;
    char message[buffer] = {};
    int i = 0, j = 0;
    while ((ch = getchar()) != '\n' & ch != EOF)
        message[i++] = ch;
    int fill[8][8]={{0,0,0,0,0,0,0,1},
                    {0,0,1,0,0,0,1,1},
                    {0,1,0,0,0,1,0,1},
                    {0,1,1,0,1,1,1,1},
                    {1,0,0,0,1,0,0,1},
                    {1,0,1,0,1,0,1,1},
                    {1,1,0,0,1,1,0,1},
                    {1,1,1,0,1,1,1,1}};
    tobits(message, fill);
    printf("\n-----MESSAGE is-----\n");
    while (strlen(message)!= j)
    {
        for (int i = 0; i < 8; i++)
        {
            printf("%d", fill[j][i]);
        }
        printf(" ");
        j++;
    }
    // int size = strlen(message) * 8;
    // int more = 64 - (size % 64);
    // int final_size = strlen(message);
    // printf("\n%d\n", size);
    // printf("\n%d\n", more);
    // if (more != 64)
    // {
    //     final_size = strlen(message) + (more % 8 ? more / 8 + 1 : more / 8);
    // }
    // printf("\n%d\n", final_size);
    // int back[final_size][8];
    // convert_to_sixtyfour_bits(fill, strlen(message) * 8, back);
    // for (i = 0; i < final_size; i++)
    // {
    //     for (j = 0; j < 8; j++)
    //         printf("%d", back[i][j]);
    //     printf(" ");
    // }
    // printf("\n");
    int encoded[8][8];
    DoIP(fill, encoded, 8 * 8);
    printf("\n---MESSAGE AFTER IP IS---\n");
    for(i=0;i<8;i++){
        for(j=0;j<8;j++){
            printf("%d",encoded[i][j]);
        }printf(" ");
    }
    int L0[4][8];
    int R0[4][8];
    Halfsies(encoded, L0, R0, 0);
    Show_l0_r0(L0, R0,0);
    int R0_dash[8][6]={};
    // i = 0;
    // printf("\n");
    int key[8][7];
    printf("\n------KEY AFTER PC1------\n");
    PC1(key,12);
    int C0[4][7];
    int D0[4][7];
    C0_D0(key, C0, D0);
    LookAtParts(C0,D0,0);
    // int p;
    int keyarr[16][8][6];
    int rekey[8][7];
    int get_back[8][6];
    int ans[8][6];
    int Result[8][4];
    // int mid[8][6];
    int res[8][4];
    for (i = 1; i <= 16; i++)
    {
        if (i == 1 || i == 2 || i == 9 || i == 16)
        {
            Shift_left(C0, D0);
        }
        else
        {
            Shift_left(C0, D0);
            Shift_left(C0, D0);
        }
        LookAtParts(C0,D0,i);
        Revive_key(C0, D0, rekey);
        LookAtRevivedKey(rekey,i);
        PC2(rekey, get_back);
        Store_key(keyarr[i-1],get_back);
        Rights_to_Etable(R0, R0_dash);
        DoXor(get_back, R0_dash, ans);
        get_For_Sbox(ans, Result);
        Permute(Result, res);
        get_Rnext(res, L0);
        get_Lnext(L0, R0);
        get_next(R0, res);
    }
    Show_l0_r0(L0, R0, i- 1);
    //Deccryption: mistake in either encryption/decryption
    int encoded_message[8][8];
    int final_message[8][8];
    Reconstruct_final(R0, L0, encoded_message);
    Apply_IP_inverse(encoded_message,final_message);
    int plainenglish_message[8];
    Toplain_English(final_message, plainenglish_message);
    // DoIP(final_message,encoded_message,64);
    // Halfsies(encoded_message, R0,L0,0);
    // printf("\n===REV IP===\n");
    // for(i=0;i<8;i++){
    //     for(j=0;j<8;j++){
    //         printf("%d",encoded_message[i][j]);
    //     }printf(" ");
    // }
    // Toplain_English(encoded_message,plainenglish_message);
    // printf("\n");
    // Show_key(keyarr[0]);
    // for (i = 16; i >= 1; i--)
    // {
    //     Rights_to_Etable(L0, R0_dash);
    //     DoXor(keyarr[i-1], R0_dash, ans);
    //     get_For_Sbox(ans, Result);
    //     Permute(Result, res);
    //     get_Rnext(res, R0);
    //     get_Lnext(R0, L0);
    //     get_next(L0, res);
    //     Show_l0_r0(R0, L0, i - 1);
    // }
    // Reconstruct_final(R0,L0,encoded_message);
    // Apply_IP_inverse(final_message,encoded_message);
    // Toplain_English(final_message, plainenglish_message);
}