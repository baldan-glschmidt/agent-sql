# R145REQ

## Descrição

LNT - Requisitos do colaborador

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatLnt | Date | Não | Data do levantamento de necessidades de treinamento (LNT) |
| SeqRqu | Number(003,0) | Não | Sequencia do requisito |
| TipReq | Number(001,0) | Sim | Tipo de requisito |
| CodCpt | Number(009,0) | Sim | Código da competência |
| RevCpt | String(010) | Sim | Determina qual Revisão da Competência foi adquirida na data informada |
| PrfApl | Number(004,0) | Sim | Indica qual foi o Perfil de aplicação adquirido para esta competência |
| CodCua | Number(009,0) | Sim | Curso de aperfeiçoamento |
| CodCuf | Number(004,0) | Sim | Curso de formação |
| SitReq | Number(001,0) | Sim | Define a situação do requisito considerando os critérios de análise |
| OriReq | Number(001,0) | Sim | Origem do requisito |
| ExiReq | String(001) | Sim | Exigência do requisito |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatLnt
- SeqRqu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R145REQ_003

**Tabela:** R145COL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatLnt | DatLnt |

