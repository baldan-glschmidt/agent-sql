# R030FGT

## Descrição

Empresas - Percentuais Adicionais FGTS

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| DatAlt | Date | Não | Data Alteração da Opção pelo Simples |
| OptSim | Number(001,0) | Sim | Opção Simples |
| PerFgt | Number(005,2) | Sim | Percentual Adicional FGTS |
| PerMul | Number(005,2) | Sim | Percentual Adicional FGTS Multa |
| TemLim | String(001) | Sim | Liminar |
| PorEmp | Number(001,0) | Sim | Porte da Empresa (0, 1, 2) |

---

## Chave Primária

- NumEmp
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030FGT_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

