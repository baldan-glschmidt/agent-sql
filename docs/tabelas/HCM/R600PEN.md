# R600PEN

## Descrição

Pendências geradas TSI

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeNti | String(014) | Não | Identificador de atualização |
| NumFis | String(010) | Sim | Número Serial do Crachá SmartCard |
| NumCra | String(012) | Sim | Número do Crachá |
| NumCpo | String(002) | Sim | Número do Campo a ser Atualizado |
| InfOrm | String(056) | Sim | Informação a ser atualizada |
| StaPen | Number(001,0) | Sim | Tipo de Pendência |

---

## Chave Primária

- IdeNti

---

## Índices

### R600PENIndice2

**Tipo:** Não unico

Campos:
- NumCpo
- NumFis

---

## Relacionamentos

Nenhum relacionamento cadastrado.
