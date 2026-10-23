# R046RRA

## Descrição

Informações do RRA

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| TipPro | Number(001,0) | Sim | Tipo do Processo |
| NumPro | String(021) | Sim | Número do Processo |
| NatPro | String(050) | Sim | Natureza do rendimento |
| QtdMes | Number(004,0) | Sim | Quantidade de Meses |
| ValJud | Number(014,2) | Sim | Valor da despesa com custas judiciais |
| ValAdv | Number(014,2) | Sim | Valor da despesa com advogados |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
