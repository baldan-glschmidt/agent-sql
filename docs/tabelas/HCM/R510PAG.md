# R510PAG

## Descrição

Currículo Web - Páginas do Layout

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(003,0) | Não | Código do perfil |
| IdiLay | Number(001,0) | Não | Idioma do layout - define o idioma de apresentação |
| CodPag | Number(003,0) | Não | Código da página do layout |
| SeqPag | Number(003,0) | Sim | Sequência da página |
| NomPag | String(100) | Sim | Nome da página |
| PreCad | String(001) | Sim | Indica se a página é de pré-cadastro de candidatos |

---

## Chave Primária

- CodPer
- IdiLay
- CodPag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R510PAG_000

**Tabela:** R510PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

