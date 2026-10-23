# R031PGE

## Descrição

Geração de Escalas - Parâmetros

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEqp | Number(004,0) | Não | Código da Equipe |
| CodTur | Number(001,0) | Não | Código do Turno |
| CodCat | Number(003,0) | Não | Código da Categoria |
| InfPre | String(001) | Sim | Informar Preferências |
| SomTot | String(001) | Sim | Somar nos Totais |
| DisFlg | Number(002,0) | Sim | Distribuir Folgas Proporcionalmente |

---

## Chave Primária

- CodEqp
- CodTur
- CodCat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R031PGE_000

**Tabela:** R031EQP

| Origem | Destino |
|--------|---------|
| CodEqp | CodEqp |

### IR_R031PGE_002

**Tabela:** R031CAT

| Origem | Destino |
|--------|---------|
| CodCat | CodCat |

