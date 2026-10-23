# R080SUB

## Descrição

Registro de Subordinados

---

## Resumo

- Campos: 17
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodTur | Number(001,0) | Não | Turno dos Subordinados |
| DatAlt | Date | Não | Data Alteração da Chefia |
| EmpChe | Number(004,0) | Sim | Código da empresa do chefe |
| TipChe | Number(001,0) | Sim | Tipo Colaborador Chefe |
| CadChe | Number(009,0) | Sim | Código do Cadastro do Chefe |
| EmpSCh | Number(004,0) | Sim | Código da empresa do subchefe |
| TipSCh | Number(001,0) | Sim | Tipo Colaborador Subchefe |
| CadSCh | Number(009,0) | Sim | Código do Cadastro do Subchefe |
| TpoChe | String(001) | Sim | Tipo de Chefia |
| EmpSub | Number(004,0) | Sim | Código da empresa do substituto |
| TipSub | Number(001,0) | Sim | Tipo Colaborador Substituto |
| CadSub | Number(009,0) | Sim | Código do Cadastro do Substituto |
| DatFim | Date | Sim | Data Final do Histórico de Chefia |
| LocNiv | Number(009,0) | Sim | Local  p/identificação da chefia no nível anterior do organograma |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- CodTur
- DatAlt

---

## Índices

### R080SUBIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CadChe
- TabOrg
- NumLoc
- CodTur
- DatAlt

---

## Relacionamentos

### IR_R080SUB_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R080SUB_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

