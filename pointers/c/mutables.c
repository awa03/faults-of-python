#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure to demonstrate nested data
typedef struct {
    int scores[3];
    char name[50];
} User;

void print_array(int* arr, int size) {
    printf("[");
    for (int i = 0; i < size; i++) {
        printf("%d%s", arr[i], i < size - 1 ? ", " : "");
    }
    printf("]");
}

void print_state(const char* name1, int* ptr1, const char* name2, int* ptr2) {
    printf("\n%s points to address: %p", name1, (void*)ptr1);
    printf("\n%s points to address: %p", name2, (void*)ptr2);
    printf("\nSame address? %s", ptr1 == ptr2 ? "Yes" : "No");
    if (ptr1 && ptr2) {
        printf("\nValues: %s = %d, %s = %d", name1, *ptr1, name2, *ptr2);
    }
    printf("\n");
}

void demonstrate_basic_pointers() {
    printf("\n=== Basic Pointer Behavior ===\n");
    
    int x = 42;
    int* ptr1 = &x;
    int* ptr2 = ptr1;    // Both pointers point to x
    
    printf("\nInitial state:");
    print_state("ptr1", ptr1, "ptr2", ptr2);
    
    // Modify through ptr1
    *ptr1 = 100;
    printf("\nAfter modifying through ptr1:");
    print_state("ptr1", ptr1, "ptr2", ptr2);
    
    // Create new integer and point ptr2 to it
    int y = 200;
    ptr2 = &y;
    printf("\nAfter pointing ptr2 to new value:");
    print_state("ptr1", ptr1, "ptr2", ptr2);
}

void demonstrate_array_pointers() {
    printf("\n=== Array Pointer Behavior ===\n");
    
    // Create two arrays
    int arr1[] = {1, 2, 3};
    int arr2[] = {1, 2, 3};
    
    // Create pointers to arrays
    int* ptr1 = arr1;
    int* ptr2 = arr2;
    
    printf("\nInitial arrays:");
    printf("\narr1: ");
    print_array(arr1, 3);
    printf("\narr2: ");
    print_array(arr2, 3);
    printf("\n");
    
    // Show that arrays are at different locations
    printf("\nArray addresses:");
    print_state("arr1", ptr1, "arr2", ptr2);
    
    // Modify through pointer
    ptr1[1] = 99;
    printf("\nAfter modifying arr1 through pointer:");
    printf("\narr1: ");
    print_array(arr1, 3);
    printf("\narr2: ");
    print_array(arr2, 3);
    printf("\n");
}

void demonstrate_nested_structures() {
    printf("\n=== Nested Structure Behavior ===\n");
    
    // Create and initialize two users
    User* user1 = malloc(sizeof(User));
    User* user2 = malloc(sizeof(User));
    
    // Initialize user1
    strcpy(user1->name, "Alice");
    user1->scores[0] = 85;
    user1->scores[1] = 90;
    user1->scores[2] = 95;
    
    // Create a "shallow copy" by copying memory
    *user2 = *user1;
    strcpy(user2->name, "Bob");  // Give second user different name
    
    printf("\nAfter shallow copy:");
    printf("\nUser1: %s, scores: ", user1->name);
    print_array(user1->scores, 3);
    printf("\nUser2: %s, scores: ", user2->name);
    print_array(user2->scores, 3);
    
    // Modify user2's scores
    user2->scores[1] = 100;
    
    printf("\n\nAfter modifying user2's scores:");
    printf("\nUser1: %s, scores: ", user1->name);
    print_array(user1->scores, 3);
    printf("\nUser2: %s, scores: ", user2->name);
    print_array(user2->scores, 3);
    
    free(user1);
    free(user2);
}

void demonstrate_function_pointers() {
    printf("\n=== Function Parameter Behavior ===\n");
    
    int x = 42;
    int* ptr = &x;
    
    printf("\nBefore function call:");
    printf("\nx = %d", x);
    printf("\nptr points to: %p", (void*)ptr);
    
    // Pass pointer to function
    int y = 100;
    ptr = &y;
    
    printf("\n\nAfter changing pointer:");
    printf("\nx = %d", x);
    printf("\ny = %d", y);
    printf("\nptr now points to: %p", (void*)ptr);
    printf("\nptr value: %d\n", *ptr);
}

int main() {
    demonstrate_basic_pointers();
    demonstrate_array_pointers();
    demonstrate_nested_structures();
    demonstrate_function_pointers();
    return 0;
}
