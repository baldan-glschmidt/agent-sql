# R034DOC

## Descrição

Fotos de Documentos do Colaborador

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| DatDoc | Date | Não | Data do Documento |
| TipDoc | Number(004,0) | Não | Tipo do Documento |
| SeqDoc | Number(004,0) | Não | Sequência do Documento |
| DocEmp | Image | Sim | Imagem do Documento |
| ObsDoc | String(499) | Sim | Observação |
| NomArq | String(250) | Sim | Nome Arquivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatDoc
- TipDoc
- SeqDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034DOC_002

**Tabela:** R034CPL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R034DOC_004

**Tabela:** R022DOC

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |

