file_output_name = 'proff_out.txt'
# file_input_name = 'proff_in.txt'
catalog = []
group = ['Medicine', 'Government workers',
         'Police', 'navi and military'
         'Non Police government service', 'In office',
         'Business', 'Science', 'Work with plants',
         'Work with animals',
         'Service', 'Films, tv and radio',
         'Digital', 'Paints and culture', 'Dancing',
         'Education in school', 'Education in university',
         'low-quality not educated work'
         ]
file_output = open(file_output_name, 'a')

for i in range(0, len(group)):
    catalog.append([])

#file_input = open(file_input_name, 'r')
curr_gr = 0
while 7==7 :

    inputer = input()
    #input = file_input.readline()
    if inputer[0] == '!':
        curr_gr = int(input('введите номер группы '))
        print(group[curr_gr])
        if curr_gr == -11:
            break
    if inputer != '!':
        catalog[curr_gr].append(inputer)

for j in range(0, len(group)):

    file_output.write('  ' + "'" + group[j] + "'" + ' : [' + '\n')
    for i in range(len(catalog[j])):

        file_output.write('    ' + "'" + catalog[j][i] +  "'," + '\n')
    file_output.write('  ],'+ '\n')
