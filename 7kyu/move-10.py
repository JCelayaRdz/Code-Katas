def move_ten(word):
    res = ''
    for character in word:
        new_character_value = ord(character) + 10
        if new_character_value > 122:
            res += chr(new_character_value-26)
        else:
           res += chr(new_character_value)
    return res

assert move_ten("testcase") == "docdmkco" , "Should be docdmkco"
assert move_ten("codewars") == "mynogkbc" , "Should be mynogkbc"
assert move_ten("exampletesthere") == "ohkwzvodocdrobo" , "Should be ohkwzvodocdrobo"
assert move_ten("returnofthespacecamel") == "bodebxypdroczkmomkwov" , "Should be bodebxypdroczkmomkwov"
assert move_ten("bringonthebootcamp") == "lbsxqyxdrolyydmkwz" , "Should be lbsxqyxdrolyydmkwz"
assert move_ten("weneedanofficedog") == "goxoonkxyppsmonyq" , "Should be goxoonkxyppsmonyq"