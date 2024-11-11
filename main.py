import os

def create_test_files(directory, num_files=100000):
    os.makedirs(directory, exist_ok=True)
    
    for i in range(num_files):
        file_path = os.path.join(directory, f"test_file_{i}.txt")
        with open(file_path, 'w') as f:
            f.write("Sample content for testing.\n")
    
    print(f"Created {num_files} test files in '{directory}'")

output_directory = "./test_files"
create_test_files(output_directory)
