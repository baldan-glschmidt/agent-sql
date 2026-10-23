# R998USP

## Descrição

Parâmetros de stored procedure do usuário

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| StpNam | String(050) | Não | Nome da stored procedure |
| ParNam | String(032) | Não | Nome do parâmetro |
| ParSeq | Number(010,0) | Não | Ordem de sequência do parâmetro |
| ParTyp | Number(010,0) | Não | Tipo do parâmetro (IN/OUT/[IN/OUT]) |
| DatTyp | Number(010,0) | Não | Tipo do dado |
| DatLen | Number(010,0) | Não | Tamanho do dado |
| DatPre | Number(010,0) | Não | Precisão do dado |
| ObjSis | String(001) | Sim | Identifica se o parâmetro é de sistema ou usuário |

---

## Chave Primária

- StpNam
- ParNam

---

## Índices

### R998USPIndice1

**Tipo:** Unico

Campos:
- StpNam
- ParSeq

---

## Relacionamentos

### IR_R998USP_000

**Tabela:** R998SPN

| Origem | Destino |
|--------|---------|
| StpNam | StpNam |

