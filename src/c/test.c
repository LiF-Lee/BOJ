#include <stdio.h>

int main(void)
{
    for (int i = 1; i <= 100; i++)
    {
        _Bool condition_1 = (i - 1) % 3 == 0;
        _Bool condition_2 = (i + 1) % 5 == 0;
        _Bool condition_3 = i > 50;
        _Bool condition_4 = i % 2 == 0;
        _Bool condition_5 = (i / 100 + i / 10 % 10 + i % 10) % 2 == 0;

        if (condition_1 && condition_2 && condition_3 && condition_4 && condition_5)
        {
            printf("%d", i);
            break;
        }
    }
	return 0;
}


