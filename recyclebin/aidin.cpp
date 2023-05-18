#include <iostream>
#include <vector>
using namespace std;
string proxy;
int i = 0;
int x = 0;
vector<string> vct = {"-1","-1","-1","-1"};
int recursive()
{

    if(i == 4)
    {
        if (vct[0] + vct[1] + vct[2] + vct[3] == proxy)
        {
        
            for(int l = 0;l < 4;l++)
            {
                if (vct[l] == "-1")
                {
                    return 0;
                }

            }   
            for(int l = 0;l < 4;l++)
            {
                cout << vct[l];
                if(l < 3)
                {
                    cout << '.';
                }
            }
            cout << endl;
        }

        return 0;

    }
    string v = proxy;
    int a = 0;
    int changer = 0;
    int j = 0;
    for(int j = 0;j < x + i + 1;j++)
    {
    
        a = int(v[0]) - 48;
        v.erase(v.begin() + 0);
        
    }
    int q = 0;
    bool flag = false;
    for(int o = 0;o < 3;o++)
    {
        
        if (flag == true)
        {
            if (v.length() > 0)
            {
                a *= 10;
                a += int(v[0]) - 48;
                v.erase(0 + v.begin());
                x += 1;
                q += 1;

            }
            else
            {
                return 0;
            }
        }

        
        if (a >= 0) 
        {
             if(a <= 255)
            {
                vct[i] = to_string(a);
                
                
                i += 1;
                recursive();
                flag = true;
                i -= 1;
                
                for(int k = i; k < 4 ;k++)
                {
                    vct[k] = "-1";
                }
                if(v.length() == 0)
                {
                    x -= q;
                    return 0;
                }

            }
            
        }
       
    }
    x -= q;
    return 0;

}



int main()
{
    cin >> proxy;
    int i = 0;
    recursive();

    return 0;
}