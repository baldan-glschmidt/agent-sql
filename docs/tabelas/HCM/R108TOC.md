# R108TOC

## Descrição

Tipos de Ocorrência

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodOco | Number(006,0) | Não | Código Ocorrência |
| DesOco | String(030) | Sim | Descrição Ocorrência |
| CodDoe | String(004) | Sim | Classificação Internacional de Doenças |
| CodCid | String(010) | Sim | Código da Classificação Internacional de Doenças |
| CodSub | String(003) | Sim | Identificação do subgrupo da CID-10 |
| GerNot | String(001) | Sim | Gerar notificação compulsória de doença, agravo ou evento de saúde |
| PerNot | Number(001,0) | Sim | Informar se a periodicidade para notificação compulsória será em horas ou dia |
| PraNot | Number(002,0) | Sim | Quantidade de horas/dias para realizar notificação compulsória |
| CodCia | String(010) | Sim | Código único do CIAP-2 |

---

## Chave Primária

- CodOco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
