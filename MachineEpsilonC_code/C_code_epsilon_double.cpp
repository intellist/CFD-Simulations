#include <iostream>
using namespace std ;
int main() 
{
 double epsilon=1.0,e=2.0;

while((e) >1)
{
epsilon=epsilon*0.5;
e=epsilon+1;
cout<<epsilon<<endl;
}
cout<<"Machine epsilon is:"<<epsilon<<endl;
return 0;
}	
