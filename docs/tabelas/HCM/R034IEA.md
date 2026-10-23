# R034IEA

## Descrição

Informações Empregador Contratante de Aprendiz

---

## Resumo

- Campos: 14
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| CodOem | Number(008,0) | Sim | Código da Outra Empresa Contratação Indireta |
| TipIns | Number(001,0) | Não | Tipo de Inscrição do Empregador de Contratação Indireta do Aprendiz (CNPJ/CPF) |
| NumIns | Number(015,0) | Não | Número da Inscrição do Contratante Indireto do Aprendiz |
| CfjIns | String(014) | Sim | Número da Inscrição do Contratante Indireto do Aprendiz |
| IndCtr | Number(001,0) | Sim | Indicativo de Contratação |
| OemQua | Number(008,0) | Sim | Código da Outra Empresa Entidade Qualificadora |
| NumQua | Number(014,0) | Sim | CNPJ Entidade Qualificadora |
| CfjQua | String(014) | Sim | CNPJ Entidade Qualificadora |
| OemPra | Number(008,0) | Sim | Código da Outra Empresa Atividades Práticas |
| NumPra | Number(014,0) | Sim | CNPJ Atividades Práticas |
| CfjPra | String(014) | Sim | CNPJ Atividades Práticas |

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

### IR_R034IEA_002

**Tabela:** R034CPL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

