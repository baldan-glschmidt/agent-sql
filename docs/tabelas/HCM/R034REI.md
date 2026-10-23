# R034REI

## Descrição

Colaborador - Reintegração/Outros Provimentos

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatRei | Date | Sim | Data de Efeito |
| DatRet | Date | Sim | Data efetivo retorno ao trabalho |
| TipRei | Number(001,0) | Sim | Tipo da reintegração |
| CodPro | String(020) | Sim | Número do processo judicial |
| LeiAni | String(013) | Sim | Número e Ano da publicação da Lei de Anistia |
| EmpOri | Number(004,0) | Sim | Código da empresa que originou a reintegração |
| CadOri | Number(009,0) | Sim | Código do cadastro que originou a reintegração |
| NotFic | String(2500) | Sim | Anotação da Ficha |
| PagJui | String(001) | Sim | Pagamento Juízo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
