# R975ACC

## Descrição

Histórico de acesso a Forms/Cubo/Relatórios - Deprecada

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| MODID | Number(005,0) | Não | Id do Módulo |
| CODUSU | Number(010,0) | Não | Código do usuário |
| ITEMID | Number(010,0) | Não | Identificador do item |
| DATACC | Date | Não | Data |
| TIMACC | Number(010,0) | Não | Hora |
| ITKIND | Number(001,0) | Sim | Tipo do item |

---

## Chave Primária

- MODID
- CODUSU
- ITEMID
- DATACC
- TIMACC

---

## Índices

### R975ACCR970ACCINDEX1

**Tipo:** Não unico

Campos:
- MODID
- CODUSU

### R975ACCR970ACCINDEX2

**Tipo:** Não unico

Campos:
- MODID
- CODUSU
- ITKIND

---

## Relacionamentos

Nenhum relacionamento cadastrado.
