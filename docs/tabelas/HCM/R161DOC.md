# R161DOC

## Descrição

Bs - Atendimentos - Documentos

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Coloborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| DatIni | Date | Não | Data Inicial do Atendimento |
| HorIni | Number(005,0) | Não | Hora Inicial do Atendimento |
| SeqDoc | Number(003,0) | Não | Sequência Documento |
| DesDoc | String(030) | Sim | Descrição Documento |
| ImaDoc | Image | Sim | Imagem Documento |
| AnoDoc | String(700) | Sim | Anotação Documento |
| NomArq | String(250) | Sim | Nome Documento |
| QtdZoo | Number(003,0) | Sim | Quantidade Zoom |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni
- SeqDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
