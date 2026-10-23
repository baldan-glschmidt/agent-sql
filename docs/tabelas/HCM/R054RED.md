# R054RED

## Descrição

Remuneração - Diretor

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| ComRem | Date | Não | Competência da Remuneração |
| ValRem | Number(011,2) | Sim | Valor da Remuneração |
| PerCon | Number(004,2) | Sim | Percentual de Contribuição |
| FaiCon | Number(004,2) | Sim | Faixa de Contribuição |
| ValCon | Number(011,2) | Sim | Valor da Contribuição |
| ValRec | Number(011,2) | Sim | Valor a Ser Recolhido |
| SalCon | Number(011,2) | Sim | Salário Contribuição |
| ValDed | Number(011,2) | Sim | Valor da Dedução |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- ComRem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R054RED_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

