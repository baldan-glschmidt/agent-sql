# R038PIS

## Descrição

Histórico de Alterações de PIS

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SeqAlt | Number(009,0) | Não | Sequência Alteração |
| DatAlt | Date | Não | Data que o novo PIS passa a ser utilizado no eSocial. |
| DatHor | Number(014,6) | Sim | Data e Hora da alteração de PIS |
| MotPis | Number(001,0) | Sim | Motivo de Alteração do PIS |
| NumPis | Number(011,0) | Sim | Número do PIS/PASEP |
| PisAnt | Number(011,0) | Sim | Número do PIS/PASEP Anterior |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038PIS_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

