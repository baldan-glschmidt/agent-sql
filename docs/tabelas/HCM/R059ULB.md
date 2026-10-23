# R059ULB

## Descrição

Leitoras biométricas do usuário

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodUsu | Number(010,0) | Não | Código do Usuário do Processamento |
| CodLei | Number(003,0) | Não | Código da Leitora |
| StaLei | Number(001,0) | Sim | Status da Leitora |

---

## Chave Primária

- CodUsu
- CodLei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R059ULB_001

**Tabela:** R059LBI

| Origem | Destino |
|--------|---------|
| CodLei | CodLei |

