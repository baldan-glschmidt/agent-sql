# R145DEF

## Descrição

LNT - Definições por empresa

---

## Resumo

- Campos: 24
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| OriRqu | Number(001,0) | Sim | Origem dos requisitos considerados |
| AtuAdi | String(001) | Sim | Considerar requisitos de postos adicionais do colaborador |
| MosCol | Number(001,0) | Sim | Indica quais colaboradores devem ser considerados no LNT |
| MosRqu | Number(001,0) | Sim | Indica quais requisitos devem ser considerados no LNT |
| ReqApe | String(001) | Sim | Considerar requisitos de aperfeiçoamento |
| ValRap | String(001) | Sim | Considerar validade do histórico de aperfeiçoamento |
| RevRap | String(001) | Sim | Considerar revisão do curso do requisito de aperfeiçoamento |
| CerApr | String(001) | Sim | Considerar hist. aperfeiçoamento com certificados de aproveitamento |
| CerPar | String(001) | Sim | Considerar hist. aperfeiçoamento com certificados de participação |
| AbrSap | String(200) | Sim | Situações consideradas válidas para os históricos de aperfeiçoamento |
| ExiRap | Number(001,0) | Sim | Considerar requisitos de aperfeiçoamento do nível de exigência informado |
| ReqCpt | String(001) | Sim | Considerar requisitos de competência |
| PrfRcp | String(001) | Sim | Considerar perfil de aplicação dos requisitos de competência |
| NotRcp | String(001) | Sim | Considerar nota/conceito mínimo ao avaliar requisitos de competência |
| ExiRcp | Number(001,0) | Sim | Considerar requisitos de competência do nível de exigência informado |
| ReqFor | String(001) | Sim | Considerar requisitos de formação |
| ExiRfo | Number(001,0) | Sim | Considerar requisitos de formação do nível de exigência informado |
| AbrSfo | String(200) | Sim | Situações consideradas válidas para os históricos de formação |
| ReqBri | String(001) | Sim | Considerar requisitos exigidos para membros da Brigada |
| ReqCip | String(001) | Sim | Considerar requisitos exigidos para membros da CIPA |
| ReqEpi | String(001) | Sim | Considerar requisitos exigidos pelos EPIs utilizados pelo colaborador |
| AbrGrq | String(200) | Sim | Utilizações do grupo de requisitos que serão consideradas no LNT |
| UsuReq | String(001) | Sim | Permitir o usuário escolher os tipos de requisitos que devem ser considerados |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
