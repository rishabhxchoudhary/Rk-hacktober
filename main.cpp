/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    int x , y=0;
    char ch[50];
    cout<<"Enter String"<<endl;
    cin>>ch;

    for(x=0;ch[x]!='\0';x++)
    {
        y++;
    }
    cout<<"Reversed String Is:";

    for(x=y-1;x>=0;x--)
    {
        cout<<ch[x];
    }
}
