# R077DAV

## Descrição

Avaliação - Definições para tipo avaliador

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipAva | Number(001,0) | Não | Foco da Avaliação |
| DefMet | String(001) | Sim | Define se o avaliador estabelece meta |
| AprNot | String(001) | Sim | Define se apresenta a última nota/meta atribuída pelo avaliador |
| DetAva | String(001) | Sim | Permite que o avaliador detalhe a nota do item avaliado |
| VisNot | String(001) | Sim | Define como será a visualização da última nota do avaliado |
| VisObs | String(001) | Sim | Permite visualização de observação ao avaliado |
| DefPDI | Number(001,0) | Sim | Define a forma de utilização do PDI na Avaliação de Desempenho e Competência |
| GerRes | Number(001,0) | Sim | Permite definir a origem de realização do PDI: Item e/ou Avaliação. |
| ResPdi | String(001) | Sim | Respeita data limite estabelecida para o plano de desenvolvimento |
| LimPer | Number(002,0) | Sim | Percentual para limitar a geração de avaliação |
| LimMin | Number(004,0) | Sim | Quantidade mínima de avaliações a gerar |
| LimMax | Number(004,0) | Sim | Quantidade máxima de avaliações a gerar |
| InfAva | String(001) | Sim | Permite informar avaliador individual para este tipo de avaliação |
| PerRea | String(001) | Sim | Define se o avaliador pode reabrir avaliações |
| AceAva | Number(001,0) | Sim | Define qual é o acesso na WEB quando o usuário é o avaliado |
| MaxHCo | Number(002,0) | Sim | Quantidade máxima de habilidades complementares |

---

## Chave Primária

- TipAva

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
