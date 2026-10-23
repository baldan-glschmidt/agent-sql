# R086DOC

## Descrição

Documentos do Acidente de Trabalho

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAct | Date | Não | Data Acidente de Trabalho |
| HorAct | Number(005,0) | Não | Hora Acidente de Trabalho |
| DatDoc | Date | Não | Data do Documento |
| SeqDoc | Number(004,0) | Não | Sequência do Documento |
| DocEmp | Image | Sim | Imagem do Documento |
| ObsDoc | String(499) | Sim | Observação |
| NomArq | String(250) | Sim | Nome Arquivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAct
- HorAct
- DatDoc
- SeqDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
