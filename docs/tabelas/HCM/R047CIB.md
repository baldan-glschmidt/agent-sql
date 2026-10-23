# R047CIB

## Descrição

Composição dos CIF's

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCif | Number(003,0) | Não | Código de Integração Financeira |
| SeqCif | Number(002,0) | Não | Sequência |
| SinCif | String(001) | Sim | Sinal de Soma |
| CodTab | Number(003,0) | Sim | Código da Tabela Eventos |
| CodEve | Number(004,0) | Sim | Código do Evento |

---

## Chave Primária

- CodCif
- SeqCif

---

## Índices

### R047CIBIndice2

**Tipo:** Não unico

Campos:
- CodCif

---

## Relacionamentos

### IR_R047CIB_000

**Tabela:** R047CIF

| Origem | Destino |
|--------|---------|
| CodCif | CodCif |

### IR_R047CIB_004

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

