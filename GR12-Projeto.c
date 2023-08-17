#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <pthread.h>

#define NUM_THREAD 2
#define NUM_THREAD2 4
#define NUM_THREAD3 6
#define NUM_THREAD4 8

pthread_t tid[NUM_THREAD]={0};
int count[NUM_THREAD]={0};

pthread_t tid2[NUM_THREAD2]={0};
int count2[NUM_THREAD2]={0};

pthread_t tid3[NUM_THREAD3]={0};
int count3[NUM_THREAD3]={0};

pthread_t tid4[NUM_THREAD4]={0};
int count4[NUM_THREAD4]={0};

int total_point;

void* circle_point(void *param);

int main ()
{
    int circle, i,total, opcao, pontos;
    double a, x, y, pi;
    clock_t start_time, end_time;

    a = 0;
    i = 0;
    circle = 0;
    printf(" ------ Menu ------\n");
    printf("1 - 20000 pontos \n");
    printf("2 - 100000 pontos \n");
    printf("3 - 1000000 pontos \n");
    printf("4 - 10000000 pontos \n");
    printf("0 - Terminar programa \n");
    printf(" --------------------\n"); 
    printf("Introduza o número de pontos desejados: \n");
    scanf("%d", &opcao); 
    switch(opcao)
    {
        case 1:
            system("clear");
            pontos = 20000;
            total_point = pontos/NUM_THREAD;

            start_time = clock();
            srand(time(NULL));//tempos diferentes
            for(i=0;i<NUM_THREAD;i++)
            {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
            }
            for(i=0;i<NUM_THREAD;i++)
            {
                pthread_join(tid[i],NULL);
                circle += count[i];
            }
            pi = 4.0 * (double)circle/(double)total_point/(double) NUM_THREAD;
            end_time = clock();
            printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC);
            break;
        case 2:
            system("clear");
            pontos = 100000;
            total_point = pontos/NUM_THREAD2;

            start_time = clock();
            srand(time(NULL));//tempos diferentes
            for(i=0;i<NUM_THREAD2;i++)
            {
                pthread_create(&tid2[i],NULL,circle_point,&count2[i]);
            }
            for(i=0;i<NUM_THREAD2;i++)
            {
                pthread_join(tid2[i],NULL);
                circle += count2[i];
            }
            pi = 4.0 * (double)circle/(double)total_point/(double) NUM_THREAD2;
            end_time = clock();
            printf("Para %d pontos, o valor de PI é= %6.5f.\n.O tempo que demorou foi: %g segundos",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC);
            break;
        case 3:
            system("clear");
            pontos = 1000000;
            total_point = pontos/NUM_THREAD3;

            start_time = clock();
            srand(time(NULL));//tempos diferentes
            for(i=0;i<NUM_THREAD3;i++)
            {
                pthread_create(&tid3[i],NULL,circle_point,&count3[i]);
            }
            for(i=0;i<NUM_THREAD3;i++)
            {
                pthread_join(tid3[i],NULL);
                circle += count3[i];
            }
            pi = 4.0 * (double)circle/(double)total_point/(double) NUM_THREAD3;
            end_time = clock();
            printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC);
            break;
        case 4:
            system("clear");
            pontos = 10000000;
            total_point = pontos/NUM_THREAD4;

            start_time = clock();
            srand(time(NULL));//tempos diferentes
            for(i=0;i<NUM_THREAD4;i++)
            {
                pthread_create(&tid4[i],NULL,circle_point,&count4[i]);
            }
            for(i=0;i<NUM_THREAD4;i++)
            {
                pthread_join(tid4[i],NULL);
                circle += count4[i];
            }
            pi = 4.0 * (double)circle/(double)total_point/(double) NUM_THREAD4;
            end_time = clock();
            printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC);
            break;
        case 0:
            system("clear");
            break;
        default:
            system("clear");
            printf("Opção invalida\n");
            break;
    }
}

void* circle_point(void *param){

   int *pcount= (int*)param;
   int i;
   for(i=0; i<total_point;i++){
       double x= (double)rand()/(double)RAND_MAX;
       double y=(double)rand()/(double)RAND_MAX;
       double r= x*x+y*y;
       if(r<=1) *pcount=*pcount+1;
     }
   pthread_exit(0);
}