def decode_unicode_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Decode the unicode escape sequences
    decoded_content = content.encode().decode('unicode_escape')

    # Write the decoded content to a new file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decoded_content)

    print(f"Decoded content has been written to {output_file}")

# Example usage
input_file = '2.txt'  # replace with your input file name
output_file = '2_decoded.txt'  # replace with your desired output file name
decode_unicode_file(input_file, output_file)