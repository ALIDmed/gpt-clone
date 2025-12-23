Voici une **méthode claire et complète** pour transformer les **problèmes** d’ATW en **objectifs**, puis en **KPIs**, et enfin construire un **diagramme d’Ishikawa** pertinent.

---

### ✅ Étape 1 : Reformuler les **problèmes** en **objectifs**
| **Problème** | **Objectif SMART** |
|--------------|---------------------|
| Des clients ne partent pas alors qu’ils ont payé | **Garantir que 100 % des clients ayant payé partent effectivement** |
| Des clients partent sans avoir payé | **S’assurer que 100 % des clients partent uniquement après paiement complet** |
| Litiges fréquents | **Réduire de 80 % les litiges liés aux erreurs de paiement ou de départ** |
| Coûts implicites non contrôlés | **Réduire de 50 % les coûts implicites liés aux erreurs de gestion des paiements** |

---

### ✅ Étape 2 : Transformer les **objectifs** en **KPIs**
| **Objectif** | **KPI associé** |
|--------------|------------------|
| Garantir que 100 % des clients ayant payé partent | **Taux de départs effectués parmi les clients ayant payé** |
| S’assurer que 100 % des clients partent après paiement | **Taux de départs sans paiement complet** |
| Réduire les litiges | **Nombre de litiges par mois liés aux paiements ou départs** |
| Réduire les coûts implicites | **Coût moyen par litige ou erreur de gestion** |

---

### ✅ Étape 3 : Construire le **diagramme d’Ishikawa**
But : Identifier les **causes racines** des **erreurs de paiement ou de départ**.

#### 🎯 Tête du poisson (effet) :
> **Erreurs de paiement ou de départ non synchronisés**

#### 🧠 Les 5M à explorer :
| **Catégorie** | **Exemples de causes possibles** |
|---------------|----------------------------------|
| **Main-d’œuvre** | - Agents mal formés<br>- Pas de vérification du statut paiement avant départ |
| **Méthode** | - Processus de validation manquant<br>- Pas de confirmation automatique |
| **Matériel** | - GestStock pas synchronisé avec PeopleSoft<br>- Pas de BPMS pour orchestrer |
| **Milieu** | - Agences isolées, pas de visibilité temps réel<br>- Pas de contrôle centralisé |
| **Management** | - Pas d’alerte si pas de paiement<br>- Pas de KPI suivi |

---

### ✅ Étape 4 : Diagramme Ishikawa (texte brut à dessiner)
```
Effet : Erreurs de paiement ou de départ non synchronisés
│
├── Main-d’œuvre
│   ├── Agents pas formés à vérifier le statut paiement
│   └──Pas de procédure de double vérification
│
├── Méthode
│   ├──Pas d’étape de validation avant départ
│   └──Contrat envoyé avant validation paiement
│
├── Matériel
│   ├──GestStock pas connecté à PeopleSoft
│   └──Pas de système d’alerte automatique
│
├── Milieu
│   ├──Agences autonomes sans contrôle central
│   └──Pas de vue temps réel sur les paiements
│
└── Management
    ├──Pas de KPI suivi sur les départs sans paiement
    └──Pas de responsable désigné pour la synchronisation
```

---

### ✅ Étape 5 : Utiliser l’Ishikawa pour **définir des actions**
| **Cause** | **Action** | **KPI de suivi** |
|-----------|------------|--------------------|
| GestStock pas connecté à PeopleSoft | Intégrer les deux via un BPMS | **Taux de synchronisation paiement/départ** |
| Pas de vérification avant départ | Ajouter une étape de validation dans le processus | **Taux de départs sans validation** |
| Pas de KPI suivi | Créer un tableau de bord des litiges | **Nombre de litiges par mois** |

---

### ✅ Résumé des KPIs finaux à suivre
| **KPI** | **Cible** | **Source** |
|--------|-----------|------------|
| Taux de départs sans paiement | < 1 % | PeopleSoft + GestStock |
| Taux de départs non effectués malgré paiement | < 1 % | GestStock + BPMS |
| Nombre de litiges par mois | < 5 | Service client |
| Coût moyen par litige | < 200 € | Financier |

---

Souhaitez-vous que je vous génère un **diagramme Ishikawa visuel** (format PNG ou Mermaid) ou un **template Excel** pour le remplir en groupe ?