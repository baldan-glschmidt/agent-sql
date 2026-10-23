# R300PAR

## Descrição

Parâmetros das Stored Procedures

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipPat | Number(002,0) | Não | Tipo do Processo Automático |
| CodPro | Number(003,0) | Não | Código do Processo |
| CodPar | Number(003,0) | Não | Código do Parâmetro |
| TipPar | Number(001,0) | Sim | Tipo Parâmetro |
| DesPar | String(030) | Sim |  |
| ValPar | String(050) | Sim | Valor do Parâmetro |

---

## Chave Primária

- TipPat
- CodPro
- CodPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R300PAR_001

**Tabela:** R300PRO

| Origem | Destino |
|--------|---------|
| TipPat | TipPat |
| CodPro | CodPro |

