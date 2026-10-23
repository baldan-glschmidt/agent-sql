# R030ECO

## Descrição

Responsáveis Técnicos Espaços Confinados

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatIni | Date | Não | Data em que assumiu a responsabilidade |
| EmpECo | Number(004,0) | Não | Código da empresa do responsável técnico pelo espaço confinado |
| TipCol | Number(001,0) | Não | Tipo do responsável técnico pelo espaço confinado |
| NumCad | Number(009,0) | Não | Cadastro do responsável técnico pelo espaço confinado |
| DatTer | Date | Sim | Data em que encerrou a responsabilidade |

---

## Chave Primária

- NumEmp
- CodFil
- DatIni
- EmpECo
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030ECO_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

