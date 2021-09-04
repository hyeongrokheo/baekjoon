def solution(new_id):
    new_id = new_id.lower()

    temp = ''
    for c in new_id:
        if not c.isdigit() and not c.isalpha() and not c in ['-', '_', '.']:
            None
        else:
            temp += c
    new_id = temp

    temp = ''
    for c in new_id:
        if len(temp) != 0 and temp[-1] == '.' and c == '.':
            None
        else:
            temp += c

    new_id = temp

    if len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id[:-1]

    if len(new_id) == 0:
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id


print(solution('123_.def'))