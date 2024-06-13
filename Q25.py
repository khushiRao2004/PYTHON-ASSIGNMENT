def copy_file(source_file, destination_file):
    with open(source_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)
    print(f"Contents copied from {source_file} to {destination_file}")

source_file = "source.txt"  # Replace with your source file path
destination_file = "destination.txt"  # Replace with your destination file path
copy_file(source_file, destination_file)
