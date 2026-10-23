# R104TES

## Descrição

JR - Testemunhas

---

## Resumo

- Campos: 17
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| CodTes | Number(004,0) | Não | Código da Testemunha |
| EmpTes | Number(004,0) | Sim | Empresa da testemunha |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Código de colaborador da testemunha |
| TipTes | String(001) | Sim | Tipo de Testemunha |
| EndRua | String(040) | Sim | Endereço da Testemunha |
| EndNum | String(006) | Sim | Número |
| EndCpl | String(025) | Sim | Complemento do Endereço |
| CodCid | Number(007,0) | Sim | Código da Cidade |
| CodBai | Number(004,0) | Sim | Código do Bairro |
| EndCep | Number(008,0) | Sim | Código do CEP |
| NumTel | String(020) | Sim | Número do Telefone |
| ObsTes | String(250) | Sim | Observações sobre a Testemunha |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |

---

## Chave Primária

- NumEmp
- CodPrc
- CodTes

---

## Índices

### R104TESIndice2

**Tipo:** Não unico

Campos:
- EmpTes
- TipCol
- NumCad

---

## Relacionamentos

### IR_R104TES_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

