#include <iostream>

int LinearSearch(int arr[], int size, int element) {
    for (int i = 0; i < size; i++){
        if (arr[i] == element){
            return i;
        }
    }
    return -1;
}

int BinarySearch(int arr[], int size, int element) {

    int low, mid, high;
    low = 0;
    high = size - 1;

    mid = (low + high) / 2;

    while (low <= high){
        if (arr[mid] == element) {
            return mid;
        }
        else if (arr[mid] < element){
            low = mid + 1;
        }
        else{
            high = mid - 1;
        }
    }
    return -1;
}

int main() {

    // linear search
    std::cout << "Linear Search\n";
    int num[] = {1, 2, 7, 9, 12, 4, 10};
    int size = sizeof(num)/sizeof(int);
    int element = 7;
    int result = LinearSearch(num, size, element);
    std::cout << result << '\n';

    //binary search
    std::cout << "\nBinary Search\n";
    int num2[] = {1, 2, 6, 8, 10, 17,  24, 34, 45, 66, 78, 90, 100};
    int size2 = sizeof(num2)/sizeof(int);
    int element2 = 24;
    int res = BinarySearch(num2, size2, element2);
    std::cout << res;
    return 0;

}