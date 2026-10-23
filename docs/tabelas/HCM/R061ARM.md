# R061ARM

## Descrição

Áreas de monitoramento

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Código do Site |
| CodArm | Number(003,0) | Não | Código da área de monitoramento |
| DesArm | String(040) | Sim | Descrição da área de monitoramento |
| MapArm | Image | Sim | Mapa da área de monitoramento |

---

## Chave Primária

- CodPlt
- CodArm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R061ARM_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

