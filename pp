#include<iostream>
#include<string>
using namespace std;
int num=-1;
int firstIndex(int* arr, int n, int m, int p=0){
    if(p==n-1){
        return num;
    }
    else if(arr[p]==m){
        num=p;
        return num;
    }
    else{
        firstIndex(arr, n, m, p+1);
    }
}


bool checkPallindrome(string a, int n){
    int s=0;
    int e=n-1;
    while(s<=e){
        if(a[s]!=a[e]){
            return false;
        }
        else{
            s++;
            e--;
        }
        return true;
    }
}

string Lower(string str){
    int l=str.length();
    for(int i=0; i<l; i++){
        if(str[i]>='a' && str[i]<='z'){
            continue;
        }
        else{
            str[i]=str[i]-'A'+'a';
        }
    }
    return str;
}

char maxOccChar(string s){
    int arr[26]={0};
    int n=s.length();
    for(int i=0; i<n; i++){
        int num=s[i]-'a';
        arr[num]++;
    }
    int max=0;
    for(int i=1; i<26; i++){
        if(arr[i]>arr[max]){
            max=i;
        }
    }
    char t=(char)('a'+max);
    return t;
}

int main() {
    string p="htrhfg";
	cout<<checkPallindrome(p, 6);
	cout<<endl<<p.length()<<endl;
	cout<<Lower("yASh")<<endl;
	string h;
//	getline(cin,h);
//	cout<<h;
	cout<<maxOccChar("lilly");
}
