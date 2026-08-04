# E000ILP

## Descrição

Tabelas - Lista de Presentes- Itens

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeIlp | Number(009,0) | Não | NÃºmero de sequÃªncia do item |
| IdeLpr | Number(009,0) | Não | NÃºmero da lista de presente |
| CodPro | String(014) | Sim | CÃ³digo do produto da lista |
| CodDer | String(007) | Sim | CÃ³digo da derivaÃ§Ã£o do produto da lista |
| SitIte | String(001) | Não |  |
| QtdIte | Number(014,5) | Sim | Quantidade pedida na lista |
| UsuGer | Number(010,0) | Sim | UsuÃ¡rio responsÃ¡vel pela inclusÃ£o do item |
| UsuAlt | Number(010,0) | Sim | UsuÃ¡rio responsÃ¡vel pela Ãºltima alteraÃ§Ã£o |
| DatAlt | Date | Sim | Data da geração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| AcePrs | String(001) | Não | Indicativo se aceita item similar |

---

## Chave Primária

- IdeIlp

---

## Índices

### E000ILPIndice1

**Tipo:** Não unico

Campos:
- CodPro
- CodDer

### E000ILPIndice2

**Tipo:** Não unico

Campos:
- IdeLpr

---

## Relacionamentos

### IR_E000ILP_001

**Tabela:** E000LPR

| Origem | Destino |
|--------|---------|
| IdeLpr | IdeLpr |

