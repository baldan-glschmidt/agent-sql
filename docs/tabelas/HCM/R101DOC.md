# R101DOC

## Descrição

Avaliação de Resultado - Objetivos - Acompanhamento - Documentos

---

## Resumo

- Campos: 13
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| TipAva | Number(002,0) | Não | Sequência do tipo de avaliação |
| SeqAva | Number(002,0) | Não | Sequência da avaliação |
| IdeObj | Number(006,0) | Não | Identificação dos objetivos |
| DatAco | Date | Não | Data do Acompanhamento |
| SeqDoc | Number(003,0) | Não | Sequência do Documento |
| DesDoc | String(100) | Sim | Descrição do Documento |
| Imagem | Image | Sim | Imagem |
| AnoDoc | String(2000) | Sim | Anotações do Documento |
| NomArq | String(250) | Sim | Nome do Arquivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- TipAva
- SeqAva
- IdeObj
- DatAco
- SeqDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R101DOC_004

**Tabela:** R101CTA

| Origem | Destino |
|--------|---------|
| CodCic | CodCic |
| TipAva | TipAva |

### IR_R101DOC_006

**Tabela:** R101RES

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCic | CodCic |
| TipAva | TipAva |
| SeqAva | SeqAva |
| IdeObj | IdeObj |

