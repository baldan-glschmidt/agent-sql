# R234FRE

## Descrição

Evento - Controle de Frequência

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| CodPes | Number(009,0) | Não | Código da Pessoa |
| DatIni | Date | Não | Data Inicial do Horário |
| HorIni | Number(005,0) | Não | Hora Inicial do horário |

---

## Chave Primária

- CodEvn
- CodPes
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234FRE_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234FRE_001

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

