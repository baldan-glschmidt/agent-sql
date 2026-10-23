# R108EXL

## Descrição

Exames Obrigatórios Local

---

## Resumo

- Campos: 13
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodExa | Number(004,0) | Não | Código Exames |
| UsaAdm | String(001) | Sim | Gerar Solicitação Exame p/ Admissional |
| UsaRet | String(001) | Sim | Gerar Solicitação Exame p/ Retorno do Afastamento |
| UsaTlo | String(001) | Sim | Gerar Solicitação Exame p/ Transferência Local |
| UsaTca | String(001) | Sim | Gerar Solicitação Exame p/ Transferência Cargo |
| UsaTfu | String(001) | Sim | Gerar Solicitação Exame p/ Transferência Função |
| UsaDem | String(001) | Sim | Gerar Solicitação Exame p/ Demissional |
| UsaAco | String(001) | Sim | Gerar Solicitação Exame p/ Acompanhamento Demitidos |
| UsaNor | String(001) | Sim | Gerar Solicitação Exame p/ Periódico |
| CodReg | Number(003,0) | Sim | Código da Regra para Exame |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- CodExa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R108EXL_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R108EXL_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R108EXL_003

**Tabela:** R108EXA

| Origem | Destino |
|--------|---------|
| CodExa | CodExa |

