input_string = "The quick brown fox jumps over the lazy dog"
input_string = input_string.rsplit(" ")
output_string = [input_string[i][1] for i in range(len(input_string))]
print("".join(str(char) for char in output_string))
