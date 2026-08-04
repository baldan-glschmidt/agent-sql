# E019TST

## Descrição

Tabelas - Substituição de ICMS

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
| CodTst | String(003) | Não | Código do tipo de ICMS substituído |
| DesTst | String(030) | Não | Descrição do ICMS substituído |
| AbrTst | String(010) | Não | Abreviatura do ICMS substituído |
| CalSub | Number(001,0) | Não | Critério para o cálculo das substituições tributárias ICMS, PIS, COFINS |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| CodAnt | Number(001,0) | Sim | Código que identifica o tipo da Antecipação Tributária |

---

## Chave Primária

- CodTst

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
