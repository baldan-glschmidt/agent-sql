# R001HDI

## Descrição

Horas Dispensadas

---

## Resumo

- Campos: 3
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodHDi | Number(003,0) | Não | Código das Horas Dispensadas |
| DesHDi | String(030) | Sim | Descrição das Horas Dispensadas |
| SitHDi | Number(003,0) | Sim | Situação das Horas Dispensadas |

---

## Chave Primária

- CodHDi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R001HDI_002

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| SitHDi | CodSit |

