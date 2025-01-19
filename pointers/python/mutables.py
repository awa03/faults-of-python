def print_state(name1, val1, name2, val2):
    """Print the current state of two variables and their memory locations."""
    print(f"\n{name1} = {repr(val1)}")
    print(f"{name2} = {repr(val2)}")
    print(f"Address of {name1}: {id(val1)}")
    print(f"Address of {name2}: {id(val2)}")
    print(f"Same object? {val1 is val2}")

def demonstrate_default_args_pitfall():
    """Demonstrate the dangerous default mutable argument pitfall."""
    print("\n=== Mutable Default Argument Pitfall ===")
    
    def add_to_list(item, target_list=[]):  # DANGEROUS: mutable default argument
        target_list.append(item)
        return target_list
    
    print("First call: add_to_list(1)")
    result1 = add_to_list(1)
    print(f"Result: {result1}")
    
    print("\nSecond call: add_to_list(2)")
    result2 = add_to_list(2)
    print(f"Result: {result2}")  # Unexpectedly contains [1, 2]!
    
    print("\nProof that both calls used the same list:")
    print(f"First result points to:  {id(result1)}")
    print(f"Second result points to: {id(result2)}")
    
    print("\nCorrect version:")
    def add_to_list_fixed(item, target_list=None):
        if target_list is None:
            target_list = []
        target_list.append(item)
        return target_list
    
    print("Using fixed version:")
    result3 = add_to_list_fixed(1)
    result4 = add_to_list_fixed(2)
    print(f"First call result:  {result3}")
    print(f"Second call result: {result4}")

def demonstrate_shallow_copy_pitfall():
    """Demonstrate issues with shallow copying of nested structures."""
    print("\n=== Shallow Copy Pitfall ===")
    
    # Create a nested structure
    original = {
        'name': 'User1',
        'scores': [85, 90, 95],
        'metadata': {'created': '2024-01-19'}
    }
    
    # Make a shallow copy
    import copy
    shallow_copy = copy.copy(original)
    
    print("Original:", original)
    print("Shallow copy:", shallow_copy)
    print("\nModifying nested list in shallow copy...")
    shallow_copy['scores'].append(100)
    
    print("\nUnexpected result - both dictionaries affected:")
    print("Original:", original)
    print("Shallow copy:", shallow_copy)
    
    # Show the correct way using deep copy
    deep_copy = copy.deepcopy(original)
    print("\nUsing deep copy instead...")
    deep_copy['scores'].append(105)
    print("Original:", original)
    print("Deep copy:", deep_copy)

def demonstrate_list_reference_pitfall():
    """Demonstrate issues with list references in loops."""
    print("\n=== List Reference in Loops Pitfall ===")
    
    # Create a list of lists - WRONG WAY
    wrong_matrix = [[0] * 3] * 3
    print("Initial matrix:", wrong_matrix)
    
    print("\nTrying to modify one element...")
    wrong_matrix[0][1] = 1
    print("Unexpected result - all rows modified:", wrong_matrix)
    
    # Correct way
    correct_matrix = [[0 for _ in range(3)] for _ in range(3)]
    print("\nCorrect matrix creation:")
    print("Initial state:", correct_matrix)
    correct_matrix[0][1] = 1
    print("After modification:", correct_matrix)

def demonstrate_dict_reference_pitfall():
    """Demonstrate issues with dictionary references in class attributes."""
    print("\n=== Dictionary Reference in Class Pitfall ===")
    
    class UserWrong:
        # DANGEROUS: Class-level mutable attribute
        settings = {'theme': 'light', 'notifications': True}
        
        def __init__(self, name):
            self.name = name
    
    # Create two users
    user1 = UserWrong('Alice')
    user2 = UserWrong('Bob')
    
    print("Initial settings:")
    print(f"User1 settings: {user1.settings}")
    print(f"User2 settings: {user2.settings}")
    
    print("\nModifying User1's settings...")
    user1.settings['theme'] = 'dark'
    
    print("\nUnexpected result - both users affected:")
    print(f"User1 settings: {user1.settings}")
    print(f"User2 settings: {user2.settings}")
    
    # Correct implementation
    class UserCorrect:
        def __init__(self, name):
            self.name = name
            # Instance-level dictionary
            self.settings = {'theme': 'light', 'notifications': True}
    
    print("\nUsing correct implementation:")
    user3 = UserCorrect('Charlie')
    user4 = UserCorrect('David')
    user3.settings['theme'] = 'dark'
    
    print(f"User3 settings: {user3.settings}")
    print(f"User4 settings: {user4.settings}")

def main():
    demonstrate_default_args_pitfall()
    demonstrate_shallow_copy_pitfall()
    demonstrate_list_reference_pitfall()
    demonstrate_dict_reference_pitfall()

if __name__ == "__main__":
    main()
