# R108EXO

## Descrição

Exames Obrigatórios Empresa

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodExa | Number(004,0) | Não | Código do Exame |
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
- CodExa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R108EXO_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R108EXO_001

**Tabela:** R108EXA

| Origem | Destino |
|--------|---------|
| CodExa | CodExa |

