#include <stdio.h>

int main()
{
    int a, b;

    printf("Geben sie die erste Zahl an, dessen ggT bestimmt werden soll: ");
    scanf("%i", &a);
    printf("Geben sie die zweite Zahl an, dessen ggT bestimmt werden soll: ");
    scanf("%i", &b);
    printf("Sie haben: %i und %i eingegeben \n", a, b);

    while(a != b)
    {
        if(b > a)
        {
            int tempA = a;
            int tempB = b;
            b = tempA;
            a = tempB;
        }

        a = a - b;
    }

    printf("Der ggT ist: %i \n" , a);
    system("pause");

    return 0;
}