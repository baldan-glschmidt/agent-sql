# R124AFA

## Descrição

Colaborador - Afastamentos no Emprego Anterior

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Candidato |
| NumCad | Number(009,0) | Não | Cadastro do Candidato |
| SeqAdm | Number(002,0) | Não | Sequência da Admissão na Data |
| DatAfa | Date | Não | Data do Afastamento |
| DatTer | Date | Sim | Data Término do Afastamento |
| SitAfa | Number(003,0) | Sim | Situação do Afastamento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqAdm
- DatAfa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124AFA_003

**Tabela:** R124HEA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| SeqAdm | SeqAdm |

### IR_R124AFA_006

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| SitAfa | CodSit |

