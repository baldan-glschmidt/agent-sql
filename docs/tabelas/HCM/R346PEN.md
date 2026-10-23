# R346PEN

## Descrição

eSocial JR - Informações de Tributos - Informação dos beneficiários da pensão alimentícia

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodPro | Number(009,0) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CmpPag | Date | Não | Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença |
| CodRec | Number(006,0) | Não | Código de Receita - CR relativo a Imposto de Renda Retido na Fonte |
| TipRen | Number(002,0) | Não | Tipo Rendimento |
| CodDep | Number(002,0) | Sim | Código do Dependente |
| CpfDep | Number(011,0) | Não | Número do CPF do Dependente |
| VlrPen | Number(015,2) | Sim | Valor relativo à dedução do rendimento tributável correspondente a pagamento de pensão alimentícia |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPro
- CmpPag
- CodRec
- TipRen
- CpfDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
