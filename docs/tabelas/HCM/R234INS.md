# R234INS

## Descrição

Evento - Instrutores

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| DatIni | Date | Não | Data Inicial do Horário |
| HorIni | Number(005,0) | Não | Hora Inicial do horário |
| CodPes | Number(009,0) | Não | Código da Pessoa |
| ObsIns | String(500) | Sim | Dados complementares do instrutor |

---

## Chave Primária

- CodEvn
- DatIni
- HorIni
- CodPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234INS_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234INS_003

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

