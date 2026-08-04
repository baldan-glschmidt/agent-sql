# E095DAA

## Descrição

Cadastros - Fornecedores - DAP - Acessória Associadas

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
| CodDap | String(025) | Não | Código da DAP - Declaração de Aptidão ao Pronaf |
| CodDaa | String(025) | Não | Código da DAP - Declaração de Aptidão ao Pronaf |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodDap
- CodDaa

---

## Índices

### E095DAAIndice1

**Tipo:** Não unico

Campos:
- CodDaa

---

## Relacionamentos

### IR_E095DAA_000

**Tabela:** E095DAP

| Origem | Destino |
|--------|---------|
| CodDap | CodDap |

### IR_E095DAA_001

**Tabela:** E095DAP

| Origem | Destino |
|--------|---------|
| CodDaa | CodDap |

