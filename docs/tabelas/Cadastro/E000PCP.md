# E000PCP

## Descrição

Tabelas - Integrações - Preço custo de produto por data

---

## Resumo

- Campos: 9
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
| DatIni | Date | Não | Data Inicial do período |
| DatFim | Date | Não | Data final do período |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |
| CodFam | String(006) | Sim | Código da família de produto |
| PreCus | Number(015,6) | Sim | Preço de custo mensal |

---

## Chave Primária

- SeqInt

---

## Índices

### E000PCPIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- DatIni
- DatFim
- CodPro
- CodDer
- CodFam

---

## Relacionamentos

Nenhum relacionamento cadastrado.
