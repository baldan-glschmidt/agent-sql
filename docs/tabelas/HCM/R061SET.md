# R061SET

## Descrição

Setores de monitoramento

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Código do Site |
| CodArm | Number(003,0) | Não | Código da área de monitoramento |
| CodSet | Number(003,0) | Não | Código do setor de monitoramento |
| DesSet | String(040) | Sim | Descrição do setor de monitoramento |
| MapSet | Image | Sim | Mapa do setor de monitoramento |

---

## Chave Primária

- CodPlt
- CodArm
- CodSet

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R061SET_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R061SET_001

**Tabela:** R061ARM

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodArm | CodArm |

