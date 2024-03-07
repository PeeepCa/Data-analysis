import glob

def parseLOG():
    stat_pass = 0
    stat_fail = 0
    EOT0 = 0
    EOT1 = 0
    EOT2 = 0
    EOT3 = 0
    EOT4 = 0
    EOT5 = 0
    EOT6 = 0
    fill = 0
    Las_mark = 0
    pos1 = 0
    pos2 = 0
    pos3 = 0
    pos4 = 0
    
    list_of_files = glob.glob('*.log')
    for i in list_of_files:
        if 'feasa' in i:
            with open(i, 'r') as fileopened:
                data = fileopened.read(-1)
                data = data.splitlines()
        if 'nok' in i:
            with open(i, 'r') as fileopened:
                data2 = fileopened.read(-1)
                data2 = data2.splitlines()
    for x in data:
        temp_data = x.split(' ')
        sn = temp_data[3][:-1]
        pos = temp_data[4]
        feasa_x_y = temp_data[6] + temp_data[7].replace(',','')
        feasa_int = temp_data[8]
        ########################
        ## Druhy soubor
        for z in data2:
            if sn in z and 'NOK' in z.split(' ')[6]:
                results = z.split(':')[3].split('NOK')[1]
                stat_fail += 1

                if pos == '1':
                    pos1 += 1
                elif pos == '2':
                    pos2 += 1
                elif pos == '3':
                    pos3 += 1
                elif pos == '4':
                    pos4 += 1
                
                if 'EOT=0' in results:
                    EOT0 += 1
                elif 'EOT=1' in results:
                    EOT1 += 1
                elif 'EOT=2' in results:
                    EOT2 += 1
                elif 'EOT=3' in results:
                    EOT3 += 1
                elif 'EOT=4' in results:
                    EOT4 += 1
                elif 'EOT=5' in results:
                    EOT5 += 1
                elif 'EOT=6' in results:
                    EOT6 += 1
                if 'Fill' in results:
                    fill += 1
                if 'Las_mark' in results:
                    Las_mark += 1
            elif sn in z and 'OK' in z.split(' ')[6]:
                stat_pass += 1

    print('EOT=0: ' + str(EOT0) + ' Rate: ' + str(EOT0 / (stat_pass + stat_fail) * 100)[:5] + '%')
    print('EOT=1: ' + str(EOT1) + ' Rate: ' + str(EOT1 / (stat_pass + stat_fail) * 100)[:5] + '%')
    print('EOT=2: ' + str(EOT2) + ' Rate: ' + str(EOT2 / (stat_pass + stat_fail) * 100)[:5] + '%')
    print('EOT=3: ' + str(EOT3) + ' Rate: ' + str(EOT3 / (stat_pass + stat_fail) * 100)[:5] + '%')
    print('EOT=4: ' + str(EOT4) + ' Rate: ' + str(EOT4 / (stat_pass + stat_fail) * 100)[:5] + '%')
    print('EOT=5: ' + str(EOT5) + ' Rate: ' + str(EOT5 / (stat_pass + stat_fail) * 100)[:5] + '%')
    print('EOT=6: ' + str(EOT6) + ' Rate: ' + str(EOT6 / (stat_pass + stat_fail) * 100)[:5] + '%')
    print('Fill: ' + str(fill) + ' Rate: ' + str(fill / (stat_pass + stat_fail) * 100)[:5] + '%')
    print('Las_mark: ' + str(Las_mark) + ' Rate: ' + str(Las_mark / (stat_pass + stat_fail) * 100)[:5] + '%')
    print('PASS: ' + str(stat_pass))
    print('FAIL: ' + str(stat_fail))
    print('Defect rate: ' + str((EOT0 + EOT1 + EOT2 + EOT3 + EOT4 + EOT5 + EOT6 + fill + Las_mark)  / (stat_pass + stat_fail) * 100)[:5] + '%')
    print('Position 1: ' + str(pos1))
    print('Position 2: ' + str(pos2))
    print('Position 3: ' + str(pos3))
    print('Position 4: ' + str(pos4))

parseLOG()
