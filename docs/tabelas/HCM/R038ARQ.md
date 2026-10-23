# R038ARQ

## Descrição

Anotações para Avaliação - Arquivos

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| DatAno | Date | Não | Data da anotação |
| SeqAno | Number(002,0) | Não | Sequência da anotação |
| SeqArq | Number(002,0) | Não | Sequência do arquivo de anotação |
| NomArq | String(250) | Sim | Nome do Arquivo |
| AnoArq | Image | Sim | Arquivo da Anotação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAno
- SeqAno
- SeqArq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038ARQ_004

**Tabela:** R038AVA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatAno | DatAno |
| SeqAno | SeqAno |

