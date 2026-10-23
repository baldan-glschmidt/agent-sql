# R030DAR

## Descrição

Filiais da Empresa - Darf

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatDar | Date | Não | Início Recolhimento Darf |
| RecDar | Number(001,0) | Sim | Tipo do Darf |
| FceDar | Date | Sim | Término Recolhimento Darf |

---

## Chave Primária

- NumEmp
- CodFil
- DatDar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030DAR_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

