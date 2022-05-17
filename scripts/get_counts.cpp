#include <cstdio>
#include <string>
#include <iostream>
#include <cwchar>
#include <unordered_map>


using namespace std;

int main() {
    FILE *fp;
    fp = fopen("/Users/owlus/Downloads/RC_2019-12.json", "r");
    unordered_map<wstring, size_t> counts;

    for (size_t i = 0; i < 146000000; ++i) {
        wchar_t tmp[16000], tmp1[100], tmp2[100];
        wstring s, s1, s2;
        fgetws(tmp, 16000, fp);
        s = tmp;
        size_t n = s.find(L"subreddit_id");
        if(n + 35 >= s.size())
            continue;
        s2 = s.substr(n + 15, 20);
        n = s2.find(L"\"");
        s2 = s2.substr(0, n);

        n = s.find(L"author_fullname");
        if(n + 38 >= s.size())
            continue;
        s1 = s.substr(n + 18, 20);
        n = s1.find(L"\"");
        s1 = s1.substr(0, n);

        counts[s1 + L"$" + s2]++;
        if(i % 1000000 == 0) {
            cout << "Got " << i << endl;
        }
    }
    freopen("subr_stats_c++_19_12.txt", "w", stdout);
    for (auto& x : counts)
        wcout << x.first << L":" << x.second << L"\n";
    return 0;
}