# R060DPA

## Descrição

Definições gerais do processo de acerto

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDAp | Number(002,0) | Não | Código da Definição da Apuração |
| NomFlx | String(255) | Sim | Nome do fluxo de acerto de ponto |
| DiaExp | Number(002,0) | Sim | Quantidade de dias para a expiração |
| DiaLim | Number(002,0) | Sim | Limite de dias após o fechamento do ponto |
| BloExp | String(001) | Sim | Bloqueia a pendência após expirar |
| RejPen | String(001) | Sim | Permite devolver |
| PerAsl | String(001) | Sim | Permite assumir pendência do liderado |
| PerVer | String(001) | Sim | Permite concluir pendência não tratada |

---

## Chave Primária

- CodDAp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
