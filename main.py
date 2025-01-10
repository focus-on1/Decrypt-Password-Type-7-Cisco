
#  _______     ______  ______ _____    ______ ____   _____ _    _  _____
# / ____\ \   / /  _ \|  ____|  __ \  |  ____/ __ \ / ____| |  | |/ ____|
#| |     \ \_/ /| |_) | |__  | |__) | | |__ | |  | | |    | |  | | (___
#| |      \   / |  _ <|  __| |  _  /  |  __|| |  | | |    | |  | |\___ \
#| |____   | |  | |_) | |____| | \ \  | |   | |__| | |____| |__| |____) |
# \_____|  |_|  |____/|______|_|  \_\ |_|    \____/ \_____|\____/|_____/
# /****************************************
#  *       DECRYPT PASSWORD CISCO  *
#  ****************************************/

def demonstration_detaille():
    # La clé Cisco 
    cisco_key = "dsfd;kfoA,.iyewrkldJKDHSUB@"

    print(f"Clé Cisco: {cisco_key}")
    print(f"Longueur de la clé: {len(cisco_key)} caractères\n")
    print (f"La longue de la cle et {len(cisco_key)} caractere \n")
    
    # Mot de passe chiffré exemple
    print(f"Mot de passe chiffré: {encrypted}") 
    
    # 1. Extraction de l'offset
    offset = int(encrypted[:2])  
   
    print(f"\n1. OFFSET:")
    print(f"Premier deux caractères (offset): {encrypted[:2]}")
    print(f"Offset en décimal: {offset}")
    
    # 2. Extraction de la partie hex
    encrypted_hex = encrypted[2:]
    print(f"\n2. PARTIE CHIFFRÉE:")
    print(f"Portion hex: {encrypted_hex}")
    
    # 3. Conversion hex en bytes
    bytes_list = []
    print(f"\n3. CONVERSION HEX -> DECIMAL:")
    # on parcour 2 par 2 pour extraire les HEX 
    for i in range(0, len(encrypted_hex), 2): 
        hex_pair = encrypted_hex[i:i+2] 
        decimal = int(hex_pair, 16) # utilise int pour mettre en decimale 
        bytes_list.append(decimal) # ajoute le decimale dans la liste 
        print(f"Paire hex {hex_pair} -> décimal {decimal}")
    
    # 4. Déchiffrement détaillé
    print(f"\n4. PROCESSUS DE DÉCHIFFREMENT DÉTAILLÉ:")
    decrypted = ""
    
    """
    1) La clé a une longueur fixe. Si on a une liste de données 
    à traiter qui est plus longue que la clé, on veut réutiliser la clé en boucle.
    donc la fonction position permet de liste la position en bouclent sur la clee 
    pour pas fausse les valeur on boucle avec la clee

    2

    """
    for i, byte in enumerate(bytes_list):
        # Position dans la clé
        key_position = (offset + i) % len(cisco_key)  
        key_char = cisco_key[key_position]
        
        # Processus XOR détaillé
        key_ord = ord(key_char) # caracter en decimale
         
        # Affichage des valeurs binaires pour comprendre le XOR
        byte_bin = format(byte, '08b') # initialise le type de binaire 
        key_bin = format(key_ord, '08b')
        xor_result = byte ^ key_ord # un byt a byt avec XOR ^
        xor_bin = format(xor_result, '08b') 
        
        print(f"\nDéchiffrement caractère position {i}:")
        print(f"Byte chiffré (décimal): {byte}")
        print(f"Position dans la clé: {key_position}")
        print(f"Caractère de la clé: '{key_char}' (ASCII: {key_ord})")
        print(f"En binaire:")
        print(f"  Chiffré:  {byte_bin}")
        print(f"  Clé:      {key_bin}")
        print(f"  XOR:      {xor_bin}")
        print(f"Résultat XOR (décimal): {xor_result}")
        print(f"Caractère déchiffré: '{chr(xor_result)}'")
        
        decrypted += chr(xor_result) # ajoute le caracter decrypte dans la chaine 
    
    print(f"\n5. RÉSULTAT FINAL:")
    print(f"Mot de passe déchiffré: {decrypted}")
    
    return decrypted

encrypted = (input(f'Veuille entre la clee a decrypte : '))
run = demonstration_detaille()
