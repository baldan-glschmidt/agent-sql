# R030CNA

## Descrição

Filiais da Empresa - CNAE

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatAlt | Date | Não | Data de Alteração |
| AtiIrf | Number(007,0) | Sim | CNAE Fiscal |
| CnaPre | String(001) | Sim | CNAE Preponderante |
| CnaFis | Number(007,0) | Sim | CNAE Fiscal Preponderante |
| StaHis | Number(001,0) | Sim | Status do Histórico |

---

## Chave Primária

- NumEmp
- CodFil
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030CNA_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

