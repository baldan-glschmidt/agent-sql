# R234LIS

## Descrição

Evento - Lista de divulgação

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| CodPes | Number(009,0) | Não | Código da Pessoa |

---

## Chave Primária

- CodEvn
- CodPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234LIS_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234LIS_001

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

