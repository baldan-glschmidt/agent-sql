# R975MAC

## Descrição

Histórico de Forms/Cubo/Relatórios mais acessados

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| MODID | Number(005,0) | Não | Id do Módulo |
| CODUSU | Number(010,0) | Não | Código do usuário |
| ITEMID | Number(010,0) | Não | Identificador do item |
| ITKIND | Number(001,0) | Não | Tipo do item |
| DATACC | Date | Não | Data |
| ACCCNT | Number(010,0) | Não | Contador de acessos |

---

## Chave Primária

- MODID
- CODUSU
- ITEMID
- ITKIND

---

## Índices

### R975MACR970ACCINDEX1

**Tipo:** Não unico

Campos:
- MODID
- CODUSU

### R975MACR970ACCINDEX2

**Tipo:** Não unico

Campos:
- MODID
- CODUSU
- ITKIND

---

## Relacionamentos

Nenhum relacionamento cadastrado.
