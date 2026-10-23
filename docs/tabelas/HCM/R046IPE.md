# R046IPE

## Descrição

Percentuais IPE

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
| DatIni | Date | Não | Data Início |
| PerIPE | Number(005,2) | Sim | Percentual IPE |
| AplCol | Number(001,0) | Sim | Informe a quem o percentual será aplicado |

---

## Chave Primária

- NumEmp
- CodFil
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R046IPE_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

