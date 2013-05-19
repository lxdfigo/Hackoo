#include<stdio.h>
int main(int argc,char **argv)
{
  freopen("tmp.out","w",stdout);
  if (argc>1)
    printf("%s",argv[1]);
  return 0;
}
