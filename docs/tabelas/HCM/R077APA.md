# R077APA

## Descrição

Avaliação de Performance - Avaliação

---

## Resumo

- Campos: 22
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CmpAva | Date | Não | Competência da Avaliação |
| TipAva | Number(004,0) | Não | Sequência da Avaliação |
| EmpAva | Number(004,0) | Sim | Empresa do avaliador |
| TclAva | Number(001,0) | Sim | Tipo do Colaborador Avaliador |
| CadAva | Number(009,0) | Sim | Cadastro do Avaliador |
| TpAval | Number(001,0) | Sim | Foco da Avaliação |
| ComAva | String(3000) | Sim | Comentário |
| SitAva | String(001) | Sim | Situação da avaliação - concluída(S/N) |
| DatAva | Date | Sim | Data limite para efetuar a avaliação |
| DatPro | Date | Sim | Data prorrogação para efetuar a avaliação |
| PlaDes | String(3000) | Sim | Plano de desenvolvimento |
| NumLot | Number(009,0) | Sim | Nr. do lote em que foi gerada a avaliação |
| DatPdi | Date | Sim | Data limite para efetuar o plano de desenvolvimento |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local Avaliado |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo Avaliado |
| CodCic | Number(003,0) | Sim | Código do ciclo de avaliação |
| MedAva | Number(005,2) | Sim | Média da Avaliação de Performance |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpAva
- TipAva

---

## Índices

### R077APAIndice2

**Tipo:** Não unico

Campos:
- EmpAva
- TclAva
- CadAva
- CodCic

---

## Relacionamentos

### IR_R077APA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

