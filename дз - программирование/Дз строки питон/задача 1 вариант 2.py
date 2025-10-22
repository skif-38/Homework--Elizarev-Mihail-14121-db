def main():
    # Чтение входных данных
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline())
        lines = [f.readline().strip() for _ in range(n)]
    
    key_phrase = "the quick brown fox jumps over the lazy dog"
    
    # Поиск строки-кандидата (той же длины и с пробелами в тех же позициях)
    candidate = None
    for line in lines:
        if len(line) != len(key_phrase):
            continue
        
        # Проверяем позиции пробелов
        spaces_match = True
        for i in range(len(key_phrase)):
            if (key_phrase[i] == ' ') != (line[i] == ' '):
                spaces_match = False
                break
        
        if spaces_match:
            candidate = line
            break
    
    if candidate is None:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("No solution")
        return
    
    # Строим таблицу замены
    mapping = {}
    for i in range(len(key_phrase)):
        if key_phrase[i] != ' ':
            enc_char = candidate[i]
            orig_char = key_phrase[i]
            
            # Проверка на противоречие
            if enc_char in mapping:
                if mapping[enc_char] != orig_char:
                    with open('OUTPUT.TXT', 'w') as f:
                        f.write("No solution")
                    return
            else:
                mapping[enc_char] = orig_char
    
    # Проверяем, что все 26 букв присутствуют
    if len(mapping) != 26:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("No solution")
        return
    
    # Расшифровываем все строки
    result = []
    for line in lines:
        decrypted = []
        for char in line:
            if char == ' ':
                decrypted.append(' ')
            else:
                decrypted.append(mapping[char])
        result.append(''.join(decrypted))
    
    # Записываем результат
    with open('OUTPUT.TXT', 'w') as f:
        f.write('\n'.join(result))

if __name__ == "__main__":
    main()