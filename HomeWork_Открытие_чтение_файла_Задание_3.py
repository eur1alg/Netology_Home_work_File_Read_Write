##---------------------------------- Задание 3 --------------------------------------------
file_lines_qnt_dic = {}
for file_name in range(1,4):    ## так как названия файлов цифры, то делаем цикл на их выборку
    file_name_txt = str(file_name)+'.txt'
    with open(file_name_txt, encoding='UTF8') as file:
        file_lines_qnt = 0
        for line in file:   ## цикл на подсчет кол-ва строк в файле
            file_lines_qnt += 1
        file_lines_qnt_dic[file_name_txt] = file_lines_qnt

file_lines_qnt_dic = dict(sorted(file_lines_qnt_dic.items(),key=lambda item: item[1]))      ## сортируем словарь по кол-ву строк

with open('Task_3_write.txt', 'w') as file: ## пишем в файл
    for i in file_lines_qnt_dic:
        file.write(i+'\n')  ## пишем название файла
        file.write(str(file_lines_qnt_dic.get(i))+'\n') ## пишем кол-во строк

        with open(i, encoding='UTF8') as file_input: ## пишем сам файл
            for line in file_input:
                file.write(line)
