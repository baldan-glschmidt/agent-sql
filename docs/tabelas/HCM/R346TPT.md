# R346TPT

## Descrição

eSocial JR - Informações de Tributos

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
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
| ObsPro | String(999) | Sim | Observação referente ao pagamento de parcela prevista |
| OriInf | Number(001,0) | Sim | Origem das informações dos dados |
| CodAca | Number(007,0) | Sim | Código da Ação gerada pelo cadastro de Ações |
| DatLau | Date | Sim | Data da moléstia grave atribuída pelo laudo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPro
- CmpPag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
