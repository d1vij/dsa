#include <iostream>
#include <cmath>
#include <vector>

int get_nth_digit(int num, int idx){
    return std::fmod(num / std::pow(10, idx), 10);
}
// 123 0th 3

void print_vector(std::vector<int> vect){
    for(int num : vect){
        std::cout << num << ' ';
    }
    std::cout << '\n';
}
void print_radix_array(std::vector<int> ra[10]){
    for(int idx=0; idx<10; idx++){
        std::cout << "[ ";
        for(int num : ra[idx]){
            std::cout << idx << ' ';
        }
        std::cout << " ]";
    }

    std::cout << '\n';
}


void radix_sort(std::vector<int> &unsorted_array, int length_of_single_number){
    std::cout << "Original array ";
    print_vector(unsorted_array);
    
    for(int i=0; i<=length_of_single_number - 1; ++i){
        std::vector<int> radix_array[10];

        // filling radix array buckets
        for(int num : unsorted_array){
            int idx = get_nth_digit(num, i);
            radix_array[idx].push_back(num);
            print_radix_array(radix_array);
        }
        
        unsorted_array.clear();

        // replacing the unsorted array with radix array buckets
        for(int idx=0; idx<10; idx++){
            for(int num : radix_array[idx]){
                unsorted_array.push_back(num);
            }
        }
        
        std::cout << "Array after " << i + 1 << "th iteration ";
        print_vector(unsorted_array);
    }
    
}

int main (){
    
    std::vector<int> a1 = {491, 123, 412, 991, 230};
    std::vector<int> a2 = {582, 913, 077, 624, 359, 188, 950, 477, 013, 738, 291, 889, 402, 666, 118, 920, 734, 570, 251, 106};
    radix_sort(a1, 3);
    std::cout << '\n';
    radix_sort(a2, 3);
    return 0;
}