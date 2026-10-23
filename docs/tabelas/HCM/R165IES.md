# R165IES

## Descrição

BS - Itens Escala Trajeto

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEtr | Number(006,0) | Não | Código Escala |
| SeqEtr | Number(002,0) | Não | Dia do Trajeto |
| CodTra | Number(006,0) | Sim | Código Trajeto |

---

## Chave Primária

- CodEtr
- SeqEtr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R165IES_000

**Tabela:** R165ESC

| Origem | Destino |
|--------|---------|
| CodEtr | CodEtr |

### IR_R165IES_002

**Tabela:** R165TRA

| Origem | Destino |
|--------|---------|
| CodTra | CodTra |

