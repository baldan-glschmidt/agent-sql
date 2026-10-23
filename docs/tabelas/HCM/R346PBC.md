# R346PBC

## Descrição

eSocial JR - Informações de Tributos - Identificação dos períodos e da base de cálculo dos tributos

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodPro | Number(009,0) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CmpPag | Date | Não | Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença |
| PerRef | Date | Não | Mês/ano de referência das informações |
| VrCpMs | Number(015,2) | Sim | Valor da base de cálculo da contribuição previdenciária |
| VrCp13 | Number(015,2) | Sim | Valor da base de cálculo da contribuição previdenciária referente ao 13º salário |
| VrIrrf | Number(015,2) | Sim | Valor base do rendimento tributável do Imposto de Renda |
| VrIr13 | Number(015,2) | Sim | Valor base do rendimento tributável do Imposto de Renda referente ao 13º salário - Tributação exclusiva |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPro
- CmpPag
- PerRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
