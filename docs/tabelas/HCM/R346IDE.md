# R346IDE

## Descrição

eSocial JR - Informações de Tributos - Informações de dependentes não cadastrados pelo S-2200/S-2205/S-2300

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
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
| CodDep | Number(002,0) | Sim | Código do Dependente |
| CpfDep | Number(011,0) | Não | Número do CPF do Dependente |
| DatNas | Date | Sim | Data de Nascimento |
| NomDep | String(070) | Sim | Nome do Dependente |
| DepIrr | String(001) | Sim | Somente informar este campo em caso de dependente do trabalhador para fins de dedução de seu rendimento tributável pelo Imposto de Renda |
| TipDep | Number(002,0) | Sim | Tipo de Dependente eSocial |
| DesDep | String(100) | Sim | Descrição da dependência |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPro
- CmpPag
- CpfDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
