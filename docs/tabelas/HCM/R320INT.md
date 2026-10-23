# R320INT

## Descrição

Cadastro de Integrações via Consulta de Pendências

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ID | String(010) | Não | Identificador único da integração |
| QTDRET | Number(009,0) | Sim | Quantidade máxima de registros retornados. |
| QTDDIA | Number(003,0) | Não | Quantidade máxima de dias para retorno das pendencias. |
| CONFRECEB | String(001) | Sim | Confirmar recebimento automaticamente |
| STAINT | String(001) | Sim | Integraçao ativa |
| CARINI | String(001) | Sim | Realizado carga inicial |
| RGRWS1 | Number(003,0) | Sim | Regra Integração |

---

## Chave Primária

- ID

---

## Índices

### R320INTINDICE_1

**Tipo:** Não unico

Campos:
- ID
- CONFRECEB

---

## Relacionamentos

Nenhum relacionamento cadastrado.
