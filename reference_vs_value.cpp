/*  Nick Sweeting 2013/10/09
    References vs Values in C++
    MIT License
    Takes input and removes puctuation, using two different methods.
    It is referred from: https://github.com/pirate/Cpp-Data-Structures/
    
    Abhishek Sharma 2022/09/22
*/

#include <stdlib.h>
#include <iostream>
#include <string.h>
using namespace std;

// returns true if input character q is puctuation, else false
bool ispunctuation(char q) {
    // complete the functions here ...
    if (q!=32){
        for(int i = 48; i<57; i++){
            if (q == i) {return  false;}
        }
        for(int i = 65; i<91; i++){
            if (q == i){return false;}
        }
        for(int i = 97; i<123; i++){
            if (q == i) {return  false;}
        }

        return true;
    }
    else{return false;}

}

char* modifyAndCopy(char* raw_input, char* empty_input) {
    // complete the functions here ...
    int a = strlen(raw_input);
    
    int j = 0;
    for (int i = 0; i < a; i++){
        if(ispunctuation(raw_input[i])){
        }
        else {
            empty_input[j] = raw_input[i];
            j++;
        }
    }
    return empty_input;
}


char* modifyInPlace(char *raw_input) {
    // complete the functions here ...
    int a = strlen(raw_input);
    char* mod_input = raw_input; 
    
    int j = 0;
    for (int i = 0; i < a; i++){
        if(ispunctuation(raw_input[i])){
        }
        else {
            mod_input[j] = raw_input[i];
            j++;
        }
    }
    for (int k=j; k<a; k++){
        mod_input[k] = {0};
    }
    return raw_input;
}

int main() {
    // user input
    char raw_input[80] = {0};
    cout << "Please input something with punctuation in it: ";
    cin.getline(raw_input,80);
    cout << "length of raw input: " << strlen(raw_input) << endl;

    char mod_array[strlen(raw_input)] = {0};
    cout << "Modify and Copy: " << endl;
    cout << "Original: " << raw_input << endl;
    cout << "Modified: " << modifyAndCopy(raw_input, mod_array)<< endl << endl;

    cout << "Modify in Place: " << endl;
    cout << "Original: " << raw_input << endl;
    cout << "Modified: " << modifyInPlace(raw_input) << endl;
    
    return 0;
}
