# 🍸 Cocktail API

REST API do zarzadzania koktajlami i skladnikami.

---

## 🔧 Instalacja

1. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

2. Uruchom migracje:

```bash
python manage.py migrate
```

3. Uruchom serwer:

```bash
python manage.py runserver
```

---

## 📃 Endpointy

### 🔍 GET /api/cocktails/

**Opis:** Lista wszystkich koktajli

**Wspiera:**

- Filtrowanie: `?alcoholic=true&category=cocktail&glass=highball`
- Wyszukiwanie: `?search=whiskey`
- Sortowanie: `?ordering=name` lub `?ordering=-alcohol_strength`

**Dostępne pola sortowania:**

- `name`, `category`, `glass`, `created_at`, `updated_at`, `alcohol_strength`

**Dostępne pola filtrowania:**

- `alcoholic`, `category`, `glass`

---

### 📋 GET /api/cocktails/{id}/

**Opis:** Szczegóły pojedynczego koktajlu z pełnymi danymi i jego składnikami.

---

### ➕ POST /api/cocktails/

**Opis:** Tworzy nowy koktajl

**Przykładowy payload:**

```json
{
  "name": "Margarita",
  "category": "sweet",
  "instruction": "Shake with ice",
  "glass": "martini",
  "alcoholic": true,
  "cocktail_ingredients": [
    {
      "ingredient": 1,
      "amount": "50",
      "unit": "ml"
    },
    {
      "ingredient": 2,
      "amount": "25",
      "unit": "ml"
    }
  ]
}
```

---

### ✏️ PUT /api/cocktails/{id}/

**Opis:** Nadpisuje istniejący koktajl i jego składniki

### ✏️ PATCH /api/cocktails/{id}/

**Opis:** Czesciowa aktualizacja koktajlu

### ❌ DELETE /api/cocktails/{id}/

**Opis:** Usuwa koktajl

---

### 📂 GET /api/ingredients/

**Opis:** Lista wszystkich składników

**Wspiera:**

- Filtrowanie: `?alcoholic=true&type=vodka`
- Wyszukiwanie: `?search=cola`
- Sortowanie: `?ordering=percentage`

**Dostępne pola sortowania:**

- `name`, `type`,`percentage`, `ceated_at`, `updated_at`

**Dostępne pola filtrowania:**

- `alcoholic`, `type`

---

### 📍 POST /api/ingredients/

**Opis:** Dodaje nowy składnik

```json
{
      "name": "whiskey",
      "description": "Strong alcohol",
      "alcoholic": true,
      "type": "whiskey",
      "percentage": 40.0,
      "image": "<path>/picture.jpg"
}
```
---

### ✏️ PUT /api/ingredients/{id}/

**Opis:** Nadpisuje istniejący składnik

### ✏️ PATCH /api/ingredients/{id}/

**Opis:** Czesciowa aktualizacja składnika

### ❌ DELETE /api/ingredients/{id}/

**Opis:** Usuwa składnik

---

### 🌿 GET /api/cocktails/filter\_by\_ingredient/?ingredient\_name=whiskey

**Opis:** Zwraca koktajle zawierające wskazany składnik (po nazwie)

**Przykład:**

```
GET /api/cocktails/filter_by_ingredient/?ingredient_name=whiskey
```

---

## 💡 Dodatkowe informacje

- Pole `alcohol_strength` jest obliczane jako suma `amount * percentage` dla alkoholowych składników koktajlu

---

## 📄 Autoryzacja

Brak (API publiczne - do testów). Można dodać `TokenAuthentication` lub `JWT`.

---

## 🔄 Przykłady zapytań

**Wyszukiwanie koktajli z whiskey i sortowanie wg mocy:**

```
GET /api/cocktails/filter_by_ingredient/?ingredient_name=whiskey&ordering=-alcohol_strength
```

**Lista bezalkoholowych drinków w szkle typu "highball":**

```
GET /api/cocktails/?alcoholic=false&glass=highball
```

**Wyszukaj składnik typu vodka:**

```
GET /api/ingredients/?type=vodka
```

---
