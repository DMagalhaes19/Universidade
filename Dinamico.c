#include <stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<time.h>
#include<math.h>

int total_point;
int MenuThread();
int MenuPontos();
void* circle_point(void *param);

int main()
{
  int circle, i,total, opcao, pontos,num_threads;
  int opc,opc2;
  double calc;
  double a, x, y, pi;
  double PIOriginal = 3.14159265358979323846;
  clock_t start_time, end_time;
  a = 0;
  i = 0;
  circle = 0;
  do
  {
    opc = MenuPontos();
    switch(opc)
    {
      case 1: // 20000 pontos
      {
        do
        {
          opc2 = MenuThread();
          switch(opc2)
          {
            case 1: // 2 threads
            {
              system("clear");
              pontos = 20000;
              num_threads = 2;
              pthread_t tid[2]={0};
              int count[2]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 2: // 4 threads
            {
              system("clear");
              pontos = 20000;
              num_threads = 4;
              pthread_t tid[4]={0};
              int count[4]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 3: // 6 threads
            {
              system("clear");
              pontos = 20000;
              num_threads = 6;
              pthread_t tid[6]={0};
              int count[6]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 4: // 8 threads
            {
              system("clear");
              pontos = 20000;
              num_threads = 8;
              pthread_t tid[8]={0};
              int count[8]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 0:
            break;
          }
        }
        while(opc2 != 0);
      }
      case 2: // 100000
     {
        do
        {
          opc2 = MenuThread();
          switch(opc2)
          {
            case 1:
            {
              system("clear");
              pontos = 100000;
              num_threads = 2;
              pthread_t tid[2]={0};
              int count[2]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 2:
            {
              system("clear");
              pontos = 100000;
              num_threads = 4;
              pthread_t tid[4]={0};
              int count[4]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 3:
            {
              system("clear");
              pontos = 1000000;
              num_threads = 6;
              pthread_t tid[6]={0};
              int count[6]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 4:
            {
              system("clear");
              pontos = 100000;
              num_threads = 8;
              pthread_t tid[8]={0};
              int count[8]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 0:
            return 0;
          }
        }
        while(opc2 != 0);
     }
     case 3: //1000000 pontos
      {
        do
        {
          opc2 = MenuThread();
          switch(opc2)
          {
            case 1:
            {
              system("clear");
              pontos = 1000000;
              num_threads = 2;
              pthread_t tid[2]={0};
              int count[2]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 2:
            {
              system("clear");
              pontos = 1000000;
              num_threads = 2;
              pthread_t tid[2]={0};
              int count[2]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 3:
            {
              system("clear");
              pontos = 1000000;
              num_threads = 2;
              pthread_t tid[2]={0};
              int count[2]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 4:
            {
              system("clear");
              pontos = 1000000;
              num_threads = 2;
              pthread_t tid[2]={0};
              int count[2]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 0:
            break;
          }
        }
        while(opc2 != 0);
      }
      case 4: //10000000 pontos
      do
      {
          opc2 = MenuThread();
          switch(opc2)
          {
            case 1:
            {
              system("clear");
              pontos = 1000000;
              num_threads = 2;
              pthread_t tid[2]={0};
              int count[2]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 2:
            {
              system("clear");
              pontos = 1000000;
              num_threads = 4;
              pthread_t tid[4]={0};
              int count[4]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 3:
            {
              system("clear");
              pontos = 1000000;
              num_threads = 6;
              pthread_t tid[6]={0};
              int count[6]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 4:
            {
              system("clear");
              pontos = 1000000;
              num_threads = 8;
              pthread_t tid[8]={0};
              int count[8]={0};
              total_point = pontos/num_threads;
              start_time = clock();
              srand(time(NULL));
              for(i = 0; i<num_threads;i++)
              {
                pthread_create(&tid[i],NULL,circle_point,&count[i]);
              }  
              for(i=0;i<num_threads;i++)
              {
                pthread_join(tid[i],NULL);
                circle += count[i];
              }
              pi = 4.0 * (double)circle/(double)total_point/(double) num_threads;
              end_time = clock();
              calc = ((fabs(pi)-PIOriginal)/PIOriginal) * 100;
              printf("Para %d pontos, o valor de PI é= %6.5f.\nO tempo que demorou foi: %g segundos\n A estimativa de erro é= %f",pontos, pi,(double)(end_time-start_time)/CLOCKS_PER_SEC,calc);
              return 0;
            }
            case 0:
            break;
          }
      }
      while(opc2 != 0);
      case 0:
        break;
    }
  }
  while(opc != 0);
  return 0;
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

int MenuThread()
{
  int opc;
  printf(" ------ Menu ------\n");
  printf("[1] - 2 threads \n");
  printf("[2] - 4 threads \n");
  printf("[3] - 6 threads \n");
  printf("[4] - 8 threads \n");
  printf("[0]- Terminar programa \n");
  printf(" --------------------\n"); 
  printf("Introduza o número de pontos desejados: \n");
  scanf("%d", &opc);
  return opc ;
}

int MenuPontos()
{
  int opc;
  printf(" ------ Menu ------\n");
  printf("[1] - 20000 pontos \n");
  printf("[2] - 100000 pontos \n");
  printf("[3] - 1000000 pontos \n");
  printf("[4] - 10000000 pontos \n");
  printf("[0] - Terminar programa \n");
  printf(" --------------------\n"); 
  printf("Introduza o número de pontos desejados: \n");
  scanf("%d", &opc); 
  return opc;
}