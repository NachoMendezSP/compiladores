int suma (int, int);

int suma(int k1, int k2){
  int res = (k1+k2);
  return res;
}

int resta(int x1, int x2){
  int ans = (x1-x2);
  return ans;
}

int main(int arg, char argv){

  double a = 1.1;
  int b = 1;
  int c = 4;
  int x;
  int test = 1;
  
  c = 3;
  c += 1;

  b = resta((b*c), suma(b,c));

  c = a + b;
  
  if (a > b || (a < c && c >= b)){
    int z = 0;
    int test = 4;
    z = z +1;
  }
  if(a<b)
    a++;

  return 0;
}