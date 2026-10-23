# R105LTU

## Descrição

Cadastro de Avaliadores - Local/Turno

---

## Resumo

- Campos: 13
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da filial |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodTur | Number(001,0) | Não | Código do Turno |
| DatIni | Date | Não | Data de início |
| TpAval | Number(001,0) | Não | Foco da Avaliação |
| DatFim | Date | Sim | Data de término |
| EmpAvl | Number(004,0) | Sim | Empresa do avaliador |
| TipAvl | Number(001,0) | Sim | Tipo do Colaborador Avaliador |
| CadAvl | Number(009,0) | Sim | Cadastro do Avaliador |
| DefMut | String(001) | Sim | Na avaliação oposta o avaliador assume o papel de avaliado |
| CodCic | Number(003,0) | Sim | Código do ciclo de avaliação |

---

## Chave Primária

- NumEmp
- CodFil
- TabOrg
- NumLoc
- CodTur
- DatIni
- TpAval

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R105LTU_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

