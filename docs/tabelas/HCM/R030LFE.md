# R030LFE

## Descrição

Limites ENTE Federativo

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatAlt | Date | Não | Data Alteração |
| TipPod | Number(001,0) | Não | Tipo de Poder |
| ValSup | Number(014,2) | Sim | Valor Subteto |
| MaiDep | Number(002,0) | Sim | Maioridade Dependente |

---

## Chave Primária

- NumEmp
- CodFil
- DatAlt
- TipPod

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030LFE_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

