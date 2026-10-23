# R030LFB

## Descrição

Filiais - Base das Liminares

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpLim | Date | Não | Competência da Liminar |
| CodLim | Number(002,0) | Não | Código da Liminar |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| SeqLim | Number(003,0) | Não | Sequência |
| TipLim | Number(001,0) | Sim | Tipo |
| CodEve | Number(004,0) | Sim | Código do Evento |
| CrtEve | String(003) | Sim | Característica |
| TipInc | Number(001,0) | Sim | Incidência |

---

## Chave Primária

- NumEmp
- CodFil
- CmpLim
- CodLim
- TabEve
- SeqLim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030LFB_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

