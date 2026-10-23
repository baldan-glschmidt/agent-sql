# R095MTC

## Descrição

Materiais por Colaborador

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodMat | String(008) | Não | Código do Material |
| ObsMat | String(080) | Sim | Observação |
| SeqReg | Number(015,0) | Sim | Sequencia do Registro |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodMat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R095MTC_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R095MTC_003

**Tabela:** R095MAT

| Origem | Destino |
|--------|---------|
| CodMat | CodMat |

