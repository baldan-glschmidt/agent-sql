# R108EXC

## Descrição

Exames Obrigatórios Cargo

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
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| CodExa | Number(004,0) | Não | Código Exame |
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
- EstCar
- CodCar
- CodExa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R108EXC_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R108EXC_002

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R108EXC_003

**Tabela:** R108EXA

| Origem | Destino |
|--------|---------|
| CodExa | CodExa |

