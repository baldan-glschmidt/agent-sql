# R030FGF

## Descrição

Filiais - Percentuais Adicionais FGTS

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatAlt | Date | Não | Data de Alteração da Opção pelo Simples |
| OptSim | Number(001,0) | Sim | Opção Simples |
| PerFgt | Number(005,2) | Sim | Percentual Adicional FGTS |
| PerMul | Number(005,2) | Sim | Percentual Adicional FGTS Multa |
| TemLim | String(001) | Sim | Liminar (N, S, M, F) |
| ProcCs | Number(009,0) | Sim | Número do processo Contribuição Social Rescisória |

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

### IR_R030FGF_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

