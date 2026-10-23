# R126ANU

## Descrição

Anúncios - Cadastro de Anúncios

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodVag | String(010) | Não | Código da Vaga usado na publicação do anúncio |
| DesVag | String(200) | Sim | Descrição da vaga usada na publicação do anúncio |
| LocVag | String(200) | Sim | Descreva a localidade da vaga |
| AtrVag | String(9000) | Sim | Descreva as atribuições e responsabilidades do ocupante da vaga |
| ReqVag | String(9000) | Sim | Descreva os requisitos que o candidato deve atender para ocupar a vaga |
| BenVag | String(2000) | Sim | Benefícios oferecidos ao candidato |
| ApnVag | Number(001,0) | Sim | Define a origem do número de vagas apresentadas na publicação do anúncio |
| NumVag | String(200) | Sim | Texto usado para descrever o número de vagas que devem ser publicadas |
| DatCri | Date | Sim | Data de criação do anúncio |
| CodRes | Number(010,0) | Sim | Código do Usuário Responsável pelo Anúncio |
| CodPai | Number(004,0) | Sim | País da vaga |
| CodEst | String(004) | Sim | Estado da vaga |
| CodCid | Number(007,0) | Sim | Cidade da vaga |

---

## Chave Primária

- CodVag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
