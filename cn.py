def replace_d_with_c(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read()

    # 将字符串中的"D"替换为"C"
    modified_data = data.replace("\\", "/")

    with open(output_file, 'w') as file:
        file.write(modified_data)

# 输入和输出文件的路径
input_file_path = "test.txt"
output_file_path = "test.txt"

# 调用函数进行替换并写回文件
replace_d_with_c(input_file_path, output_file_path)

print("替换完成并已写入到output.txt文件中。")
