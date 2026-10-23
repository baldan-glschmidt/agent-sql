# R046LIQ

## Descrição

Controle de Pagamento

---

## Resumo

- Campos: 30
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CmpPag | Date | Não | Competência |
| SeqPag | Number(002,0) | Não | Sequência |
| OriPag | Number(002,0) | Sim | Rotina Origem |
| DatPag | Date | Sim | Data do Pagto |
| ValOri | Number(011,2) | Sim | Valor Original a ser Pago |
| ValPag | Number(011,2) | Sim | Valor Pago |
| DatRf1 | Date | Sim | Data de Referência 1 |
| DatRf2 | Date | Sim | Data de Referência 2 |
| CodCal | Number(005,0) | Sim | Código Cálculo Gerador |
| DatGer | Date | Sim | Data Geração |
| HorGer | Number(005,0) | Sim | Hora Geração |
| CodDep | Number(002,0) | Sim | Código do dependente |
| PagApr | String(001) | Sim | Pagamento Aprovado |
| PagGer | String(001) | Sim | Pagamento Gerado |
| StaPag | Number(001,0) | Sim | Status do Pagamento |
| CodBan | Number(004,0) | Sim | Código do Banco |
| CodAge | Number(005,0) | Sim | Código da Agência |
| ConBan | Number(012,0) | Sim | Conta Bancária |
| DigBan | String(003) | Sim | Dígito da Conta Bancária |
| TpCtba | Number(001,0) | Sim | Tipo de Conta Bancária |
| ModPag | String(001) | Sim | Modo de Pagamento do Salário |
| UsuApr | Number(009,0) | Sim | Código do Usuário que aprovou o pagamento |
| UsuGer | Number(009,0) | Sim | Código do Usuário que gerou o pagamento |
| DatApr | Date | Sim | Data Aprovação |
| HorApr | Number(005,0) | Sim | Hora Aprovação |
| TpcPix | Number(002,0) | Sim | Tipo de Chave Pix - Pagamento Instantâneo |
| ChvPix | String(100) | Sim | Chave Pix - Pagamento Instantâneo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpPag
- SeqPag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
