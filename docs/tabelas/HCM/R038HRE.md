# R038HRE

## Descrição

Histórico Receita

---

## Resumo

- Campos: 12
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
| DatAlt | Date | Não | Data da Alteração da Receita |
| CodRec | Number(004,0) | Sim | Código da Receita |
| TipIrf | String(001) | Sim | Cálculo IR |
| PerAli | Number(005,2) | Sim | Alíquota |
| TipRen | Number(003,0) | Sim | Tipo de Rendimento |
| ForTri | Number(002,0) | Sim | Forma de Tributação |
| DatMol | Date | Sim | Data atribuída pelo laudo da moléstia grave |
| RelPag | Number(003,0) | Sim | Relação Fonte Pagadora |
| DedSim | Number(001,0) | Sim | Cálculo Simplificado |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038HRE_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R038HRE_004

**Tabela:** R050REC

| Origem | Destino |
|--------|---------|
| CodRec | CodRec |

