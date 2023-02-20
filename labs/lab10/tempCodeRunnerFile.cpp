#include<bits/stdc++.h>
using namespace std;
int n,m;//n个点，m条边
int map1[1000][1000];
struct edge{
    int x;
    int val;
    int y;
}e[10000];
int head[1000];
int note;int visited[10000];
int OD[1000],ID[1000];//OD出度，ID入读
int D[1000];//度
int dfn[1000],count=1;
void init(int n){
    for(int i=0;i<=n;i++)
        head[i]=-1;
}
void add(int x,int y,int val){
    e[++node].u=x;
    e[node].v=v;
    e[node].val=val;
    e[node].next=head[u];
    head[u]=node;
}
void DFS1(int map[][],int n){
    for(int i=1;i<=n;i++)
        visited[i]=0;
    for(int i=1;i<=n;i++)
        if(!visited[i]){
            DFS2(map,i);
        }
            
}
void DFS2(int map[][],int k){
    dfn[k]=count++;
    for(int i=1;i<=n;i++)
        if(map[k][i]!=0 && (!visited[i])){
            visited[i]=1;
            cout<<k<<"->"<<i<<" ";
            DFS2(map,i);
        }
}
int main(){
    cin>>n>>m;
    for(int i=1;i<=m;i++){
        int x,y,val;
        cin>x>>y>>val;
        map1[x][y]=map1[y][x]=val;
        D[x]++,D[y]++;
    }
    /*init(n);
    for(int i=1;i<=m;i++){
        int x,y,val;
        cin>>x>>y>>val;
        add(x,y,val);
        ID[y]++,OD[x]++;
    }*/
    DFS1(map1,n);
    cout<<endl;
    for(int i=1;i<=n;i++)
    cout<<dfn[i]<<" ";
    return 0;
}
