
def print_state(name1, val1, name2, val2):
    """Print the current state of two variables and their memory locations."""
    print(f"\n{name1} = {repr(val1)}")
    print(f"{name2} = {repr(val2)}")
    print(f"Address of {name1}: {id(val1)}")
    print(f"Address of {name2}: {id(val2)}")
    print(f"Same object? {val1 is val2}")

def test_list_reference():
    """Demonstrate how multiple names can reference the same list."""
    print("\n=== List Reference Example ===")
    
    # Create a list and have two names point to it
    original = [1, 2, 3]
    reference = original
    
    print_state("original", original, "reference", reference)
    
    # Modify through one reference
    print("\nModifying through 'reference'...")
    reference.append(4)
    print_state("original", original, "reference", reference)
    
    # Create a new list assignment
    print("\nAssigning new list to 'reference'...")
    reference = [5, 6, 7]
    print_state("original", original, "reference", reference)

def test_nested_reference():
    """Demonstrate reference behavior with nested structures."""
    print("\n=== Nested Reference Example ===")
    
    # Create a nested structure
    outer = {'data': [1, 2, 3]}
    pointer1 = outer
    pointer2 = outer
    
    print("Initial state:")
    print(f"outer = {outer}")
    print(f"pointer1 = {pointer1}")
    print(f"pointer2 = {pointer2}")
    print(f"All point to same object? {outer is pointer1 is pointer2}")
    
    # Modify through different references
    print("\nModifying nested list through pointer1...")
    pointer1['data'].append(4)
    print(f"outer = {outer}")
    print(f"pointer1 = {pointer1}")
    print(f"pointer2 = {pointer2}")

def test_function_reference():
    """Demonstrate how function parameters can reference objects."""
    def modify_list(lst):
        print(f"\nInside function, lst points to: {id(lst)}")
        lst.append(99)
        print("Modified list inside function")
    
    print("\n=== Function Reference Example ===")
    numbers = [1, 2, 3]
    print(f"Before function call, numbers points to: {id(numbers)}")
    print(f"Initial numbers: {numbers}")
    
    modify_list(numbers)
    print(f"After function call, numbers: {numbers}")
    print(f"After function call, numbers still points to: {id(numbers)}")

def test_class_reference():
    """Demonstrate reference behavior in class instances."""
    class SharedData:
        shared_list = []  # Class variable - shared among all instances
        
        def __init__(self, name):
            self.name = name
            self.private_list = []  # Instance variable - unique to each instance
    
    print("\n=== Class Reference Example ===")
    
    # Create two instances
    obj1 = SharedData("Object 1")
    obj2 = SharedData("Object 2")
    
    # Modify shared data through obj1
    print("Adding to shared list through obj1...")
    obj1.shared_list.append("shared data")
    print(f"obj1.shared_list: {obj1.shared_list}")
    print(f"obj2.shared_list: {obj2.shared_list}")
    print(f"Same shared_list object? {obj1.shared_list is obj2.shared_list}")
    
    # Modify private data
    print("\nAdding to private list in obj1...")
    obj1.private_list.append("private data")
    print(f"obj1.private_list: {obj1.private_list}")
    print(f"obj2.private_list: {obj2.private_list}")
    print(f"Same private_list object? {obj1.private_list is obj2.private_list}")

def main():
    test_list_reference()
    test_nested_reference()
    test_function_reference()
    test_class_reference()

if __name__ == "__main__":
    main()
