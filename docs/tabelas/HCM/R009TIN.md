# R009TIN

## Descrição

Gestão de Incidentes - Tratamento dos Incidentes

---

## Resumo

- Campos: 16
- Chave Primária: 5 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatApi | Date | Não | Data da Apuração de Incidente |
| SeqApi | Number(002,0) | Não | Seqüência da Apuração de Incidente |
| CodGIn | Number(003,0) | Sim | Código da Definição de Gestão de Incidentes |
| SugPen | Number(003,0) | Sim | Código da Penalidade Sugerida |
| DocPen | Number(003,0) | Sim | Código da Penalidade no Documento |
| CodPen | Number(003,0) | Sim | Código da Penalidade |
| CodJuP | Number(002,0) | Sim | Código da Justificativa Alteração Penalidade |
| StaTIn | Number(001,0) | Sim | Status Tratamento Incidente |
| SeqNot | Number(002,0) | Sim | Sequência do Histórico de Anotações |
| DatGer | Date | Sim | Data Geração Incidente |
| OrdTra | Number(002,0) | Sim | Ordem Tratamento Incidentes |
| IniAfa | Date | Sim | Data do Afastamento |
| FimAfa | Date | Sim | Data do Término do Afastamento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatApi
- SeqApi

---

## Índices

### R009TINindice2

**Tipo:** Não unico

Campos:
- CodGIn
- DatApi

### R009TINindice3

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- OrdTra
- DatApi
- SeqApi

---

## Relacionamentos

Nenhum relacionamento cadastrado.
