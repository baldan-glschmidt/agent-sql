# R059RSR

## Descrição

Coletores/Funções da Solicitação

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSoR | Number(002,0) | Não | Código da Solicitação |
| CodPlt | Number(005,0) | Não | Código do Site |
| RlgSoR | Number(005,0) | Não | Código do Coletor na Solicitação |
| FncSoR | Number(002,0) | Não | Código da Função na Solicitação |

---

## Chave Primária

- CodSoR
- CodPlt
- RlgSoR
- FncSoR

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R059RSR_000

**Tabela:** R059SOR

| Origem | Destino |
|--------|---------|
| CodSoR | CodSoR |

