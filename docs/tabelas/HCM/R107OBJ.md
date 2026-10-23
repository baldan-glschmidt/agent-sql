# R107OBJ

## Descrição

PDI - Objetivos do plano de desenvolvimento

---

## Resumo

- Campos: 21
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo de colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| CodPln | Number(004,0) | Não | Código do Plano de Desenvolvimento |
| CodObj | Number(002,0) | Não | Código do Objetivo |
| DesObj | String(200) | Sim | Descrição do Objetivo |
| PraObj | Date | Sim | Prazo do Objetivo |
| CodHte | String(006) | Sim | Código da Habilidade Técnica |
| CodHpe | String(004) | Sim | Código da Habilidade Pessoal |
| FamCnc | String(004) | Sim | Família do Conhecimento |
| CodCnc | String(005) | Sim | Código do Conhecimento |
| CodCpt | Number(009,0) | Sim | Competência relacionada ao objetivo que será desenvolvida |
| RevCpt | String(010) | Sim | Revisão da competência relacionada ao objetivo que será desenvolvida |
| PrfApl | Number(004,0) | Sim | Perfil de aplicação da competência que será desenvolvido |
| SitObj | Number(001,0) | Sim | Situação do Objetivo |
| ColAva | String(001) | Sim | Colaborador Avaliado |
| ColAvr | String(001) | Sim | Colaborador Avaliador |
| CodCic | Number(003,0) | Sim | Código do ciclo de avaliação |
| TipAva | Number(002,0) | Sim | Sequência do tipo de avaliação |
| SeqAva | Number(002,0) | Sim | Sequência da avaliação |
| IdeObj | Number(006,0) | Sim | Identificação dos objetivos |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPln
- CodObj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R107OBJ_003

**Tabela:** R107PDI

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodPln | CodPln |

