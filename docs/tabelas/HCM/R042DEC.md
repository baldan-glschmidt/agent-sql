# R042DEC

## Descrição

HomologNet - Informações 13° Salário

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| AnoPag | Number(004,0) | Não | Ano Pagamento |
| TipPag | Number(001,0) | Sim | Salários Pagos |
| ValPag | Number(011,2) | Sim | Valor Pago |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- AnoPag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042DEC_002

**Tabela:** R042COL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

