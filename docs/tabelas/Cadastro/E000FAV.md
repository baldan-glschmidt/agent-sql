# E000FAV

## Descrição

Tabelas - Integração - Controle de Favorecidos

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFav | Number(014,0) | Não | Número do CNPJ ou CPF do favorecido |
| DocIde | String(014) | Sim | Número do CNPJ ou CPF do favorecido |
| IdeFav | String(050) | Sim | Identificador único alfanumérico |

---

## Chave Primária

- SeqInt

---

## Índices

### E000FAVIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodFav
- DocIde

---

## Relacionamentos

Nenhum relacionamento cadastrado.
