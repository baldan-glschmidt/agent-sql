# R122CAA

## Descrição

Candidatos Externos - Áreas Pretendidas

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro do candidato |
| SeqAre | Number(003,0) | Não | Sequência para permitir determinar a prioridade |
| AreAtu | Number(003,0) | Não | Código da área desejada |

---

## Chave Primária

- NumCan
- SeqAre
- AreAtu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CAA_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R122CAA_002

**Tabela:** R024AAT

| Origem | Destino |
|--------|---------|
| AreAtu | AreAtu |

