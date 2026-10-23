# R033DOC

## Descrição

Fotos de Documentos do Colaborador

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPes | Number(009,0) | Não | Código da Pessoa |
| DatDoc | Date | Não | Data do Documento |
| TipDoc | Number(004,0) | Não | Tipo do Documento |
| SeqDoc | Number(004,0) | Não | Sequência do Documento |
| ImgDoc | Image | Sim | Imagem do Documento |
| ObsDoc | String(499) | Sim | Observação |
| NomArq | String(250) | Sim | Nome Arquivo |

---

## Chave Primária

- CodPes
- DatDoc
- TipDoc
- SeqDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R033DOC_000

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

### IR_R033DOC_002

**Tabela:** R022DOC

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |

