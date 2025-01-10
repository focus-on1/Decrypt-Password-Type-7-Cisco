# Décryptage des mots de passe Cisco

## Description
Ce script Python est conçu pour démontrer le processus de décryptage des mots de passe Cisco. Il fournit une explication détaillée de chaque étape, y compris l'extraction de l'offset, la conversion hexadécimale, et l'utilisation de la clé Cisco pour déchiffrer le mot de passe chiffré.

## Fonctionnalités
- Extraction et affichage de l'offset.
- Conversion de la partie hexadécimale en décimale.
- Décryptage détaillé à l'aide de la clé Cisco et de l'opération XOR.
- Affichage du processus de déchiffrement pour chaque caractère.

## Prérequis
- Python 3.x

## Installation
Aucune installation particulière n'est nécessaire. Assurez-vous simplement que Python 3 est installé sur votre machine.

## Utilisation
1. Clonez ce dépôt ou copiez le script sur votre machine locale.
2. Exécutez le script avec Python :

    ```bash
    python main.py
    ```

3. Entrez le mot de passe chiffré lorsqu'il vous est demandé.
4. Le script affichera les étapes détaillées du déchiffrement et le mot de passe en clair à la fin.

## Exemple de sortie
```plaintext
Clé Cisco: dsfd;kfoA,.iyewrkldJKDHSUB@
Longueur de la clé: 26 caractères

Mot de passe chiffré: 060A4B5C

1. OFFSET:
Premier deux caractères (offset): 06
Offset en décimal: 6

2. PARTIE CHIFFRÉE:
Portion hex: 0A4B5C

3. CONVERSION HEX -> DECIMAL:
Paire hex 0A -> décimal 10
Paire hex 4B -> décimal 75
Paire hex 5C -> décimal 92

4. PROCESSUS DE DÉCHIFFREMENT DÉTAILLÉ:
...

5. RÉSULTAT FINAL:
Mot de passe déchiffré: mypassword
```

## Structure du code
- **Clé Cisco** : Une chaîne fixe utilisée pour le déchiffrement.
- **Offset** : Les deux premiers caractères du mot de passe chiffré.
- **Conversion Hex -> Décimal** : Processus de transformation de la partie hexadécimale en valeurs décimales.
- **Décryptage détaillé** : Utilisation de l'opération XOR pour retrouver chaque caractère en clair.

## Avertissement
Ce script est uniquement à des fins éducatives. Toute utilisation non autorisée pour accéder à des informations protégées est illégale et contraire à l'éthique.

## Auteur
Ce projet a été développé par [Focus](https://github.com/focus-on1/).
