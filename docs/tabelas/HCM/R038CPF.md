# R038CPF

## Descrição

Histórico de Alterações de CPF

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAlt | Date | Não | Data que houve alteração do CPF |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| MatEso | String(030) | Sim | Matrícula eSocial |
| ObsTre | String(255) | Sim | Observação mudança de CPF |
| AltCPF | Number(001,0) | Sim | Indicar o tipo de alteração de CPF |
| NovMat | String(030) | Sim | Nova Matrícula eSocial gerada pela alteração de CPF via Portal WEB |
| NroBen | String(020) | Sim | Número do Benefício |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038CPF_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

