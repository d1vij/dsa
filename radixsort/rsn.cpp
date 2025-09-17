#include <iostream>
#include <cmath>
#include <vector>

using namespace std;


int get_nth_digit(int num, int n){
    int a = num / pow(10,n);
    return a % 10;
}

void radix_sort(vector<int>& unsorted_array, int length_of_single_number){

    
    for(int iter=0; iter<length_of_single_number; iter++){

        // [vect1, vect2 ,vect3 ...]
        vector<int> radix_array[10];

        
        // filling radix array
        for(int idx=0; idx < unsorted_array.size(); idx++){
            int num = unsorted_array[idx];
            int nth_digit = get_nth_digit(num, iter);

            radix_array[nth_digit].push_back(num);
        }

        // clearing the unsorted_array
        unsorted_array.clear();

        // filling array with data from radix_array buckets
        for(int idx=0; idx< 10; idx++){
            vector<int> bucket = radix_array[idx];

            for(int i=0; i<bucket.size(); i++){
                int num = bucket[i];
                unsorted_array.push_back(num);
            }
        }
    }
}
void print_vector(vector<int> vect){
    for(int num : vect){
        cout << num << ' ';
    }
    cout << '\n';
}


int main(){
    vector<int> a1 = {491, 123, 412, 991, 230};
    print_vector(a1);
    radix_sort(a1, 3);
    print_vector(a1);
    
    return 0;
}