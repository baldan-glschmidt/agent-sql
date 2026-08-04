# E099IPE

## Descrição

Cadastros - Usuários - Tabela log de processos executados por usuário

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeUpa | Number(009,0) | Não | Identificador de registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E099IPE_FKIndex1

**Tipo:** Não unico

Campos:
- IdeUpa

---

## Relacionamentos

### IR_E099IPE_001

**Tabela:** E099UPA

| Origem | Destino |
|--------|---------|
| IdeUpa | IdeUni |

