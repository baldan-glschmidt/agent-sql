# R030PDI

## Descrição

Empresa - Histórico de perfis de PDI

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| DatAlt | Date | Não | Data da Alteração do perfil de PDI |
| CodPer | Number(004,0) | Sim | Perfil de PDI Web |

---

## Chave Primária

- NumEmp
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030PDI_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R030PDI_002

**Tabela:** R107PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

