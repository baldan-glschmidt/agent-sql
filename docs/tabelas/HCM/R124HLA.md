# R124HLA

## Descrição

Colaborador - Laudos Psicólogo

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Candidato |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador Candidato |
| DatHla | Date | Não | Data do Laudo |
| EmpPsi | Number(004,0) | Sim | Empresa do Psicólogo |
| OriPsi | Number(001,0) | Sim | Tipo do Psicólogo |
| NumPsi | Number(009,0) | Sim | Cadastro do Psicólogo |
| ComHla | String(7000) | Sim | Laudo |
| NomArq | String(250) | Sim | Arquivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatHla

---

## Índices

### R124HLAIndice2

**Tipo:** Não unico

Campos:
- EmpPsi
- OriPsi
- NumPsi

---

## Relacionamentos

### IR_R124HLA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

