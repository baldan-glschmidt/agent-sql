# E070CPD

## Descrição

Cadastros - Filiais - Paralisação da dependência comunicada ao BACEN

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodDep | String(015) | Não | Código da dependência |
| DatIni | Date | Não | Data Inicial |
| DatFim | Date | Sim | Data Final |

---

## Chave Primária

- CodEmp
- CodFil
- CodDep
- DatIni

---

## Índices

### E070CPD_FKIndex1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodDep

---

## Relacionamentos

### IR_E070CPD_002

**Tabela:** E070CDE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodDep | CodDep |

