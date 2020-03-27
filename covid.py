def comparison(content1, content2):
    var = 0
    iter = min(len(content1), len(content2))
    for i in range(0, iter):
        if content1[i] == content2[i]:
            var = var + 1
    return (100*var)/iter

archivo = open("AY274119.txt", "r")
archivo1 = open("AY278488.2.txt", "r")
archivo2 = open("MN988669.txt", "r")
archivo3 = open("MN988668.txt", "r")
archivo4 = open("MN908947.txt", "r")
content = archivo.read();
content1 = archivo1.read();
content2 = archivo2.read();
content3 = archivo3.read();
content4 = archivo4.read();
list = [content, content1, content2, content3, content4]
print("Creando coincidencias de genoma...")
print(" ", "    1   ", " 2   ", " 3  ", "  4 ", "   5 ")
num = 1
for file in list:
    print(num, end=" ")
    for files in list:
        print(round(comparison(file, files), 2), end = " ")
    num += 1
    print("")
archivo.close()
archivo1.close()
archivo2.close()
archivo3.close()
archivo4.close()

