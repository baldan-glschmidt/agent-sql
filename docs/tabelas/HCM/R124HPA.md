# R124HPA

## Descrição

Colaborador - Parecer Psicólogo

---

## Resumo

- Campos: 19
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador Candidato |
| DatHpa | Date | Não | Data do Parecer |
| EmpCsi | Number(004,0) | Sim | Empresa Psicólogo |
| OriCsi | Number(001,0) | Sim | Tipo de Psicólogo |
| NumCsi | Number(009,0) | Sim | Cadastro do Psicólogo |
| CodPsi | Number(003,0) | Sim | Código do Parecer Psicólogo |
| CmtPsi | String(7000) | Sim | Comentário do Psicólogo |
| EmpCse | Number(004,0) | Sim | Empresa Selecionador |
| OriCse | Number(001,0) | Sim | Tipo de Selecionador |
| NumCse | Number(009,0) | Sim | Cadastro do Selecionador |
| CodPse | Number(003,0) | Sim | Código do Parecer Selecionador |
| CmtPse | String(2000) | Sim | Comentário do Selecionador |
| EmpCsu | Number(004,0) | Sim | Empresa Superior |
| OriCsu | Number(001,0) | Sim | Tipo de Superior |
| NumCsu | Number(009,0) | Sim | Cadastro do Superior |
| CodPsu | Number(003,0) | Sim | Código do Parecer Superior |
| CmtPsu | String(2000) | Sim | Comentário do Superior |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatHpa

---

## Índices

### R124HPAIndice2

**Tipo:** Não unico

Campos:
- EmpCsi
- OriCsi
- NumCsi

---

## Relacionamentos

### IR_R124HPA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

