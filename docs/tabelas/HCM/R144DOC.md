# R144DOC

## Descrição

BS - Atendimentos - Documentos

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Colaborador |
| DatSol | Date | Não | Data Solicitação |
| TipSol | Number(003,0) | Não | Tipo Solicitação |
| SeqDoc | Number(003,0) | Não | Sequência Documento |
| DesDoc | String(030) | Sim | Descrição Documento |
| ImaDoc | Image | Sim | Imagem Documento |
| AnoDoc | String(700) | Sim | Anotação Documento |
| NomArq | String(250) | Sim | Nome Arquivo |
| QtdZoo | Number(003,0) | Sim | Quantidade de Zoom |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatSol
- TipSol
- SeqDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R144DOC_004

**Tabela:** R144ATE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatSol | DatSol |
| TipSol | TipSol |

