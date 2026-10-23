# R124HEP

## Descrição

Colaborador - Emprego Anterior - Períodos Contribuição

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SeqAdm | Number(002,0) | Não | Sequência da Admissão na Data |
| DinCon | Date | Não | Data de Início da Contribuição |
| DfiCon | Date | Sim | Data de Término Contribuição |
| FatCon | Number(005,2) | Sim | Fator T.Servico |
| FaiCon | Number(002,0) | Sim | Faixa de Contribuição |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqAdm
- DinCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124HEP_003

**Tabela:** R124HEA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| SeqAdm | SeqAdm |

