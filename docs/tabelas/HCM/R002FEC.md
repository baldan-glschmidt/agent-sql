# R002FEC

## Descrição

Datas Feriados

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFer | Number(004,0) | Não | Código da Tabela de Feriados |
| DatFer | Date | Não | Data do Feriado |
| DesFer | String(030) | Sim | Descrição do Feriado |
| DisVtr | String(001) | Sim | Distribuir Vale Transporte |
| UtiSrv | Number(001,0) | Sim | Dia da Semana para Serviços |

---

## Chave Primária

- CodFer
- DatFer

---

## Índices

### R002FECIndice2

**Tipo:** Não unico

Campos:
- DatFer

---

## Relacionamentos

### IR_R002FEC_000

**Tabela:** R002FEM

| Origem | Destino |
|--------|---------|
| CodFer | CodFer |

