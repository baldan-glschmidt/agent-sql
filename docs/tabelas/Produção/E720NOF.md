# E720NOF

## Descrição

Ficha - Roteiro - Narrativas p/ Operações (Instruções)

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodNof | String(006) | Não | Código da Narrativa técnica p/ operação (Instruções de trabalho) |
| DesNof | String(050) | Não | Descrição da Narrativa (sobre a instrução de trabalho na operação) |
| ObsNof | String(240) | Sim | Observação (sobre a instrução de trabalho na operação) |
| CodEtg | Number(004,0) | Sim | Código do Estágio (Opcional) |
| CodOpr | String(006) | Sim | Código da operação (opcional) |
| DatAlt | Date | Sim | Data da geração/alteração |
| CodUsu | Number(010,0) | Sim | Usuário geração/alteração |

---

## Chave Primária

- CodEmp
- CodNof

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
