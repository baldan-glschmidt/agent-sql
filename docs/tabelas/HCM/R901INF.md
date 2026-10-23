# R901INF

## Descrição

LGPD - Informações do Dossiê

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
| NumSec | Number(014,0) | Não | Número interno |
| OrdInf | Number(009,0) | Não | Ordem da informação do dossiê |
| NivInf | String(020) | Sim | Nível da informação do dossiê |
| DesInf | String(050) | Sim | Descrição da informação do dossiê |
| ConInf | String(250) | Sim | Conteúdo da informação do dossiê |
| SenInf | String(001) | Sim | Indica se a informação é classificada como sensível perante a LGPD |
| LegInf | String(001) | Sim | Indica se a informação é classificada como obrigação legal perante a LGPD |
| SisInf | String(001) | Sim | Indica se a informação é classificada como obrigatória a nível de sistema |

---

## Chave Primária

- NumSec
- OrdInf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
