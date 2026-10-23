# R036DOC

## Descrição

Documentos da Pensão

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| CodDep | Number(002,0) | Não | Código do dependente |
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
- CodDep
- DatDoc
- TipDoc
- SeqDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R036DOC_005

**Tabela:** R022DOC

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |

