#include<iostream>
#include<algorithm>
using namespace std;


int main(){
    int t;
    cin>>t;

    while(t--){

        int n;
        cin>>n;
        int arr[n];
        // int m;
        // cin>>m;
        int arr2[n];

        for(int i=0;i<n;i++){
            cin>>arr[i];
        }

        for(int i=0;i<n;i++){
            cin>>arr2[i];
        }

        int mx=-1;

        for(int i=0;i<n;i++){
            mx=max(mx,arr[i]);
        }

        int total=0;
        for(int i=0;i<n;i++){
            total+=arr[i];
        }

        cout<<min(total,mx)<<endl;


    }
}