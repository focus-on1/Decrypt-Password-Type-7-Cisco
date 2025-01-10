# 🔐 Décryptage des mots de passe Cisco - CryptFocus
[![Licence MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)]()

## 📜 Description

CryptFocus est un outil avancé pour l'analyse et le décryptage des mots de passe Cisco Type 7. Développé avec Python et une interface web moderne, il offre une approche didactique du processus de chiffrement tout en fournissant des fonctionnalités d'analyse puissantes.

### 🌟 Caractéristiques principales

- 🔓 Décryptage de mots de passe Cisco Type 7
- 🔒 Chiffrement en Type 7
- 📊 Analyse de la force des mots de passe
- ⚡ Interface web moderne et réactive
- 🔍 Visualisation détaillée du processus
- 🚀 Calcul de temps de force brute
- 📱 Support mobile et desktop

## 🛠️ Technologies utilisées

- **Backend**: 
  - Python 3.8+
  - Flask
  - Cryptographie

- **Frontend**: 
  - HTML5/CSS3
  - JavaScript moderne
  - TailwindCSS
  - Matrix Animation

## 🚀 Installation

1. **Clonez le repository**
```bash
git clone https://github.com/focus-on1/Decrypt-Password-Type-7-Cisco.git
cd cisco-password-decrypt
```

2. **Lancez l'application**
```bash
python main.py
```

## 💻 Utilisation

### Interface Web
1. Accédez à `[http://localhost:5000](https://website-cisco-type-7.vercel.app/)`
2. Choisissez l'opération souhaitée :
   - 🔓 Décryptage
   - 🔒 Chiffrement
   - 📊 Analyse de force brute


## 📚 Documentation

### Format des mots de passe Type 7
```
AABBCCDDEEEE...
AA       : Offset (2 caractères)
BBCCDD.. : Mot de passe chiffré (hex)
```

### Exemple de sortie détaillée
```plaintext
🔑 Clé Cisco: dsfd;kfoA,.iyewrkldJKDHSUB@
📏 Longueur: 26 caractères

🔍 Analyse du mot de passe chiffré: 060A4B5C
├── Offset: 06 (décimal: 6)
├── Partie chiffrée: 0A4B5C
└── Conversion hex -> décimal: [10, 75, 92]
```

## 🌐 Application Web
Visitez [CryptFocus Web](https://website-cisco-type-7.vercel.app/) pour utiliser l'interface web.

## 🤝 Contribution
Les contributions sont bienvenues ! Voici comment vous pouvez contribuer :

1. 🍴 Forkez le projet
2. 🔨 Créez votre branche (`git checkout -b feature/AmazingFeature`)
3. 💾 Committez vos changements (`git commit -m 'Add AmazingFeature'`)
4. 📤 Pushez vers la branche (`git push origin feature/AmazingFeature`)
5. 🔍 Ouvrez une Pull Request

## ⚠️ Avertissement
Cet outil est destiné à des fins éducatives et de test uniquement. L'utilisation non autorisée pour accéder à des systèmes protégés est illégale.

## 📝 Licence
Ce projet est sous licence MIT - voir le fichier [LICENSE.md](LICENSE.md) pour plus de détails.

## 👨‍💻 Auteur
**Focus** - [GitHub](https://github.com/focus-on1/)

## 🙏 Remerciements
- 🎯 Cisco pour la documentation
- 🎨 TailwindCSS pour le design
- 🌟 Tous les contributeurs

---
⭐️ Si vous trouvez ce projet utile, n'oubliez pas de lui donner une étoile !

[⬆️ Retour en haut](#-décryptage-des-mots-de-passe-cisco---cryptfocus)
